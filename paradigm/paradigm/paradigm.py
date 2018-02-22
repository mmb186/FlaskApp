import os
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO
import socket
import sys
import sensorData_pb2
from celery import Celery

from workers import make_celery,startUDPListener

app = Flask(__name__) 
app.config.from_object(__name__) 

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost/db_name'
app.config['SECRET_KEY'] = 'secret!'
app.config.update(
    CELERY_BROKER_URL='redis://localhost:6379',
    CELERY_RESULT_BACKEND='redis://localhost:6379'
)

#Initialize Celery
celery = make_celery(app)

#Create Background task for UDP listener
@celery.task(name="tasks.startUDP")
def startUDP():
	startUDPListener()
	return



@app.route('/')
def landingController():
	retval = add.startUDP()
	return 'Hello, World!'

