from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import gemini
import process_data

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:5173"}})

# Database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.secret_key = "verysecret"
db = SQLAlchemy(app)

class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data1 = db.Column(db.String(100), nullable=False)
    data2 = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"<Data {self.id}: {self.data1}, {self.data2}>"

with app.app_context():
    db.create_all()

# Send message route
@app.route("/send_message", methods=["POST"])
def send_message():
    data = request.get_json()
    if data and "message" in data:
        user_msg = data["message"]
        backend_response = f"Flask received: {user_msg}"
    else:
        backend_response = "Hello, I am the backend. How do you do?"
    return backend_response

@app.route("/predict", methods=["POST"])
def predict():
    """
    Receives user input text and returns the top 3 predicted diseases with remedies.
    """
    data = request.get_json()
    user_input = data.get("message", "")

    if not user_input:
        return jsonify([{
            "disease": "Unknown",
            "home_remedy": "",
            "conventional_remedy": "",
            "otc_remedy": "",
            "herbal_remedy": ""
        }] * 3), 400

    symptoms: list[str] = gemini.get_symptoms(user_input)
    diseases: list[tuple[str, int]] = process_data.predict_top_diseases(symptoms, top_n=3)
    # Get top 3 results
    results = gemini.get_results(diseases)

    return jsonify(results)


if __name__ == "__main__":
    app.run(debug=True)
