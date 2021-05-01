from __main__ import app
from controller.generateResources import generateString

app.add_url_rule('/', view_func=generateString, methods=['POST'])
