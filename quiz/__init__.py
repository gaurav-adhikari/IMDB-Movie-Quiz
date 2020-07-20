
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)
app.config['SECRET_KEY'] = 'btEjYQQonbKyuYL_FgFID9ywlldk_wgaEXmcMOoFpd4LJVM3UHy-AlmsOutey6Q3BAZR5-_dpg'
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///QuizSchema.db"

db = SQLAlchemy(app)

bcrypt=Bcrypt(app)

from quiz import routes

