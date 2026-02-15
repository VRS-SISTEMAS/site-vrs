# =================================================================
# NOME DO SISTEMA: VRS Soluções
# MÓDULO: Configuração do Banco de Dados (bancodedados.py)
# =================================================================
import sqlite3

def inicializar_banco():
    """
    Cria o arquivo de banco de dados e a tabela de ativações caso não existam.
    """
    # Conecta ao arquivo de banco (será criado na pasta do projeto)
    conn = sqlite3.connect('vrs_gestao.db')
    cursor = conn.cursor()

    # Criando a tabela para armazenar os dados de ativação
    # Armazenamos Nome, Email, Telefone, Documento, ID da Máquina e o Plano
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ativacoes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            telefone TEXT,
            documento TEXT,
            id_maquina TEXT NOT NULL,
            plano TEXT,
            data_cadastro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            status_pagamento TEXT DEFAULT 'Pendente'
        )
    ''')
    
    conn.commit()
    conn.close()

# Executa a criação da tabela ao rodar o script
if __name__ == "__main__":
    inicializar_banco()
    print("Banco de dados VRS Soluções inicializado com sucesso!")