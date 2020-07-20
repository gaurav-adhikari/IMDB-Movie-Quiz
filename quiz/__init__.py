
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'btEjYQQonbKyuYL_FgFID9ywlldk_wgaEXmcMOoFpd4LJVM3UHy-AlmsOutey6Q3BAZR5-_dpg'
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///QuizSchema.db"

db = SQLAlchemy(app)
db.create_all()

from quiz import routes