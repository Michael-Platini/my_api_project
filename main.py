from flask import Flask
from models import db

# Configuração do banco de dados PostgreSQL
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/my_api'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializa a extensão SQLAlchemy
db.init_app(app)

#Cria as tabelas no banco de dados
@app.before_first_request
def create_tables():
 
    db.create_all()