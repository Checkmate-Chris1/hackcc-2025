from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# creating the databasse
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.secret_key = "verysecret"

db = SQLAlchemy(app)

# DATABASE with datapoints, add new ones in here
class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data1 = db.Column(db.String(100), nullable=False)
    data2 = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"<Data {self.id}: {self.data1}, {self.data2}>"

# starting the database
with app.app_context():
    db.create_all()

@app.route("/send_message", methods=["POST"])
def send_message():
    msg = request.form.get("message")
    return f"You sent: {msg}"



if __name__ == "__main__":
    app.run(debug=True)
