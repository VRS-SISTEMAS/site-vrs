# =================================================================
# NOME DO SISTEMA: VRS Soluções
# MÓDULO: Lógica de Persistência (backend.py)
# =================================================================
import sqlite3
import os

def salvar_ativacao(dados):
    """
    Salva os dados de ativação no banco de dados da VRS Soluções.
    """
    try:
        db_path = os.path.join(os.path.dirname(__file__), 'vrs_gestao.db')
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        cursor.execute('''
            INSERT INTO ativacoes (nome, email, telefone, documento, id_maquina, plano)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (
            dados.get('nome'),
            dados.get('email'),
            dados.get('telefone'),
            dados.get('documento'),
            dados.get('id'),
            dados.get('plano')
        ))

        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(f"Erro VRS Soluções: {e}")
        return False