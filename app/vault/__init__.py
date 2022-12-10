from flask import Blueprint

vault = Blueprint('vault', __name__)

from . import views