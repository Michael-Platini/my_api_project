"""
Module for handling item data storage and utility functions.
"""

import json
import os

# Path to the data file
DATA_FILE = 'items.json'


def load_items():
    """
    Load items from the JSON file.

    Returns:
        list: A list of items if the file exists; otherwise, an empty list.
    """
    if not os.path.exists(DATA_FILE):
        return []

    with open(DATA_FILE, 'r') as f:
        return json.load(f)


def save_items(items):
    """
    Save items to the JSON file.

    Args:
        items (list): The list of items to save.
    """
    with open(DATA_FILE, 'w') as f:
        json.dump(items, f, indent=4)


def generate_item_id(items):
    """
    Generate a unique ID for a new item.

    Args:
        items (list): The current list of items.

    Returns:
        int: A new unique ID.
    """
    return len(items) + 1


def format_date(date):
    """
    Format a date into a string.

    Args:
        date (datetime): The date to format.

    Returns:
        str: The formatted date string.
    """
    return date.strftime('%Y-%m-%d %H:%M:%S')


items = load_items()
