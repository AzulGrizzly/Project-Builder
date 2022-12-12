#Front End - Flet
#Back End - Flask
#DB SQL Alchemy

from enum import unique
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from uuid import uuid4
import os


db = SQLAlchemy()


def CreateUUID():
    return uuid4().hex

#Creation of the DB Model and Table Names
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.String(32), unique=True, primary_key=True,
default=CreateUUID)
    email = db.Column(db.String(355), unique=True)
    password = db.Column(db.String(), nullable=False)


#AppConfig to show what is happening in the DB (ECHO) as well as generation of the db file and storing it in this current directory. 
class AppConfiguration:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = r"sqlite:///./db.sqlite"

#Start of Flask App
app = Flask(__name__)
app.config.from_object(AppConfiguration)
db.init_app(app)

#Routes

@app.route("/")
def home():
    return "Hello World!"

@app.route('/register', methods=['POST'])
def RegisterUser():
    user_data = request.get_json()
    user = User(email=user_data['email'], password=user_data['password'])
    db.session.add(user)
    db.session.commit()
    return "done", 201

@app.route('/login', methods=['POST'])
def login():
    email = request.json('email')
    password = request.json('password')

    user = User.query.filter_by(email=email).first()

#Login errors
    if user is None:
        return jsonify({'error': 'Invalid email'}), 401

    if user.password != password:
        return jsonify({'error': 'Invalid password'}), 401

    return jsonify({'OK': 'Login Successful'}), 201

#Run App/Server without being online
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)