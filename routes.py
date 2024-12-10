"""
Routes for managing items in the Flask application.

This module defines the routes for:
    - Listing all items.
    - Retrieving a specific item by ID.
    - Creating a new item.
    - Updating an existing item by ID.
    - Deleting an item by ID.

Each route interacts with the database using SQLAlchemy and returns data in JSON format.
"""

from flask import Blueprint, jsonify, request
from models import db, Item
from datetime import datetime

bp = Blueprint("routes", __name__)


@bp.route("/items", methods=["GET"])
def list_items():
    """
    Fetches all items from the database.

    Returns:
        JSON: List of all items in the database.
    """
    items = Item.query.all()
    return jsonify([item.to_dict() for item in items]), 200


@bp.route("/items/<int:item_id>", methods=["GET"])
def get_item(item_id):
    """
    Fetches a single item by its ID from the database.

    Args:
        item_id (int): The ID of the item to retrieve.

    Returns:
        JSON: The item data or an error message if not found.
    """
    item = Item.query.get(item_id)
    if not item:
        return jsonify({"error": "Item not found"}), 404
    return jsonify(item.to_dict()), 200


@bp.route("/items", methods=["POST"])
def create_item():
    """
    Creates a new item in the database.

    Expects JSON data with the following fields:
        - name: The name of the item (string)
        - value: The value of the item (float)
        - is_electronic: (Optional) Whether the item is electronic (boolean)

    Returns:
        JSON: The created item data or an error message if invalid data is provided.
    """
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
    """
    Updates an existing item by its ID.

    Args:
        item_id (int): The ID of the item to update.

    Returns:
        JSON: The updated item data or an error message if the item is not found.
    """
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
    """
    Deletes an existing item by its ID.

    Args:
        item_id (int): The ID of the item to delete.

    Returns:
        JSON: A message confirming the deletion or an error message if the item is not found.
    """
    item = Item.query.get(item_id)
    if not item:
        return jsonify({"error": "Item not found"}), 404

    db.session.delete(item)
    db.session.commit()
    return jsonify({"message": "Item deleted successfully"}), 200
