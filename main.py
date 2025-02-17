from flask import Flask, jsonify, request

app = Flask(__name__)

# Initialize the status as False
status = False

@app.route('/status', methods=['GET'])
def get_status():
    return jsonify({"status": status})

@app.route('/status', methods=['POST'])
def post_status():
    global status
    data = request.get_json()
    if 'status' in data:
        status = data['status']
        return jsonify({"status": status}), 200
    else:
        return jsonify({"error": "Invalid input"}), 400

if __name__ == '__main__':
    app.run(debug=True)
