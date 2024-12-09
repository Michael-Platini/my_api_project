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

## 📥 Local Installation

1. **Clone this repository**:
   
git clone https://github.com/Michael-Platini/my_api_project.git
cd my_api_project
   
2. **Create a virtual environment and activate it**:


   python3 -m venv venv

   source venv/bin/activate  - Linux/macOS

   venv\Scripts\activate     - Windows

3. **Instale as dependências**:




   pip install -r requirements.txt

Run the application locally:


python main.py

Access the API in your browser or using tools like Postman or curl:


http://127.0.0.1:8080/


## 🧪 Testing

The project uses Pytest to test the API endpoints, including creation, listing, updating, and deletion of items.

### To run the tests:
pytest test_api.py


# 📄 Endpoints

### `GET /items`
- **Descrição**: Lista todos os itens no sistema.
- **Resposta**: Array JSON contendo os itens.

### `GET /items/int:item_id`
- **Descrição**: Recupera um item pelo seu ID.
- **Resposta**: Objeto JSON do item ou mensagem de erro caso não encontrado.

### `POST /items`
- **Descrição**: Cria um novo item.
- **Corpo**: Objeto JSON contendo `name` (string) e `value` (float). `is_electronic` é opcional.
- **Resposta**: Objeto JSON do item criado.

### `PUT /items/int:item_id`
- **Descrição**: Atualiza um item existente.
- **Corpo**: Objeto JSON contendo o nome atualizado, valor e `is_electronic`.
- **Resposta**: Objeto JSON do item atualizado.

### `DELETE /items/int:item_id`
- **Descrição**: Deleta um item pelo seu ID.
- **Resposta**: Mensagem de confirmação de exclusão bem-sucedida ou erro caso não encontrado.

