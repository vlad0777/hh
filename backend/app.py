from flask import Flask, jsonify, request
from backend.auth import require_auth
from backend.fetch_job import fetch_and_save_all

app = Flask(__name__)

@app.route("/api/statistics", methods=["GET"])
@require_auth
def get_statistics():
    return jsonify({"status": "ok", "message": "Statistics endpoint working"})

@app.route("/api/fetch", methods=["POST"])
@require_auth
def fetch():
    fetch_and_save_all()
    return jsonify({"status": "ok", "message": "Data fetched"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)