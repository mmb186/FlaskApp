
from celery import Celery

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
	# Bind the socket to the port
	server_address = ('localhost', 10000)
	print >> sys.stderr, 'starting up on %s port %s' % server_address
	sock.bind(server_address)
	#Create Empty Protobuf object
	sensorReading = sensorData_pb2.Sensor()
	
	while True:
	    print >>sys.stderr, '\nwaiting to receive message'
	    data, address = sock.recvfrom(4096)
	   	
	   	#Parse Protobuf 
	    sensorReading.ParseFromString(data)

	    #Prettyprint Protobuf
	    print >>sys.stderr, 'Packet Recieved : \n'
	    print >>sys.stderr, sensorReading.__str__()
	    
	    #Echo The message
	    if data:

	    	

	        sent = sock.sendto(data, address)
	        print >>sys.stderr, 'sent %s bytes back to %s' % (sent, address)