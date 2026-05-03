from flask import Blueprint, jsonify, request, session

user_bp = Blueprint('user', __name__)

@user_bp.route("/login", methods=["POST"])
def login():
    session['user'] = "aarav"
    return jsonify({"login":"failed"})
 

@user_bp.route("/", methods=["GET"])
def hello():
    return {"login":"Hey"}
 