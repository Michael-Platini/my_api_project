from flask import Flask, jsonify, request
from models import db, Item

app = Flask(__name__)

# Configuração do banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/my_api'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializa a extensão SQLAlchemy
db.init_app(app)

#Cria as tabelas no banco de dados se não existirem.
def create_tables():
    db.create_all()

#Lista todos os itens no banco de dados.
@app.route('/items', methods=['GET'])
def list_items():
    
    items = Item.query.all()
    response = [
        {
            'id': item.id,
            'name': item.name,
            'value': item.value,
            'is_electronic': item.is_electronic,
            'creation_date': item.creation_date.strftime('%Y-%m-%d %H:%M:%S')
        }
        for item in items
    ]
    return jsonify(response), 200

#Adiciona um novo item ao banco de dados.
@app.route('/items', methods=['POST'])
def create_item():
    
    data = request.get_json()
    if not data or 'name' not in data or 'value' not in data:
        return jsonify({'error': 'Invalid data'}), 400

    new_item = Item(
        name=data['name'],
        value=data['value'],
        is_electronic=data.get('is_electronic', False)
    )
    db.session.add(new_item)
    db.session.commit()
    return jsonify({
        'id': new_item.id,
        'name': new_item.name,
        'value': new_item.value,
        'is_electronic': new_item.is_electronic,
        'creation_date': new_item.creation_date.strftime('%Y-%m-%d %H:%M:%S')
    }), 201

#Atualiza um item existente pelo ID.
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    
    item = Item.query.get(item_id)
    if not item:
        return jsonify({'error': 'Item not found'}), 404

    data = request.get_json()
    item.name = data.get('name', item.name)
    item.value = data.get('value', item.value)
    item.is_electronic = data.get('is_electronic', item.is_electronic)
    db.session.commit()
    return jsonify({
        'id': item.id,
        'name': item.name,
        'value': item.value,
        'is_electronic': item.is_electronic,
        'creation_date': item.creation_date.strftime('%Y-%m-%d %H:%M:%S')
    }), 200


#Deleta um item existente pelo ID.
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
   
    item = Item.query.get(item_id)
    if not item:
        return jsonify({'error': 'Item not found'}), 404

    db.session.delete(item)
    db.session.commit()
    return jsonify({'message': 'Item deleted successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)