#imports
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText # shit for sending emails
# vars
path = "crackList.txt"#my local dataset of emails

sender_email = "" # email I will be sending from
receiver_email = [] #intlazing the list of emails for me to send to
password = "" # special app password
subject = "yuh"
body = "body"

# Set up the server
smtp_server = "smtp.gmail.com" # the server we are using for the google thing
port = 587  # For TLS (port)

#defs
def readFile(path): # function to get the eamils and reurt them as a list
   with open(path, "r") as file:
    return file.readlines()
   
def printEmails(emails): # funtion to read the list of emails
  for email in emails:
    print(email)

def createEmails(emails, subject, sender, body, password, smpt, port):

    server = smtplib.SMTP(smtp_server, port)
    server.starttls()  # Secure the connection
    server.login(sender_email, password)

    for email in emails:
        message = MIMEMultipart()
        message["From"] = sender
        message["To"] = email
        message["Subject"] = subject
        body = body
        message.attach(MIMEText(body, "plain"))
        print(email)

        server.sendmail(sender, email, message.as_string())
        print("Email Scsessfuly sent")
    server.quit()
    return 0
  

#main
receiver_email.extend(readFile(path))
printEmails(receiver_email)
createEmails(receiver_email, subject, sender_email, body, password, smtp_server, port)


