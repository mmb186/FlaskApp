import socket
import sys
import sensorData_pb2


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 2004))
s.send('Hello, world')
s.close()