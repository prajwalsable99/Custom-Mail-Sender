Custom Email Sender with Analytics

This is a Python-based email automation app using Streamlit for the front end, SQLite for database management, and Groq's AI service for generating custom email content. The app allows users to upload CSV files, create custom email templates, send personalized emails, view email logs, and analyze email delivery status.

Features
User Authentication: Users can sign in by providing their email address.
Email Template Customization: Create dynamic email templates with placeholders that get replaced with CSV data.
Email Sending Simulation: Simulate email sending with random success/failure statuses.
Email Logs: View logs of sent emails including timestamps, status (success/fail), and email content.
Email Analytics: View detailed analytics on the number of emails sent, successes, and failures.
Groq AI Integration: Automatically improve email templates with AI-generated content (e.g., adding a thank-you message).
Requirements
Python 3.x
Streamlit
SQLite
Pandas
Groq API Key for email content improvement
Setup
1. Clone the repository
bash
Copy code
git clone https://github.com/prajwalsable99/Custom-Mail-Sender.git
cd email-automation-app
2. Install required libraries
Install the necessary Python libraries using pip:

bash
Copy code
pip install -r requirements.txt
3. Set up your SQLite database
Ensure that the database is initialized correctly. You can do this by running the app for the first time, and the database will be automatically created.

4. Get Groq API Key
To generate email content with Groq, you will need to create an account and get an API key.

Visit Groq's website.
Sign up and get your API key.
Save your API key in the config.json file:
json
Copy code
{
    "DATABASE": "email_automation.db",
    "GROQ_API_KEY": "your_groq_api_key_here"
}
5. Run the Streamlit App
Start the Streamlit app by running:

bash
Copy code
streamlit run app.py
This will launch the app in your default web browser.

File Structure
bash
Copy code
.
├── app.py                   # Streamlit app entry point
├── config.json              # Configuration file containing database and API key
├── db_setup.py              # Database setup and operations
├── email_utils.py           # Email-related utilities (sending emails, logs)
├── groq.py                  # Groq API interaction for message generation
├── logo.jfif                # Logo for the app
├── outputs/                 # Folder containing images ss1.JPG, ss2.JPG, ss3.JPG
│   ├── ss1.JPG
│   ├── ss2.JPG
│   └── ss3.JPG
├── requirements.txt         # List of required libraries for the project
├── README.md                # This README file
└── sample_data.csv          # Sample CSV file for email generation (optional)
Usage
User Flow
Enter Email Address: On the main page, enter your email address to start.
Upload CSV File: Upload a CSV file containing the necessary data to personalize the email (e.g., recipient's name, company, location).
Customize Email Template: Define placeholders (e.g., {Company Name}) in the email template.
Generate & Send Emails: Click "Generate AND Send Emails" to process the CSV data and send personalized emails.
View Logs: Check the logs to see the status of the sent emails (success or fail).
Analytics: View analytics on email performance (total sent, successes, failures).
Email Template Example
plaintext
Copy code
Hello {Company Name},

We are delivering products {Products} to {Location}. 

Thank you,
{Your Name}
This template will be personalized for each row in the uploaded CSV file, with placeholders like {Company Name}, {Products}, and {Location} replaced by the corresponding values in the CSV.

Contributions
Feel free to contribute to this project! You can:

Fork the repository.
Create a feature branch.
Commit your changes.
Open a pull request.
License
This project is licensed under the MIT License.

Acknowledgments
Groq for the AI-powered email content enhancement.
Streamlit for the web app framework.
SQLite for the lightweight database solution.
Note:
Please remember to keep your API keys and sensitive information secure. Never upload your config.json with your API keys to a public repository.

Image Display
The images (ss1.JPG, ss2.JPG, and ss3.JPG) are displayed above to give you an idea of how the app's user interface looks and how emails are generated. These images are located in the outputs/ folder of the project.

In this version of the README, the images are displayed at the top of the file using the following markdown syntax:

markdown
Copy code
![ss1](outputs/ss1.JPG)
![ss2](outputs/ss2.JPG)
![ss3](outputs/ss3.JPG)
