from flask import Blueprint, jsonify, request
from models import db, Item
from datetime import datetime

bp = Blueprint("routes", __name__)


@bp.route("/items", methods=["GET"])
def list_items():
    items = Item.query.all()
    return jsonify([item.to_dict() for item in items]), 200


@bp.route("/items/<int:item_id>", methods=["GET"])
def get_item(item_id):
    item = Item.query.get(item_id)
    if not item:
        return jsonify({"error": "Item not found"}), 404
    return jsonify(item.to_dict()), 200


@bp.route("/items", methods=["POST"])
def create_item():
    data = request.get_json()
    if not data or "name" not in data or "value" not in data:
        return jsonify({"error": "Invalid data"}), 400

    new_item = Item(
        name=data["name"],
        value=data["value"],
        is_electronic=data.get("is_electronic", False),
        creation_date=datetime.utcnow()
    )
    db.session.add(new_item)
    db.session.commit()
    return jsonify(new_item.to_dict()), 201


@bp.route("/items/<int:item_id>", methods=["PUT"])
def update_item(item_id):
    item = Item.query.get(item_id)
    if not item:
        return jsonify({"error": "Item not found"}), 404

    data = request.get_json()
    item.name = data.get("name", item.name)
    item.value = data.get("value", item.value)
    item.is_electronic = data.get("is_electronic", item.is_electronic)

    db.session.commit()
    return jsonify(item.to_dict()), 200


@bp.route("/items/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):
    item = Item.query.get(item_id)
    if not item:
        return jsonify({"error": "Item not found"}), 404

    db.session.delete(item)
    db.session.commit()
    return jsonify({"message": "Item deleted successfully"}), 200
