from flask import Blueprint, jsonify, session

auth_bp = Blueprint('auth', __name__)

@auth_bp.route("/getauth", methods=["GET"])
def getauth():
    if 'user' in session:
        print(session['user'])
    return jsonify({"aarav": 1})
 