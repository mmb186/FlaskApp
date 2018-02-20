

"""
SocketIO Client:
    FakePOD THAT SENDS 'PodSensors'
    ****************DOES NOT WORK YET****************
"""
from random import randint

from socketIO_client import SocketIO, LoggingNamespace

# for x in range(10):
#     print ("Random Number Generated: %r" % randint(1,101) )


with SocketIO('127.0.0.1', 5000, LoggingNamespace, namespace='/test') as socketIO:
    print("FakePod Connected!")
    socketIO.send("FAKE POD IS HERE", namespace='/test',broadcast=True)
    socketIO.emit('podSensors', {'data': 'This Works'}, namespace='test/')
    socketIO.wait(seconds=1)


