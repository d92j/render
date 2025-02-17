from flask import Flask, request, jsonify
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

# Store the state
hasCargo = False

@app.route('/status', methods=['GET'])
def get_status():
    return jsonify({"hasCargo": hasCargo})

@app.route('/status', methods=['POST'])
def update_status():
    global hasCargo
    data = request.json
    hasCargo = data.get("hasCargo", hasCargo)  # Update only if data has 'hasCargo'
    socketio.emit('status_update', {"hasCargo": hasCargo})  # Notify clients
    return jsonify({"message": "Status updated", "status": {"hasCargo": hasCargo}}), 200

if __name__ == '__main__':
    socketio.run(app, debug=True)
