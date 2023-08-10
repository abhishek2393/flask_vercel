from pprint import pprint
from flask import Blueprint, jsonify, request

test = Blueprint('test', __name__)



@test.route('/thoughts', methods=['POST'])
def thoughts():
    return 'Hello World!'
