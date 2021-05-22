import smtplib
from email.message import EmailMessage
import sys
from email.mime.multipart import MIMEMultipart
import socket


def emailAlert(subject, body, to, bcc):
    msg = EmailMessage()
    # msg = MIMEMultipart('alternative')
    # msg.set_content(body)
    tableRows = ''

    for row in body:
        tableRows= tableRows + '''
                <tr>
                  <td>''' + str(row[0]) + '''</td>
                  <td>''' + str(row[1]) + '''</td>
                  <td>''' + str(row[2]) + '''</td>
                  <td>''' + str(row[3]) + '''</td>
                  <td>''' + str(row[4]) + '''</td>
                  <td>''' + str(row[5]) + '''</td>
                  <td>''' + str(row[6]) + '''</td>
                </tr>
        '''

    bodyNew = '''
    <!DOCTYPE html>
        <html>
          <head>
            <meta charset="utf-8" />
            <style type="text/css">
              table {
                background: white;
                border-radius:3px;
                border-collapse: collapse;
                height: auto;
                max-width: 900px;
                padding:5px;
                width: 100%;
                animation: float 5s infinite;
              }
              th {
                color:#D5DDE5;;
                background:#1b1e24;
                border-bottom: 4px solid #9ea7af;
                font-size:14px;
                font-weight: 300;
                padding:10px;
                text-align:center;
                vertical-align:middle;
              }
              tr {
                border-top: 1px solid #C1C3D1;
                border-bottom: 1px solid #C1C3D1;
                border-left: 1px solid #C1C3D1;
                color:#666B85;
                font-size:16px;
                font-weight:normal;
              }
              tr:hover td {
                background:#4E5066;
                color:#FFFFFF;
                border-top: 1px solid #22262e;
              }
              td {
                background:#FFFFFF;
                padding:10px;
                text-align:left;
                vertical-align:middle;
                font-weight:300;
                font-size:13px;
                border-right: 1px solid #C1C3D1;
              }
            </style>
          </head>
          <body>
            Dear User,<br> <br>
            We have an important update for you. New vaccine slots have been added in your area.<br> 
            The information is as provided below. Please make sure to register right away before the slots get exhausted.<br><br>
            <table>
              <thead>
                <tr style="border: 1px solid #1b1e24;">
                  <th>Session No</th>
                  <th>Address</th>
                  <th>Vaccine</th>
                  <th>Available Slot</th>
                  <th>Fee</th>
                  <th>Capacity</th>
                  <th>Min Age Limit</th>
                </tr>
              </thead>
              <tbody>''' + tableRows + '''
              </tbody>
            </table>
            <br><br>
            If you have any feedback, please back to us. <br>
            Thank you! <br>
            Team covid19-social
          </body>
        </html>
    '''
    msg.set_content(bodyNew, subtype='html')

    msg['subject'] = subject
    msg['to'] = to
    msg['Bcc'] = bcc
    user = "covid19socialcontact@gmail.com"
    msg['from'] = user
    password = "ndpxqxpvecftabyt"

    #server details
    print("Trying to connect ot server")
    server = smtplib.SMTP('smtp.gmail.com', 587)
    # server.set_debuglevel(1)
    print("connected to server")
    server.starttls()
    print("start tls")
    server.login(user, password)
    print("logged in ")
    serverResponse = server.send_message(msg)
    print("message sent")
    server.quit()
    return serverResponse

if __name__ == "__main__":
    subject = "Vaccine Slots available at your area- Hurry!"
    slots = "10:00AM-11:00AM, 11:00AM-12:00PM, 12:00PM-01:00PM, 01:00PM-04:00PM"
    sessionList = [['1', 'Gandhi Nagar', 'Cowaxin', slots, 'Rs100', '321', '45'], ['2', 'Gandhi Nagar', 'Cowaxin', slots, 'Rs100', '321', '45'], ['3', 'Gandhi Nagar', 'Cowaxin', slots, 'Rs100', '321', '45'], ['4', 'Gandhi Nagar', 'Cowaxin', slots, 'Rs100', '321', '45'], ['5', 'Gandhi Nagar', 'Cowaxin', slots, 'Rs100', '321', '45'], ['6', 'Gandhi Nagar', 'Cowaxin', slots, 'Rs100', '321', '45']]

    emailLists = ['srtestdev1@gmail.com']
    bccList = ["shubartking@gmail.com", "devanshi.verma123@gmail.com"]
    try:
        emailResponse = emailAlert(subject, sessionList, emailLists, bccList)
        print(emailResponse)
    except Exception as e:
        print(e)
    # myargs = str(sys.argv)
    # subject = myargs[1]
    # body = myargs[2]
    # to = myargs[3]
    # bcc = myargs[4]
    #
    # try:
    #     emailResponse = emailAlert(subject, body, to, bcc)
    #     print(emailResponse)
    # except Exception as e:
    #     print(e)

    # to = "someone@gmail.com"
    # cc = "anotherperson@gmail.com,someone@yahoo.com"
    # bcc = "bccperson1@gmail.com,bccperson2@yahoo.com"
    #
    # rcpt = cc.split(",") + bcc.split(",") + [to]
    # print(type(rcpt))
    # print(rcpt)