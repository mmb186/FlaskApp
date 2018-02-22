import socket
import sys
import sensorData_pb2


# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('localhost', 10000)


sensorReading = sensorData_pb2.Sensor()
sensorReading.name = "ThermoCoupleOne"
sensorReading.value = 2
sensorReading.time = 10


message = sensorReading.SerializeToString()

try:

    # Send data
    print >>sys.stderr, 'sending "%s"' % sensorReading.__str__()
    sent = sock.sendto(message, server_address)

    # Receive response
    print >>sys.stderr, 'waiting to receive'
    data, server = sock.recvfrom(4096)
    print >>sys.stderr, 'received "%s"' % data

finally:
    print >>sys.stderr, 'closing socket'
    sock.close()
