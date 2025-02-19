import eventlet
eventlet.monkey_patch()

from flask import Flask
from flask_cors import CORS
from flask_socketio import SocketIO

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")

status = False

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
    status = data.get('status', status)
    print(f"Received new status: {status}")

    socketio.emit('status_update', {"status": status})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    socketio.run(app, debug=True, host="0.0.0.0", port=port)
