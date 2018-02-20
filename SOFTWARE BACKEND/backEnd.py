from flask import Flask, render_template, session, request
from flask_socketio import SocketIO, send, emit #importing SocketIO class and send function.

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
socketio = SocketIO(app) #instantiating the socketIO with the app


@app.route('/')
def index():
    return render_template('main.html')


@socketio.on('connect', namespace='/test')
def test_connect():
    print("Clinet Connnected")
    send("Client Has Connected", broadcast=True)
    # emit('my_response', {'data': 'connected'}) #BroadCast that client has connected


@socketio.on('disconnect') #socket io waits/listens to a specified event here. We are Listening to standard message event.
def test_disconnect():
    print('Client Disconnected')

# Messages from Pod -> Client
@socketio.on('podSensors', namespace='/test')
def test_PodSensors(message):
    print("POD Data Recieved.../n sending to Client...")
    emit('podData', {'data': message.data})
    # emit('podData', {'data': message['data']})

# Print Received Commands and TODO: send to pod
@socketio.on('clientCommands', namespace='/test')
def test_ClientCommands(command):
    print("Command Received from FRONEND:")
    print(command["data"]) #NOTE: 'json' and custom events deliver a JSON payload in the form of a Python Dictionary!

# handle messages that are recieved
@socketio.on('message', namespace='/test')
def handle_message(msg):
    print("Message received: " + msg)

@socketio.on('message')
def handle_message_no_namespace(msg):
    print ("Message received (no_namespace): "+ msg)



if __name__ == '__main__':
    socketio.run(app) #socketio takes typical flask app, and wrapps around it the socketio functionality
