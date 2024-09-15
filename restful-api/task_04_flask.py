#!/usr/bin/python3from flask import Flask, jsonify, requestapp = Flask(__name__)users = {}@app.route("/")def home():    return "Welcome to the Flask API!"@app.route("/data")def get_data():    return jsonify(list(users.keys()))@app.route("/status")def status():    return "OK"@app.route("/users/<username>")def get_user(username):    user = users.get(username)    if user:        return jsonify(user)    else:        return jsonify({"error": "User not found"}), 404@app.route("/add_user", methods=["POST"])def add_user():    user_data = request.get_json()    username = user_data.get("username")    if not username:        return jsonify({"error": "Username is required"}), 400    users[username] = user_data    return jsonify({"message": "User added", "user": user_data}), 201if __name__ == "__main__":    app.run()