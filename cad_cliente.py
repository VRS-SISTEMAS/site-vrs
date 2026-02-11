# =================================================================
# NOME DO SISTEMA: VR SOLUÇÕES Sistemas
# MÓDULO: cad_cliente.py (COM CAMPO CPF/CNPJ)
# =================================================================
import csv
import os
from datetime import datetime

def salvar_dados_vrs(nome, documento, telefone, email, id_pc, plano):
    """
    Registra os dados de vendas incluindo o documento (CPF/CNPJ).
    """
    arquivo = "clientes_vrs.csv"
    data_hoje = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    
    # Adicionamos o 'documento' na lista de salvamento
    nova_linha = [data_hoje, nome, documento, telefone, email, id_pc, plano]
    
    existe = os.path.isfile(arquivo)
    
    try:
        with open(arquivo, mode='a', newline='', encoding='utf-8-sig') as f:
            writer = csv.writer(f, delimiter=';')
            
            if not existe:
                writer.writerow([
                    "DATA_HORA", 
                    "NOME_CLIENTE", 
                    "CPF_CNPJ", # <--- Nova Coluna
                    "WHATSAPP", 
                    "EMAIL_CONTATO", 
                    "ID_MAQUINA", 
                    "PLANO"
                ])
            
            writer.writerow(nova_linha)
        return True
    except Exception as e:
        print(f"ERRO: {e}")
        return False