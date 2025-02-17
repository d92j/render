from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS

app = Flask(__name__)

CORS(app)

hasCargo = False

@app.route('/status', methods=['GET'])
def get_status():
    return jsonify({"hasCargo": hasCargo})

@app.route('/status', methods=['POST'])
def update_status():
    global hasCargo
    data = request.json
    hasCargo = data.get("hasCargo", hasCargo)  # Update only if data has 'hasCargo'
    return jsonify({"message": "Status updated", "status": {"hasCargo": hasCargo}}), 200

if __name__ == '__main__':
    app.run(debug=True)
