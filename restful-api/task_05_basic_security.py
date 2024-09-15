#!/usr/bin/python3from flask import Flask, jsonify, requestfrom werkzeug.security import generate_password_hash, check_password_hashfrom flask_httpauth import HTTPBasicAuthfrom flask_jwt_extended import (JWTManager, create_access_token,                                jwt_required, get_jwt_identity)app = Flask(__name__)app.config['SECRET_KEY'] = 'your_secret_key_here'auth = HTTPBasicAuth()jwt = JWTManager(app)users = {    "user1": {        "username": "user1",        "password": generate_password_hash("password"),        "role": "user"    },    "admin1": {        "username": "admin1",        "password": generate_password_hash("password"),        "role": "admin"    }}@auth.verify_passworddef verify_password(username, password):    user = users.get(username)    if user and check_password_hash(user['password'], password):        return user    return None@app.route('/basic-protected')@auth.login_requireddef basic_protected():    return "Basic Auth: Access Granted"@app.route('/login', methods=['POST'])def login():    data = request.get_json()    username = data.get('username')    password = data.get('password')    user = users.get(username)    if user and check_password_hash(user['password'], password):        access_token = create_access_token(identity={'username': username,                                                     'role': user['role']})        return jsonify(access_token=access_token)    return jsonify({"error": "Invalid credentials"}), 401@app.route('/jwt-protected')@jwt_required()def jwt_protected():    return "JWT Auth: Access Granted"@app.route('/admin-only')@jwt_required()def admin_only():    current_user = get_jwt_identity()    if current_user['role'] != 'admin':        return jsonify({"error": "Admin access required"}), 403    return "Admin Access: Granted"@jwt.unauthorized_loaderdef handle_unauthorized_error(err):    return jsonify({"error": "Missing or invalid token"}), 401@jwt.invalid_token_loaderdef handle_invalid_token_error(err):    return jsonify({"error": "Invalid token"}), 401@jwt.expired_token_loaderdef handle_expired_token_error(err):    return jsonify({"error": "Token has expired"}), 401@jwt.revoked_token_loaderdef handle_revoked_token_error(err):    return jsonify({"error": "Token has been revoked"}), 401@jwt.needs_fresh_token_loaderdef handle_needs_fresh_token_error(err):    return jsonify({"error": "Fresh token required"}), 401if __name__ == "__main__":    app.run()