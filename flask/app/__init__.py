from flask import Flask

app = Flask(__name__)

# api = Api(app)

from app import views