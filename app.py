from flask import Flask, render_template
from controller.generateResources import generateString, notificationData, vaccineNotification
from flask_mysqldb import MySQL

app = Flask(__name__, template_folder='controller')

app.add_url_rule('/', view_func=generateString, methods=['GET', 'POST'])
app.add_url_rule('/notification', view_func=notificationData, methods=['GET', 'POST'])
app.add_url_rule('/notificationForm', view_func=vaccineNotification, methods=['GET', 'POST'])


if __name__ == '__main__':
    app.debug = True
    app.run()