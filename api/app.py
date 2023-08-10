from flask import Flask, request
from flask_cors import CORS, cross_origin
from dotenv import load_dotenv
from os import getenv

# BluePrints
from blueprints.test import test


app = Flask(__name__)
CORS(app)
app.register_blueprint(test, url_prefix='/api/test')


if __name__ == '__main__':
    app.run('0.0.0.0', port=4100, debug=True)
