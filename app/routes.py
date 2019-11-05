from app import app
from app.models import User
from flask import jsonify, request, redirect, url_for

@app.route('/')
@app.route('/index')
def index():
    return 'This is a test.'


@app.route('/api/register')
def register():

    token = request.headers.get('token')

    print(token)



@app.route('/api/login')
def login():
    pass
