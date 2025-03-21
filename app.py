from flask import Flask, request, jsonify
from flask_cors import CORS
from firebase_config import athlete_collection

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Welcome to AthleteEdge API!"

# Route to get athlete data
@app.route('/api/athlete/<athlete_id>', methods=['GET'])
def get_athlete(athlete_id):
    try:
        doc = athlete_collection.document(athlete_id).get()
        if doc.exists:
            return jsonify(doc.to_dict()), 200
        else:
            return jsonify({"error": "Athlete not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to add/update athlete performance data
@app.route('/api/athlete/<athlete_id>/performance', methods=['POST'])
def add_performance(athlete_id):
    try:
        performance_data = request.json
        athlete_ref = athlete_collection.document(athlete_id)
        athlete_ref.set({'performance': performance_data}, merge=True)
        return jsonify({"message": "Performance data updated"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to get all athletes
@app.route('/api/athletes', methods=['GET'])
def get_all_athletes():
    try:
        athletes = []
        for doc in athlete_collection.stream():
            athletes.append(doc.to_dict())
        return jsonify(athletes), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
