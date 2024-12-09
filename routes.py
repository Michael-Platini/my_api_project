"""
Module defining the API routes for item management.
"""

from flask import Blueprint, jsonify, request
from utils import (
    load_items,
    save_items,
    generate_item_id,
    format_date,
    get_current_brazil_time,
)

# Blueprint for item routes
bp = Blueprint("routes", __name__)

# Load initial items
items = load_items()


@bp.route("/items/<int:item_id>", methods=["GET"])
def get_item(item_id):
    """
    Retrieve a specific item by its ID.

    Args:
        item_id (int): The ID of the item.

    Returns:
        JSON response with the item data or an error message.
    """
    item = next((item for item in items if item["id"] == item_id), None)

    if not item:
        return jsonify({"error": "Item not found"}), 404

    return jsonify(item), 200


@bp.route("/items", methods=["GET"])
def list_items():
    """
    Retrieve a list of all items.

    Returns:
        JSON response containing a list of all items.
    """
    return jsonify(items), 200


@bp.route("/items", methods=["POST"])
def create_item():
    """
    Create a new item.

    Body:
        JSON containing the new item's data (name, value, is_electronic).

    Returns:
        JSON response with the created item data.
    """
    data = request.get_json()

    if not data or "name" not in data or "value" not in data:
        return jsonify({"error": "Invalid data"}), 400

    new_item = {
        "id": generate_item_id(items),
        "name": data["name"],
        "value": data["value"],
        "is_electronic": data.get("is_electronic", False),
        "creation_date": format_date(get_current_brazil_time()),
    }

    items.append(new_item)
    save_items(items)
    return jsonify(new_item), 201


@bp.route("/items/<int:item_id>", methods=["PUT"])
def update_item(item_id):
    """
    Update an existing item.

    Args:
        item_id (int): The ID of the item to update.

    Body:
        JSON with the updated data.

    Returns:
        JSON response with the updated item data or an error message.
    """
    item = next((item for item in items if item["id"] == item_id), None)

    if not item:
        return jsonify({"error": "Item not found"}), 404

    data = request.get_json()
    item["name"] = data.get("name", item["name"])
    item["value"] = data.get("value", item["value"])
    item["is_electronic"] = data.get("is_electronic", item["is_electronic"])

    save_items(items)
    return jsonify(item), 200


@bp.route("/items/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):
    """
    Delete an item by its ID.

    Args:
        item_id (int): The ID of the item to delete.

    Returns:
        JSON response confirming the deletion or an error message.
    """
    item = next((item for item in items if item["id"] == item_id), None)

    if not item:
        return jsonify({"error": "Item not found"}), 404

    items.remove(item)
    save_items(items)
    return jsonify({"message": "Item deleted successfully"}), 200
