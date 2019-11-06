from app import app, db
from app.models import User
from flask import jsonify, request, redirect, url_for
import jwt



@app.route('/')
@app.route('/index')
def index():
    return 'This is a test.'


@app.route('/api/register', methods=['GET', 'POST'])
def register():

    try:
        token = request.headers.get('token')



        # decode the token back to a dictionary
        data = jwt.decode(
        token,
        app.config['SECRET_KEY'],
        algorithm=['HS256']
        )
        print(data)


        #create the user
        user = User(email=data['email'], fullname=data['name'], username=data['username'])
        user.set_password(data['password'])

        db.session.add(user)
        db.session.commit()

        return jsonify({ 'Success': 'User created!'})
    except:
        return jsonify({ 'Error_001': 'User not created, try again.'})


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
