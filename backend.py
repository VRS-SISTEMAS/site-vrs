# =================================================================
# NOME DO SISTEMA: VRS Soluções
# MÓDULO: Lógica de Persistência (backend.py)
# =================================================================
import sqlite3
import os

def salvar_ativacao(dados):
    """
    Salva os dados de ativação no banco de dados SQLite da VRS Soluções.
    """
    try:
        # Define o caminho absoluto para o banco de dados no servidor
        db_path = os.path.join(os.path.dirname(__file__), 'vrs_gestao.db')
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Insere os dados garantindo que todos os campos existam
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
        # Mostra o erro exato no log do Streamlit caso falhe
        print(f"Erro VRS Soluções (Salvar): {e}")
        return False