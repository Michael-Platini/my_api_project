from flask import Blueprint, jsonify, request
from datetime import datetime
from utils import load_items, save_items, generate_item_id, format_date

# Rota de items
bp = Blueprint('routes', __name__)

# Função para carregar os itens
items = load_items()

# Rota para listar todos os itens
@bp.route('/items', methods=['GET'])
def list_items():
    return jsonify(items), 200

# Rota para criar um novo item
@bp.route('/items', methods=['POST'])
def create_item():
    data = request.get_json()
    
    if not data or 'name' not in data or 'value' not in data:
        return jsonify({'error': 'Invalid data'}), 400
    
    new_item = {
        'id': generate_item_id(items),
        'name': data['name'],
        'value': data['value'],
        'is_electronic': data.get('is_electronic', False),
        'creation_date': format_date(datetime.utcnow())
    }
    
    items.append(new_item)
    save_items(items)  # Salva no arquivo JSON após adicionar
    return jsonify(new_item), 201

# Rota para atualizar um item
@bp.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    
    if not item:
        return jsonify({'error': 'Item not found'}), 404
    
    data = request.get_json()
    item['name'] = data.get('name', item['name'])
    item['value'] = data.get('value', item['value'])
    item['is_electronic'] = data.get('is_electronic', item['is_electronic'])
    
    save_items(items)  # Salva no arquivo JSON após atualizar
    return jsonify(item), 200

# Rota para deletar um item
@bp.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    
    if not item:
        return jsonify({'error': 'Item not found'}), 404
    
    items.remove(item)
    save_items(items)  # Salva no arquivo JSON após deletar
    return jsonify({'message': 'Item deleted successfully'}), 200