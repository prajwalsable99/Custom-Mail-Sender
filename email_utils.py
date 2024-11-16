import random


#note we have not used any mail server we are simly randomly returning false and true and saving transaction to db

def send_email(to_email, subject,content ):
    status =  random.choice(["Success", "Fail"])
    return status