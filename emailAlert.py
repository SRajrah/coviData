import smtplib
from email.message import EmailMessage
import sys
from email.mime.multipart import MIMEMultipart
import socket


def emailAlert(subject, body, to, bcc):
    msg = EmailMessage()
    # msg = MIMEMultipart('alternative')
    # msg.set_content(body)
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
            Dear Somebody,<br> <br>
            Bla-bla-bla<br><br>
            <table>
              <thead>
                <tr style="border: 1px solid #1b1e24;">
                  <th>head1</th>
                  <th>head2</th>
                  <th>head3</th>
                  <th>head4</th>
                  <th>head5</th>
                  <th>head6</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>1</td>
                  <td>2</td>
                  <td>3</td>
                  <td>4</td>
                  <td>5</td>
                  <td>6</td>
                </tr>
                <tr>
                  <td>1</td>
                  <td>2</td>
                  <td>3</td>
                  <td>4</td>
                  <td>5</td>
                  <td>6</td>
                </tr>
              </tbody>
            </table>
            <br>
            Bla-bla.<br>
            ''' + body + '''
            <a href='mailto:some_email@gmail.com'>some_email@gmail.com</a>.<br> <br>
            Thank you!
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
    # emailLists = []
    # for i in range(4):
    #     emailLists.append("srtestdev1+testing"+str(i)+"@gmail.com")
    #
    # print(emailLists)
    # try:
    #     emailResponse = emailAlert("New SLot yyy -Hello world test!", "Hi there! This is a test email you are receiving as you are lovely.", emailLists, ["shubartking@gmail.com", "devanshi.verma123@gmail.com"])
    #     print(emailResponse)
    # except Exception as e:
    #     print(e)
    myargs = str(sys.argv)
    subject = myargs[1]
    body = myargs[2]
    to = myargs[3]
    bcc = myargs[4]

    try:
        emailResponse = emailAlert(subject, body, to, bcc)
        print(emailResponse)
    except Exception as e:
        print(e)

    # to = "someone@gmail.com"
    # cc = "anotherperson@gmail.com,someone@yahoo.com"
    # bcc = "bccperson1@gmail.com,bccperson2@yahoo.com"
    #
    # rcpt = cc.split(",") + bcc.split(",") + [to]
    # print(type(rcpt))
    # print(rcpt)