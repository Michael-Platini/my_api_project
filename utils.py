"""
Utility functions for item management.
"""

import json
import os
from datetime import datetime
import pytz

# Path to the JSON file
DATA_FILE = 'items.json'


def load_items():
    """
    Load items from the JSON file.

    Returns:
        list: A list of items.
    """
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r') as f:
        return json.load(f)


def save_items(items):
    """
    Save items to the JSON file.

    Args:
        items (list): List of items to save.
    """
    with open(DATA_FILE, 'w') as f:
        json.dump(items, f, indent=4)


def generate_item_id(items):
    """
    Generate a unique ID for a new item.

    Args:
        items (list): List of current items.

    Returns:
        int: A new unique ID.
    """
    return len(items) + 1


def format_date(date):
    """
    Format a datetime object to a string.

    Args:
        date (datetime): The datetime object to format.

    Returns:
        str: The formatted date string.
    """
    return date.strftime('%Y-%m-%d %H:%M:%S')


def get_current_brazil_time():
    """
    Get the current date and time in Brazil's timezone.

    Returns:
        datetime: The current date and time in Brazil's timezone.
    """
    brazil_timezone = pytz.timezone('America/Sao_Paulo')
    return datetime.now(brazil_timezone)
