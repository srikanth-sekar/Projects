from flask import Flask
import random
import time

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Kubernetes Self-Healing App</h1>", 200

@app.route("/health")
def health():
    return "OK", 200

@app.route("/metrics")
def metrics():
    cpu = random.random() * 100
    return f"custom_cpu_usage {cpu}\n", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)