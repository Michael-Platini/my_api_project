"""
Configuração do ambiente de testes.

Este módulo configura o ambiente necessário para os testes automatizados.
Adiciona o diretório raiz do projeto ao `sys.path`, permitindo importar
corretamente os módulos do projeto.

Estrutura:
- Configura o caminho base do projeto antes de rodar os testes.

Uso:
Não é necessário chamar explicitamente este arquivo. Ele será carregado
automaticamente pelo Pytest antes da execução dos testes.
"""

import sys
import os

# Adiciona o diretório raiz do projeto ao sys.path antes de rodar os testes
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
