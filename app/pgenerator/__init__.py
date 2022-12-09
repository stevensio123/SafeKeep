
from flask import Blueprint

pgenerator = Blueprint('pgenerator', __name__)

from . import views

