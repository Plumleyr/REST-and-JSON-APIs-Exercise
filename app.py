"""Flask app for Cupcakes"""
from flask import Flask, render_template
from models import db, connect_db
from api import api_bp

app = Flask(__name__)

app.register_blueprint(api_bp)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///cupcakes"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True

connect_db(app)

app.config["SECRET_KEY"] = "ZZZZZ"

@app.route("/")
def show_homepage():
    return render_template("index.html")