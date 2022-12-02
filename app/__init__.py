import os

from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_login import LoginManager, current_user, login_required
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy


from config import config

# Extensions
bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLAlchemy()

#
login_manager = LoginManager()
login_manager.login_view = 'auth.login'



def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    
    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)

    login_manager.init_app(app)

    # initialize SQLAlchemy
    db.init_app(app)

    # initialize Bootstrap
    bootstrap.init_app(app)

    @app.route('/')
    def index():
        return render_template('base.html', user=current_user)

    # Blueprints
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    @app.before_first_request
    def create_tables():
        db.create_all()
        print('Created Database')

    return app