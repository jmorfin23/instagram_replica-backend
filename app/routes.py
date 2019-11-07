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

        return jsonify({ 'message': 'success', 'User': 'Success User Created!' })
    except:
        return jsonify({ 'Error_001': 'User not created, try again.'})


@app.route('/api/login', methods=['GET', 'POST'])
def login():

    token = request.headers.get('token')

    print(token)

    #decrypt the token
    data = jwt.decode(
    token,
    app.config['SECRET_KEY'],
    algorithm=['HS256']
    )

    print(data)

    #check if user is in database
    user = User.query.filter_by(email=data['email']).first()

    if user is None or not user.check_password(data['password']):
        return jsonify({ 'message': 'Error #002: Invalid credentials' })

    # create a token and return it
    return jsonify({ 'message': 'success', 'token': user.get_token(), 'email': user.email, 'username': user.username, 'url': user.url, 'fullname': user.fullname, 'iat': data['iat'], 'exp': data['exp']})
