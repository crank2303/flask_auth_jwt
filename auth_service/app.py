import os

from flask import Flask
from flask_redoc import Redoc

app = Flask(__name__)

app.config['REDOC'] = {
    'spec_route': '/docs',
    'title': 'Flask Auth Service',}

redoc = Redoc(app, 'service.yml')


@app.route('/')
def index():
    return "Hello World!"


if __name__ == "__main__":
    app.run()
