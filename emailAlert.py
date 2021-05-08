import smtplib
from email.message import EmailMessage
import socket


def emailAlert(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to
    user = "covid19socialcontact@gmail.com"
    msg['from'] = user
    password = "ndpxqxpvecftabyt"

    #server details
    print("Trying to connect ot server")
    server = smtplib.SMTP('smtp.gmail.com', 587)
    print("connected to server")
    server.starttls()
    print("start tls")
    server.login(user, password)
    print("logged in ")
    server.send_message(msg)
    print("message sent")
    server.quit()

if __name__ == "__main__":
    emailAlert("Hello world test!", "Hi there! This is a test email you are receiving as you are lovely.", "devanshi.verma123@gmail.com")