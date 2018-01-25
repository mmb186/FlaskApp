import os
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO

app = Flask(__name__) # create the application instance :)
app.config.from_object(__name__) # load config from this file 

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost/db_name'
app.config['SECRET_KEY'] = 'secret!'

@app.route('/')
def landingController():
	return 'Hello, World!'

