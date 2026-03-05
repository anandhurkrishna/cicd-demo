from flask import Flask, jsonify
import time
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

# ---- Metrics ----
REQUEST_COUNT = Counter("app_requests_total", "Total App Requests")

@app.before_request
def before_request():
    REQUEST_COUNT.inc()

# ---- Main Route ----
@app.route("/")
def home():
    return "App Running"

# ---- Health Endpoint ----
@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "timestamp": time.time()
    }), 200

# ---- Metrics Endpoint ----
@app.route("/metrics")
def metrics():
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}

# ---- Run App ----
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
