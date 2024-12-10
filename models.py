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
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class Item(db.Model):
    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    value = db.Column(db.Float, nullable=False)
    is_electronic = db.Column(db.Boolean, default=False)
    creation_date = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        """
        Converts the Item object to a dictionary format.

        Returns:
            dict: The item as a dictionary, including fields:
                - id: The item's ID.
                - name: The item's name.
                - value: The item's value.
                - is_electronic: Whether the item is electronic.
                - creation_date: The item's creation date as a string.
        """
        return {
            "id": self.id,
            "name": self.name,
            "value": self.value,
            "is_electronic": self.is_electronic,
            "creation_date": self.creation_date.strftime('%Y-%m-%d %H:%M:%S')
        }

