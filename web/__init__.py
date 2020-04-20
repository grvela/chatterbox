from flask import Flask

app = Flask(__name__)

from web.controllers import routes
