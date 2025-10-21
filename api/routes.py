from flask import Blueprint, request, jsonify
from api.app import db
from api.models import User

api_bp = Blueprint('api', __name__)

@api_bp.route("/create", methods=["POST"])
def create_user():
    data = request.get_json()
    user = User(username=data["username"], email=data["email"])
    db.session.add(user)
    db.session.commit()
    return jsonify(user.to_dict()), 201

@api_bp.route("/update/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    user = User.query.get_or_404(user_id)
    data = request.get_json()
    user.username = data.get("username", user.username)
    user.email = data.get("email", user.email)
    db.session.commit()
    return jsonify(user.to_dict())

@api_bp.route("/delete/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": f"User {user_id} deleted"}), 200
