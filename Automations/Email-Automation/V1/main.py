from email_sender import send_mail
from config import SENDER_EMAIL, APP_PASSWORD, SUBJECT
import csv

def main():
    
    body =  """ Check my resume. """
    
    # Open receivers.csv in Read mode ("r") and call it file
    with open("receivers.csv", "r") as file:   
    # Read the CSV file as dictionaries (column name → value)
        reader = csv.DictReader(file)          

# Go through the file one row at a time
        for row in reader:  
            # Get the value under the "email" column                   
            receiver_email = row["email"]  
            
            send_mail(SENDER_EMAIL, APP_PASSWORD, receiver_email, SUBJECT, body)
                
    print("Email sent successfully.")