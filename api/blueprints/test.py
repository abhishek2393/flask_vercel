from pprint import pprint
from flask import Blueprint, jsonify, request

posts = Blueprint('test', __name__)



@posts.route('/thoughts', methods=['POST'])
def thoughts():
    return 'Hello World!'
