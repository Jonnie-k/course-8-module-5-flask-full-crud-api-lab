from flask import Flask, jsonify, request

app = Flask(__name__)

# Simulated data
class Event:
    def __init__(self, id, title):
        self.id = id
        self.title = title

    def to_dict(self):
        return {"id": self.id, "title": self.title}

# In-memory "database"
events = [
    Event(1, "Tech Meetup"),
    Event(2, "Python Workshop")
]


@app.route("/")
def home():
    return jsonify({"message": "Welcome to the Events API"})


@app.route("/events", methods=["GET"])
def get_events():
    return jsonify([event.to_dict() for event in events])


@app.route("/events", methods=["POST"])
def create_event():
    data = request.get_json()

    if not data or "title" not in data:
        return jsonify({"error": "Title is required"}), 400

    new_event = Event(len(events) + 1, data["title"])
    events.append(new_event)

    return jsonify(new_event.to_dict()), 201


@app.route("/events/<int:event_id>", methods=["PATCH"])
def update_event(event_id):
    data = request.get_json()

    for event in events:
        if event.id == event_id:
            if "title" in data:
                event.title = data["title"]
            return jsonify(event.to_dict())

    return jsonify({"error": "Event not found"}), 404


@app.route("/events/<int:event_id>", methods=["DELETE"])
def delete_event(event_id):
    for event in events:
        if event.id == event_id:
            events.remove(event)
            return jsonify({"message": "Event deleted"})

    return jsonify({"error": "Event not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)