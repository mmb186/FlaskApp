from celery import Celery
import socket
import sys
import sensorData_pb2

def make_celery(app):
    celery = Celery(app.import_name, broker=app.config['CELERY_BROKER_URL'])
    celery.conf.update(app.config)
    TaskBase = celery.Task
    class ContextTask(TaskBase):
        abstract = True
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)
    celery.Task = ContextTask
    return celery


def startUDPListener():
	# Create a UDP/IP socket
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	# Bind UDP socket to the port
	server_address = ('localhost', 10000)
	print >> sys.stderr, 'UDP listener on %s port %s' % server_address
	sock.bind(server_address)
	

	dbSock =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	dbSockserver_address = ('localhost', 2004)
	print >> sys.stderr, 'dataBaseIO client on %s port %s' % dbSockserver_address
	dbSock.connect(dbSockserver_address)


	#Create Empty Protobuf object
	dataPoint = sensorData_pb2.dataPoint()
	pointPackage = sensorData_pb2.pointPackage()

	while True:
	    print >>sys.stderr, '\nwaiting to receive message'
	    data, address = sock.recvfrom(4096)
	   	
	    #Echo The message
	    if data:
	    	#Prettyprint Protobuf
	    	print >>sys.stderr, 'Packet Recieved : \n'
	    	
	    	dataPoint.ParseFromString(data)
	    	print >>sys.stderr, dataPoint.__str__()
	    	
	    	pointPackage.points.extend([dataPoint])
	    	dataPoint.Clear()

	    	print >>sys.stderr, 'Current Package Contents %s' % pointPackage.__str__()

	        if len(pointPackage.points) > 3:
	        	print >> sys.stderr, 'WE GOT TOO MANY PACKATES'
	        	dbSock.send(pointPackage.SerializeToString())
	        	pointPackage.Clear()






	        	
def dataBaseIO():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind(('localhost', 2004))
	s.listen(1)
	conn, addr = s.accept()
	while 1:
	    data = conn.recv(1024)
	    if data = 'exit'
	    	break
	    if data: 
	    	print >> sys.stderr, 'START DATABASE IO'
	    	package = sensorData_pb2.pointPackage()
	    	package.ParseFromString(data)
	    	print >> sys.stderr , package.__str__()
	conn.close()


