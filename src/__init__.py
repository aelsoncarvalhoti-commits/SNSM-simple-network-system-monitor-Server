from flask import Flask

app = Flask(__name__)

from .controllers.controller_web import *
from .controllers.controller_api import *