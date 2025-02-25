import os
import sqlite3
from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Definir o caminho correto do banco
DB_PATH = os.path.join(os.path.dirname(__file__), 'contador.db')

# Função para obter a data alvo
def get_target_date():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Garantir que a tabela config existe antes de tentar selecionar
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='config';")
    if cursor.fetchone() is None:
        return "Erro: Tabela config não existe!"
    
    cursor.execute("SELECT target_date FROM config LIMIT 1")
    data = cursor.fetchone()
    conn.close()
    
    return data[0] if data else "Erro: Nenhuma data encontrada!"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_target_date')
def get_date():
    return jsonify({'target_date': get_target_date()})

if __name__ == '__main__':
    app.run(debug=True)
