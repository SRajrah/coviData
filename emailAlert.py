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
    password = "nqgmoerkrpssctxg"

    #server details
    server = smtplib.SMTP('localhost', 8080)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)
    server.quit()

if __name__ == "__main__":
    print(socket.getaddrinfo('localhost', 8080))
    emailAlert("Hello world test!", "Hi there!", "shubartking@gmail.com")