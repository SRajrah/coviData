from flask import Flask
from flaskext.autoversion import Autoversion
from controller.generateResources import generateString,usefulLinks, donationLinks


app = Flask(__name__, template_folder='controller')

app.add_url_rule('/', view_func=generateString, methods=['GET', 'POST'])
app.add_url_rule('/usefulLinks', view_func=usefulLinks, methods=['GET'])
app.add_url_rule('/donationLinks', view_func=donationLinks, methods=['GET'])

app.autoversion = True
Autoversion(app)

if __name__ == '__main__':
    app.debug = True
    app.run()