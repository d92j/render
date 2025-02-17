from flask import Flask, request
from flask_socketio import SocketIO
from os import environ

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/add', methods=['POST'])
def add_data():
    data = request.json
    socketio.emit('new_data', data)
    return {"message": "Data added successfully"}, 200

if __name__ == '__main__':
    port = int(environ.get("PORT", 5000))
    socketio.run(app, host='0.0.0.0', port=port)
