import os
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO
import socket
import sys, time
import sensorData_pb2
from celery import Celery

from workers import make_celery,startUDPListener,dataBaseIO

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


@celery.task(name="tasks.startDataBaseIO")
def startDataBaseIO():
	dataBaseIO()
	return


@app.route('/')
def landingController():
	startDataBaseIO.delay()
	time.sleep(2)
	startUDP.delay()
	return 'Hello, World!'


