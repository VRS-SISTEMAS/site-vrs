# ==============================================================================
# NOME DO SISTEMA: VRS SOLUÇÕES - SISTEMAS
# MÓDULO: banco_dados_admin.py
# OBJETIVO: Gestão de Ativações e Registro de Clientes Elite
# DESENVOLVEDOR: Iara & Vitor
# ==============================================================================

import sqlite3
import os

def inicializar_banco():
    """
    Cria a estrutura de tabelas da VRS Soluções se não existir.
    Este banco armazena quem são os clientes que ativaram o sistema.
    """
    # Define o caminho do banco de dados na mesma pasta do script
    db_path = os.path.join(os.path.dirname(__file__), 'vrs_gestao.db')
    
    # Estabelece conexão com o banco de dados SQLite
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Criação da tabela de ativações com todos os campos necessários para o CEO
    # Adicionei o campo 'chave_gerada' para controle das licenças enviadas
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ativacoes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT,
            telefone TEXT,
            documento TEXT,
            id_maquina TEXT NOT NULL,
            plano TEXT NOT NULL,
            chave_gerada TEXT,
            data TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Salva as alterações e fecha a conexão com segurança
    conn.commit()
    conn.close()
    print("BANCO DE DADOS VRS SOLUÇÕES INICIALIZADO COM SUCESSO! ✅")

def registrar_nova_ativacao(nome, email, telefone, documento, id_maquina, plano, chave):
    """
    Salva uma nova venda/ativação no banco de dados da VRS Soluções.
    """
    db_path = os.path.join(os.path.dirname(__file__), 'vrs_gestao.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT INTO ativacoes (nome, email, telefone, documento, id_maquina, plano, chave_gerada)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (nome, email, telefone, documento, id_maquina, plano, chave))
    
    conn.commit()
    conn.close()

# Executa a inicialização ao rodar o script diretamente
if __name__ == "__main__":
    inicializar_banco()