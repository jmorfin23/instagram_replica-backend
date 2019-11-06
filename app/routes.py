from app import app
from app.models import User
from flask import jsonify, request, redirect, url_for
import jwt



@app.route('/')
@app.route('/index')
def index():
    return 'This is a test.'


@app.route('/api/register', methods=['GET', 'POST'])
def register():

    print('test')
    token = request.headers.get('token')

    print('test02')


    # decode the token back to a dictionary
    data = jwt.decode(
    token,
    app.config['SECRET_KEY'],
    algorithm=['HS256']
    )
    print(data)

    #create the user




    return jsonify({ 'Success': 'There was something returned!'})


    # except:
    #     return jsonify({ 'Error_001': 'There is an error withing /api/register'})


@app.route('/api/login', methods=['GET', 'POST'])
def login():
    print('*****************')
    print('*****************')
    print('*****************')
    print('inside login API')
    print('*****************')
    print('*****************')
    print('*****************')
    return jsonify({ 'Success': 'There was something returned!'})
