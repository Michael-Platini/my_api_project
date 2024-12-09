
Aqui está o conteúdo formatado para o README.md:

markdown
Copiar código
# Item Management API

This project provides an API for managing items with the following operations:

- **Create an item**
- **List all items**
- **Update an item**
- **Delete an item**

---

## 🛠 Requirements

- **Python 3.12**
- **Flask framework**
- **Google Cloud Platform (GCP)** for deployment
- **Pytest** for testing

---

## 🌟 Features

- **Item Fields:**
  - `name` (string)
  - `value` (float)
  - `is_electronic` (boolean, optional)
  - `creation_date` (datetime, auto-generated)
  
- **Supported Operations:**
  - **Create:** Adds a new item to the database.
  - **List:** Retrieves a list of all items.
  - **Update:** Modifies an existing item.
  - **Delete:** Removes an item from the list.

---

## 📥 Local Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/Michael-Platini/my_api_project.git
   cd my_api_project
Create a virtual environment and activate it:

bash
Copiar código
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
Install the dependencies:

bash
Copiar código
pip install -r requirements.txt
Run the application locally:

bash
Copiar código
python main.py
Access the API in your browser or using tools like Postman or curl:

bash
Copiar código
http://127.0.0.1:8080/
🧪 Testing
The project uses Pytest to test the API endpoints, including creation, listing, updating, and deletion of items.

To run the tests:

bash
Copiar código
pytest test_api.py
📄 Endpoints
GET /items
Description: Lists all items in the system.
Response: JSON array of items.
GET /items/<int:item_id>
Description: Retrieves an item by its ID.
Response: JSON object of the item or error message if not found.
POST /items
Description: Creates a new item.
Body: JSON object containing name (string) and value (float). is_electronic is optional.
Response: JSON object of the created item.
PUT /items/<int:item_id>
Description: Updates an existing item.
Body: JSON object containing updated name, value, and is_electronic.
Response: JSON object of the updated item.
DELETE /items/<int:item_id>
Description: Deletes an item by its ID.
Response: Confirmation message of successful deletion or error if not found.

