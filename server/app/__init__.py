from flask import Flask
from flask_login import LoginManager
# from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)
# api = Api(app)

from app import routes, models