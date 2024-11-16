

from groq import Groq
import json
# Load configuration
with open('config.json', 'r') as config_file:
    config = json.load(config_file)

GROQ_API_KEY = config['GROQ_API_KEY']

client = Groq(    api_key=GROQ_API_KEY,)


def generate_custom_message(template, row,from_user):
    # Replace placeholders in the template
    for col in row.index:
        placeholder = f"{{{col}}}"
        template = template.replace(placeholder, str(row[col]))
    
  




    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": f"improve email :\n{template} and add thank you from {from_user} in th end of mailtext,dont write subject and extra parameters",
            }
        ],
        model="llama3-8b-8192",
    )

    # print(chat_completion.choices[0].message.content)
    resp=chat_completion.choices[0].message.content
    resp=resp.replace('Here is a revised version of your email:','') 
    resp=resp.replace('Here is an improved version of the email:','')
    return resp 