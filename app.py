from flask import Flask, jsonify
import time

app = Flask(__name__)

@app.route("/")
def home():
    return "App Running"

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "timestamp": time.time()
    }), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
