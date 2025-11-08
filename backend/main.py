from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

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

if __name__ == "__main__":
    app.run(debug=True)
