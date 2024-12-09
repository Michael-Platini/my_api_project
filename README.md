# Item Management API

This project provides an API for managing items with the following operations:
- Create an item
- List all items
- Update an item
- Delete an item

## Requirements:
- Python 3.12
- Flask framework
- Google Cloud Platform (GCP) for deployment
- Pytest for testing

## Features:
- **Item Fields**: `name`, `value`, `is_electronic`, `creation_date`
- **Operations**:
  - **Create**: Adds a new item to the database.
  - **List**: Retrieves a list of all items.
  - **Update**: Modifies an existing item.
  - **Delete**: Removes an item from the list.
  
## Setup:

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   
2.  To run the API locally, execute:
bash
Copiar código
python main.py


3. The application will be available at http://127.0.0.1:5000. 



Testing:
Pytest is used to test the API endpoints.
Tests cover the creation, listing, updating, and deletion of items.

To run the tests:
pytest test_api.py
   


Endpoints:

GET: /items
Description: Lists all items in the system.
Response: JSON array of items.


GET: /items/<int:item_id>
Description: Retrieves an item by its ID.
Response: JSON object of the item or error message if not found.


POST: /items
Description: Creates a new item.
Body: JSON object containing name and value. is_electronic is optional.
Response: JSON object of the created item.


PUT: /items/<int:item_id>
Description: Updates an existing item.
Body: JSON object containing updated name, value, and is_electronic.
Response: JSON object of the updated item.


DELETE: /items/<int:item_id>

Description: Deletes an item by its ID.
Response: Confirmation message of successful deletion or error if not found.
Deployment on Google Cloud Platform (GCP):
Deploy your app to GCP following the official Flask deployment guide for Google Cloud.
Make sure to set the FLASK_ENV environment variable to production.
