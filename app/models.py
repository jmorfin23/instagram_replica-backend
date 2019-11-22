from app import db, login, app
from flask_login import UserMixin
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from time import time
import jwt



class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), index=True, unique=True)
    fullname = db.Column(db.String(64))
    username = db.Column(db.String(64), unique=True)
    url = db.Column(db.String(500), default='http://placehold.it/250x250')
    password_hash = db.Column(db.String(128))

    #sets password when registering
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    #checks password for user
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def get_token(self, expires_in=86400):
        return jwt.encode(
            { 'user_id': self.id, 'exp': time() + expires_in },
            app.config['SECRET_KEY'],
            algorithm='HS256'
        ).decode('utf-8')

    @staticmethod
    def verify_token(token):
        try:
            id = jwt.decode(
                token,
                app.config['SECRET_KEY'],
                algorithm=['HS256']
            )['user_id']
        except:
            return

        return User.query.get(id)



#create class for posts here

class Post(db.Model):
    post_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) # for logins
    message = db.Column(db.String(140))
    date_posted = db.Column(db.DateTime, default=datetime.now().date())
