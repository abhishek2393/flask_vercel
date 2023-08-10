
from flask import Blueprint

test = Blueprint('test', __name__)



@test.route('/thoughts', methods=['GET'])
def thoughts():
    return 'Hello World!'
