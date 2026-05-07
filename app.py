from flask import Flask, jsonify
from flask_cors import CORS
import psutil
import random

app = Flask(__name__)
CORS(app)


def get_metrics():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    prediction = "HEALTHY"

    if cpu > 80 or memory > 80:
        prediction = "WARNING"

    if cpu > 90 or memory > 90:
        prediction = "CRITICAL"

    return {
        "cpu": cpu,
        "memory": memory,
        "disk": disk,
        "prediction": prediction,
        "health_score": random.randint(70, 100)
    }


@app.route('/api/metrics')
def metrics():
    return jsonify(get_metrics())


if __name__ == '__main__':
    app.run(debug=True)
