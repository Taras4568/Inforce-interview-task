from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os
import time

app = Flask(__name__)

DB_HOST = os.getenv("POSTGRES_HOST", "db")
DB_PORT = os.getenv("POSTGRES_PORT", "5432")
DB_NAME = os.getenv("POSTGRES_DB", "testdb")
DB_USER = os.getenv("POSTGRES_USER", "postgres")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD", "postgres")

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

def init_db():
    connected = False
    while not connected:
        try:
            with app.app_context():  
                db.create_all()
            connected = True
        except Exception as e:
            print("Waiting for DB... retrying in 2 sec")
            time.sleep(2)

init_db()


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"}), 200

@app.route("/users", methods=["POST"])
def add_user():
    data = request.get_json()
    name = data.get("name")
    if not name:
        return jsonify({"error": "Name is required"}), 400

    user = User(name=name)
    db.session.add(user)
    db.session.commit()
    return jsonify({"id": user.id, "name": user.name}), 201

@app.route("/users", methods=["GET"])
def get_users():
    users = User.query.all()
    return jsonify([{"id": u.id, "name": u.name} for u in users])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
