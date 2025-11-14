import sqlite3
import matplotlib.pyplot as plt

def conectar_bd():
    conexao = sqlite3.connect('estoque.db')
    return conexao

def criar_tabela():
    conn = conectar_bd()
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL UNIQUE,
            categoria TEXT,
            preco REAL NOT NULL,
            quantidade INTEGER NOT NULL
        );
    """)
    conn.commit()
    conn.close()
    print("Banco de dados e tabela 'produtos' verificados com sucesso.")

def exibir_menu():
    print("\n--- Mini-ERP de Estoque -------------------")
    print("1. Cadastrar Produto")
    print("2. Movimentação de Estoque")
    print("3. Excluir Produto")
    print("4. Mostrar Relatório Gerencial")
    print("5. Dashboard")
    print("6. Sair do Programa")
    print("---------------------------------------------")
