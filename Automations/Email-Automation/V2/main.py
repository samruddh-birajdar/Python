from email_sender import send_mail
from config import SENDER_EMAIL, APP_PASSWORD, SUBJECT
import csv

def main():
      
    with open("receivers.csv", "r") as file:   
        reader = csv.DictReader(file)          

        for row in reader:   
            name = row["name"]               
            receiver_email = row["email"]  
            
            with open("body.html", "r") as html:
                body = html.read()
                
            body = body.replace("{name}", name)
            send_mail(SENDER_EMAIL, APP_PASSWORD, receiver_email, SUBJECT, body)
                
    print("Email sent successfully.")