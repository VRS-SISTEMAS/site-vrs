import sqlite3
import os

def inicializar_banco():
    """
    Cria a estrutura de tabelas da VRS Soluções se não existir.
    """
    db_path = os.path.join(os.path.dirname(__file__), 'vrs_gestao.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ativacoes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            email TEXT,
            telefone TEXT,
            documento TEXT,
            id_maquina TEXT,
            plano TEXT,
            data TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()