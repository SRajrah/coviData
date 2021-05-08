from flask import Flask, render_template
from controller.generateResources import generateString

import os

print("hi-", os.path.dirname(__file__))
app = Flask(__name__, template_folder='controller')

app.add_url_rule('/', view_func=generateString, methods=['GET', 'POST'])


if __name__ == '__main__':
    app.debug = True
    app.run()