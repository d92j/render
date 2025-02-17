from flask import Flask, jsonify, request

app = Flask(__name__)

status = False

@app.route('/status', methods=['GET'])
def get_status():
    """Retrieve the current status."""
    return jsonify({"status": status})

@app.route('/status', methods=['POST'])
def set_status():
    """Modify the current status."""
    global status
    data = request.get_json()
    
    if 'status' in data and isinstance(data['status'], bool):
        status = data['status']
        return jsonify({"message": "Status updated successfully", "status": status}), 200
    else:
        return jsonify({"error": "Invalid input. Expected a boolean value."}), 400

if __name__ == '__main__':
    app.run(debug=True)
