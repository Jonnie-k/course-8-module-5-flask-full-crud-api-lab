from flask import Flask, jsonify
from routes.events import events_bp

app = Flask(__name__)

app.register_blueprint(events_bp)

@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to the Events API"
    })

if __name__ == "__main__":
    app.run(debug=True)