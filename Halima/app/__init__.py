from flask import Flask
from flask_bootstrap import Bootstrap

app = Flask (__name__)

#initializing flask ext
bootstrap = Bootstrap(app)

from app import views