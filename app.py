from flask import Flask, render_template, request, jsonify
from flask_cors import CORS  # Import CORS

# Step 1: Create the Flask app instance
app = Flask(__name__)

# Step 2: Enable CORS for the app
CORS(app)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()  # Get JSON data from the request
    if not data or 'activity' not in data:
        return jsonify({"message": "Invalid input"}), 400

    suspicious_activities = ["delete_file", "access_server", "modify_permissions"]
    activity = data['activity']

    if activity in suspicious_activities:
        return jsonify({"message": "Suspicious activity detected!"})
    else:
        return jsonify({"message": "Activity is normal."})

if __name__ == '__main__':
    app.run(debug=True)