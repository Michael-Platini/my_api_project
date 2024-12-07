import json
import os
from datetime import datetime

# Caminho do arquivo JSON
DATA_FILE = 'items.json'

# Função para carregar os itens do arquivo JSON
def load_items():
    if not os.path.exists(DATA_FILE):
        return []  # Se o arquivo não existir, retorna uma lista vazia
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

# Função para salvar os itens no arquivo JSON
def save_items(items):
    with open(DATA_FILE, 'w') as f:
        json.dump(items, f, indent=4)

# Função para gerar novos IDs
def generate_item_id(items):
    return len(items) + 1

# Função para formatar a data
def format_date(date):
    return date.strftime('%Y-%m-%d %H:%M:%S')