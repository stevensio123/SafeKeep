# Import the database object (db) from the main application module
from app import db
from werkzeug.security import check_password_hash, generate_password_hash

from flask_login import UserMixin

# Define a base model for other database tables to inherit
class Base(db.Model, UserMixin):

    __abstract__  = True

    id            = db.Column(db.Integer, primary_key=True)
    date_created  = db.Column(db.DateTime,  default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime,  default=db.func.current_timestamp(),
                                           onupdate=db.func.current_timestamp())

# Define a User model
class User(Base):

    __tablename__ = 'users'

    # User Name
    name = db.Column(db.String(64), unique=True, index=True)

    # Identification Data: email & password
    email    = db.Column(db.String(128),  nullable=False,
                                            unique=True)
    password = db.Column(db.String(192),  nullable=False)


    # New instance instantiation procedure
    def __init__(self, name, email, password):

        self.username = name
        self.email    = email
        self.password = password

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)


    def __repr__(self):
        return '<User %r>' % (self.name)  