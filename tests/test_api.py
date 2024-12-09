"""
Tests for the Item Management API

This module contains automated tests to validate the functionalities
of the item management API, including creation, listing, updating,
deletion, and error scenarios.

Requirements:
- Pytest to run the tests.
- The main application (`main.py`) to be tested.

Test Structure:
- Item creation test.
- Item listing test.
- Item updating test.
- Item deletion test.
- Error scenarios (item not found).

Execution:
To run the tests, use the command:
    pytest test_api.py
"""

import pytest
from main import app


@pytest.fixture
def client():
    """
    Sets up a test client for the Flask application.

    Returns:
        FlaskClient: Instance of the test client.
    """
    with app.test_client() as client:
        yield client


def test_create_item(client):
    """
    Tests the creation of a new item in the API.

    Scenario:
    - Sends a POST request to create an item.
    - Verifies that the item was created correctly and that the HTTP status is 201.

    Validations:
    - The fields returned in the JSON must match the sent data.
    - The 'id' field is automatically generated.
    """
    new_item = {'name': 'Book', 'value': 99.99}
    response = client.post('/items', json=new_item)
    response_data = response.json
    response_data.pop('id', None)  # Remove 'id' for validation

    assert response.status_code == 201 and response_data == {
        'name': new_item['name'],
        'value': new_item['value'],
        'is_electronic': False,
        'creation_date': response_data['creation_date']
    }


def test_list_items(client):
    """
    Tests the listing of existing items in the API.

    Scenario:
    - Sends a GET request to list the items.
    - Verifies that the response is a list and contains registered items.

    Validations:
    - The response must be a non-empty list.
    """
    response = client.get('/items')
    assert response.status_code == 200 and isinstance(
        response.json, list) and len(response.json) > 0


def test_update_item(client):
    """
    Tests the update of an existing item in the API.

    Scenario:
    - Creates a new item with a POST request.
    - Sends a PUT request to update the data of the created item.
    - Verifies that the data was correctly updated.

    Validations:
    - The HTTP status must be 200.
    - The data returned in the JSON must reflect the updates made.
    """
    new_item = {'name': 'Book', 'value': 99.99}
    create_response = client.post('/items', json=new_item)
    item_id = create_response.json['id']

    updated_item = {'name': 'Computer', 'value': 150.75, 'is_electronic': True}
    update_response = client.put(f'/items/{item_id}', json=updated_item)

    assert update_response.status_code == 200 and update_response.json == {
        'id': item_id,
        'name': updated_item['name'],
        'value': updated_item['value'],
        'is_electronic': updated_item['is_electronic'],
        'creation_date': update_response.json['creation_date']
    }


def test_delete_item(client):
    """
    Tests the deletion of an existing item in the API.

    Scenario:
    - Creates a new item with a POST request.
    - Sends a DELETE request to remove the created item.
    - Tries to fetch the deleted item and verifies that it is not found.

    Validations:
    - The HTTP status for deletion must be 200.
    - The response for fetching the deleted item must be 404.
    """
    new_item = {'name': 'Book', 'value': 99.99}
    create_response = client.post('/items', json=new_item)
    item_id = create_response.json['id']

    delete_response = client.delete(f'/items/{item_id}')
    assert delete_response.status_code == 200 and delete_response.json == {
        'message': 'Item deleted successfully'}

    check_response = client.get(f'/items/{item_id}')
    assert check_response.status_code == 404 and check_response.json == {'error': 'Item not found'}


def test_item_not_found(client):
    """
    Tests searching for a non-existent item in the API.

    Scenario:
    - Sends a GET request for an item ID that does not exist.
    - Verifies that the HTTP status is 404 and the error message is correct.

    Validations:
    - The HTTP status must be 404.
    - The error message must indicate that the item was not found.
    """
    response = client.get('/items/99999')
    assert response.status_code == 404 and response.json == {'error': 'Item not found'}
