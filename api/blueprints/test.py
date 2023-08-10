from pprint import pprint
from flask import Blueprint, jsonify, request

posts = Blueprint('posts', __name__)



@posts.route('/thoughts', methods=['POST'])
def thoughts():
    return jsonify({
        'success': True,
        'post': 'thoughts'
    })
