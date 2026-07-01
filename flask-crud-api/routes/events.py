from flask import Blueprint, jsonify, request
from models.data import events

events_bp = Blueprint("events", __name__)


# Helper function
def find_event(event_id):
    for event in events:
        if event["id"] == event_id:
            return event
    return None


# GET /events
@events_bp.route("/events", methods=["GET"])
def get_events():
    return jsonify(events)


# POST /events
@events_bp.route("/events", methods=["POST"])
def add_event():
    data = request.get_json()

    if not data or "title" not in data:
        return jsonify({"error": "Title is required"}), 400

    new_event = {
        "id": len(events) + 1,
        "title": data["title"],
        "location": data.get("location", "")
    }

    events.append(new_event)

    return jsonify(new_event), 201


# PATCH /events/<id>
@events_bp.route("/events/<int:event_id>", methods=["PATCH"])
def update_event(event_id):
    event = find_event(event_id)

    if not event:
        return jsonify({"error": "Event not found"}), 404

    data = request.get_json()

    if "title" in data:
        event["title"] = data["title"]

    if "location" in data:
        event["location"] = data["location"]

    return jsonify(event)


# DELETE /events/<id>
@events_bp.route("/events/<int:event_id>", methods=["DELETE"])
def delete_event(event_id):
    event = find_event(event_id)

    if not event:
        return jsonify({"error": "Event not found"}), 404

    events.remove(event)

    return jsonify({"message": "Event deleted"})