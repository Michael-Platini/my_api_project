from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
 
db = SQLAlchemy()

#Modelo de Item
class Item(db.Model):

# Atributos:
 #       id (int): Identificador único do item.
 #       name (str): Nome do item.
 #       value (float): Valor monetário do item.
 #       is_electronic (bool): Indica se o item é eletrônico.
 #       creation_date (datetime): Data de criação do item.

    __tablename__ = 'items' # Nome da tabela no banco de dados

    id = db.Column(db.Integer, primary_key=True) # Chave primária (id)
    name = db.Column(db.String(100), nullable=False) # Nome do item
    value = db.Column(db.Float, nullable=False) # Valor do item
    is_electronic = db.Column(db.Boolean, default=False) # É eletrônico?
    creation_date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)  # Data de criação automática