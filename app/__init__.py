import os

from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_login import LoginManager, current_user, login_required
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy

from config import config

from . extensions import bootstrap, mail, moment, db, login_manager
from . models import User



def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    configure_extensions(app)

    # Blueprints
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    from .pgenerator import pgenerator as pgenerator_blueprint
    app.register_blueprint(pgenerator_blueprint)

    @app.before_first_request
    def create_tables():
        db.create_all()
        print('Created Database')
        user = User(username='admin', password='admin', email='admin@example.com')
        db.session.add(user)
        db.session.commit()
        print('Added new user')

    return app



def configure_extensions(app):
    # flask-sqlalchemy
    db.init_app(app)

    # flask-bootstrap
    bootstrap.init_app(app)
    # flask-mail
    mail.init_app(app)

    # Admin
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    login_manager.init_app(app)

    # flask-moment
    moment.init_app(app)
