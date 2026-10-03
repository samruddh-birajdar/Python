import smtplib
from email.message import EmailMessage
from pathlib import Path

def send_mail(sender, app_password, receiver, subject, body):

    msg = EmailMessage()

    msg["From"] = sender
    msg["To"] = receiver
    msg["Subject"] = subject
    
    msg.set_content(body, subtype="html")
    
    folder = Path("attachments")
    print(folder)
    
    for file in folder.iterdir(): 
        with open(file, "rb") as attachment:
            file_data = attachment.read()
            msg.add_attachment(
                file_data,
                maintype = "application",
                subtype = "octet-stream",
                filename = file.name
            )

    smtp = smtplib.SMTP_SSL("smtp.gmail.com", 465)

    smtp.login(sender, app_password)
    smtp.send_message(msg)
    smtp.quit() 