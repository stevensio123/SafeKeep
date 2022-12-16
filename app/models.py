from itsdangerous import URLSafeTimedSerializer as Serializer
from flask import current_app
from app import db
from werkzeug.security import check_password_hash, generate_password_hash

from flask_login import UserMixin

from .encryption import encrypt_credential, decrypt_credential

# Define a base model for other database tables to inherit
class Base(db.Model, UserMixin):

    __abstract__  = True

    id            = db.Column(db.Integer, primary_key=True)
    date_created  = db.Column(db.DateTime,  default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime,  default=db.func.current_timestamp(),
                                           onupdate=db.func.current_timestamp())

class Credential(Base):
    __tablename__ = 'credentials'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    website = db.Column(db.String(120), nullable=False)
    username = db.Column(db.String(80), nullable=False)
    encrypted_password = db.Column(db.String(120), nullable=False)

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        user = User.query.filter_by(id=self.user_id).first()
        master_password = user.password_hash
        self.encrypted_password = encrypt_credential(password, master_password)

    def decrypt_credential(self, paswword=encrypted_password):
        user = User.query.filter_by(id=self.user_id).first()
        master_password = user.password_hash
        return decrypt_credential(paswword, master_password)


    def __repr__(self):
        return '<Credential %r>' % (self.username)


# Define a User model
class User(Base):

    __tablename__ = 'users'

    # User Name
    username = db.Column(db.String(64), unique=True, index=True)

    # Identification Data: email & password
    email    = db.Column(db.String(128),  nullable=False,
                                            unique=True)
    password_hash = db.Column(db.String(192),  nullable=False)

    credentials = db.relationship('Credential', backref='user', lazy='dynamic')

    """
    Not used: This code will be used to generate confirmation after registration
    def generate_confirmation_token(self):
        s = Serializer(current_app.config['SECRET_KEY'])
        return s.dumps({'confirm': self.id})
    """
        
    """
    def confirm(self, token, experation=3600):
        s = Serializer(current_app.config['SECRET_KEY'] )
        try:
            data = s.loads(token, max_age=experation)
        except:
            return False
        if data.get('confirm') != self.id:
            return False
        self.confirmed = True
        db.session.add(self)
        return True
    """


    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)


    def __repr__(self):
        return '<User %r>' % (self.username)  


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)

    def __repr__(self):
        return '<Role %r>' % self.name
