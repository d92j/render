import eventlet
eventlet.monkey_patch()

from flask import Flask
from flask_cors import CORS
from flask_socketio import SocketIO

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")

status = False
direction = "Aucune"
destination = "Aucune"

@app.route('/')
def home():
    return 'Server is live!', 200

@socketio.on('connect')
def handle_connect():
    print("A client connected")

@socketio.on('disconnect')
def handle_disconnect():
    print("A client disconnected")

@socketio.on('status_update')
def handle_status_update(data):
    global status
    status = bool(data.get('status', status))
    print(f"Received new status: {status}")

    socketio.emit('status_update', {"status": status})

@socketio.on('direction_update')
def handle_direction_update(data):
    global direction
    status = str(data.get('direction', direction))
    print(f"Received new direction: {direction}")

    socketio.emit('direction_update', {"direction": direction})

@socketio.on('destination_update')
def handle_destination_update(data):
    global destination
    status = str(data.get('destination', destination))
    print(f"Received new destination: {destination}")

    socketio.emit('destination_update', {"destination": destination})

@socketio.on('start')
def handle_start(data=None):
    print(f"Received start command")

    if len(socketio.server.eio.sockets) > 0:
        socketio.emit('start')

@socketio.on('stop')
def handle_stop(data=None):
    print(f"Received stop command")

    if len(socketio.server.eio.sockets) > 0:
        socketio.emit('stop')

if __name__ == '__main__':
    socketio.run(app, debug=True, host="0.0.0.0")
