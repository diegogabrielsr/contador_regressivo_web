import sqlite3
import os

# Caminho absoluto do banco de dados
DB_PATH = os.path.join(os.path.dirname(__file__), 'contador.db')

# Conectar ao banco de dados (ele será criado se não existir)
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Criar a tabela config se ainda não existir
cursor.execute('''
    CREATE TABLE IF NOT EXISTS config (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        target_date TEXT NOT NULL
    )
''')

# Limpar qualquer valor antigo e inserir a nova data
cursor.execute("DELETE FROM config")
cursor.execute("INSERT INTO config (target_date) VALUES ('2025-08-15')")

# Salvar mudanças e fechar conexão
conn.commit()
conn.close()

print("Banco de dados criado com sucesso!")
