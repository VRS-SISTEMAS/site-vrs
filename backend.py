# =================================================================
# NOME DO SISTEMA: VRS Soluções
# MÓDULO: Lógica de Persistência (backend.py)
# =================================================================
import sqlite3

def salvar_ativacao(dados):
    """
    Recebe o dicionário de dados do site e salva no banco de dados SQLite.
    """
    try:
        conn = sqlite3.connect('vrs_gestao.db')
        cursor = conn.cursor()

        # Inserindo os dados capturados no formulário do site
        cursor.execute('''
            INSERT INTO ativacoes (nome, email, telefone, documento, id_maquina, plano)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (
            dados.get('nome'),
            dados.get('email'),
            dados.get('telefone'),
            dados.get('documento'), # Adicionado para completar o perfil do cliente
            dados.get('id'),        # Este é o ID da máquina
            dados.get('plano')
        ))

        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(f"Erro ao salvar no banco da VRS: {e}")
        return False