import streamlit as st
import pandas as pd
import json
import re
from db_setup import init_db, insert_user, insert_email_log, fetch_email_logs_by_user
from email_utils import send_email
from llm_utils import generate_custom_message


with open('config.json', 'r') as config_file:
    config = json.load(config_file)

DATABASE = config['DATABASE']
init_db(DATABASE)


st.set_page_config(
    page_title="Custom Email Sender",
    page_icon="📧",
    layout="wide",
)


def is_valid_email(email):
    
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(email_regex, email):
        return True
    return False

def main():
    st.sidebar.title("Navigation")
    st.sidebar.image("logo.jfif")

    
    user_email = st.text_input("Enter your email address to proceed:", placeholder="Enter your email here")
    if not user_email:
        st.warning("Please enter your email address to start.")
        return

    
    if not is_valid_email(user_email):
        st.warning("Please enter a valid email address.")
        return

   
    user_id = insert_user(DATABASE, user_email)

   
    st.sidebar.header("User Profile")
    st.sidebar.write(f"**Email:** {user_email}")
    st.sidebar.write(f"**User ID:** {user_id}")

    # Sidebar 
    page = st.sidebar.radio("Select ", ["Send Emails", "View Logs", "Analytics"])

    if page == "Send Emails":
        send_emails_page(user_email, user_id)
    elif page == "View Logs":
        view_logs_page(user_email, user_id)
    elif page == "Analytics":
        analytics_page(user_email, user_id)

def send_emails_page(user_email, user_id):
    st.title("Email Generator")

   
    st.header("Upload CSV File")
    csv_file = st.file_uploader("Choose a CSV file", type=["csv"])

    if csv_file:
        df = pd.read_csv(csv_file)
        st.write("Uploaded Data:", df)

        
        st.header("Define Email Template")
        st.markdown(f'Following are the columns in your file: {list(df.columns)}')
        template = st.text_area("Email Template",
         value="Hello {Company Name},We are delivering prods {Products} to lo {Location}")
        st.markdown('Example: Hello {Company Name},')
        email_sub = st.text_input("Enter your Subject", 'Subject:')

      
        st.header("Generate and Send Emails")
        sent_btn = st.button("Generate AND Send Emails")

        if sent_btn:
            previews = []
            for _, row in df.iterrows():
                content = generate_custom_message(template, row, user_email)
                previews.append(content)
            df["Generated mailtext"] = previews
            
            st.write("Preview Emails:", df[["Email", "Generated mailtext"]])

            for _, row in df.iterrows():
                status = send_email(
                    to_email=row["Email"],
                    subject=email_sub,
                    content=row['Generated mailtext']
                )
                insert_email_log(DATABASE, user_id, row["Email"], email_sub + "\nText: " + row['Generated mailtext'], status)
                print(status)

            st.success("Emails are being sent ,go check logs")

def view_logs_page(user_email, user_id):
    st.title("Your Email Logs")

   
    # st.header("Your Email Logs")
    emails_logs = fetch_email_logs_by_user(DATABASE, user_id)

    if emails_logs.empty:
        st.warning("No email logs found for this user.")
    else:
        st.write(emails_logs)

def analytics_page(user_email, user_id):
    st.title("Email Analytics")

   
    emails_logs = fetch_email_logs_by_user(DATABASE, user_id)
    
    if emails_logs.empty:
        st.warning("No email logs found for this user.")
        return

    # Analytics tabs
    tab = st.selectbox("Select Analytics View", ["Total Emails Sent", "Successes", "Failures"])

    if tab == "Total Emails Sent":
        st.subheader("Total Emails Sent")
        total_sent = len(emails_logs)
        st.write(f"Total emails sent: {total_sent}")

    elif tab == "Successes":
        st.subheader("Success Emails")
       
        success_logs = emails_logs[emails_logs['status'] != 'Fail']  
        st.write(f"Total Successes: {len(success_logs)}")
        st.write(success_logs)

    elif tab == "Failures":
        st.subheader("Failed Emails")
        failed_logs = emails_logs[emails_logs['status'] == 'Fail']
        st.write(f"Total Failures: {len(failed_logs)}")
        st.write(failed_logs)

if __name__ == "__main__":
    main()
