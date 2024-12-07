# models.py
import json
import os  # Adicionando a importação do módulo os
from datetime import datetime

# Caminho do arquivo de dados
DATA_FILE = 'items.json'

def load_items():
    """Carrega os itens do arquivo JSON"""
    if not os.path.exists(DATA_FILE):  # Verifica se o arquivo existe
        return []

    with open(DATA_FILE, 'r') as f:
        return json.load(f)

def save_items(items):
    """Salva os itens no arquivo JSON"""
    with open(DATA_FILE, 'w') as f:
        json.dump(items, f, indent=4)

def generate_item_id(items):
    """Gera um ID único para o novo item"""
    return len(items) + 1

def format_date(date):
    """Formata a data para o formato adequado"""
    return date.strftime('%Y-%m-%d %H:%M:%S')

# Carrega os itens do arquivo JSON
items = load_items()