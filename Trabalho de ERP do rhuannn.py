import sqlite3
import matplotlib.pyplot as plt
from datetime import datetime

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
            quantidade INTEGER NOT NULL,
            data_cadastro TEXT,
            data_ultima_saida TEXT
        );
    """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS movimentacoes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            produto_id INTEGER NOT NULL,
            data_movimentacao TEXT NOT NULL,
            tipo TEXT NOT NULL, 
            quantidade INTEGER NOT NULL,
            FOREIGN KEY(produto_id) REFERENCES produtos(id)
        );
    """)
    
    conn.commit()
    conn.close()
    print("Banco de dados e tabelas verificados com sucesso.")
    
def registrar_movimentacao(produto_id, tipo, quantidade):
    conn = conectar_bd()
    cursor = conn.cursor()
    data_hora_movimentacao = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    cursor.execute("""
        INSERT INTO movimentacoes (produto_id, data_movimentacao, tipo, quantidade) 
        VALUES (?, ?, ?, ?)
    """, (produto_id, data_hora_movimentacao, tipo, quantidade))
    
    conn.commit()
    conn.close()

def exibir_menu():
    print("\n--- Mini-ERP de Estoque -------------------")
    print("1. Cadastrar Produto")
    print("2. Movimentação de Estoque")
    print("3. Excluir Produto")
    print("4. Mostrar Relatório Gerencial")
    print("5. Dashboard")
    print("6. Sair do Programa")
    print("---------------------------------------------")
