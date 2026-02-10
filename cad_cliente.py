# =================================================================
# NOME DO SISTEMA: VR SOLUÇÕES Sistemas
# MÓDULO: cad_cliente.py (Gestão de Dados dos Clientes)
# =================================================================
import csv
import os
from datetime import datetime

def salvar_dados_vrs(nome, telefone, email, id_pc, plano):
    """
    Salva os dados do cliente em uma planilha CSV para controle da VR Soluções.
    """
    arquivo = "clientes_vrs.csv"
    data_hoje = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    
    # Prepara a linha com as informações
    nova_linha = [data_hoje, nome, telefone, email, id_pc, plano]
    
    # Verifica se o arquivo já existe para não repetir o cabeçalho
    existe = os.path.isfile(arquivo)
    
    try:
        with open(arquivo, mode='a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            # Se o arquivo for novo, cria o cabeçalho (os títulos das colunas)
            if not existe:
                writer.writerow(["Data/Hora", "Nome", "Telefone", "Email", "ID Computador", "Plano"])
            
            # Grava os dados do cliente
            writer.writerow(nova_linha)
        return True
    except Exception as e:
        print(f"Erro ao salvar dados: {e}")
        return False

# Comentário: Vitor, este arquivo criará um 'clientes_vrs.csv' na mesma pasta.
# Você pode abrir esse arquivo direto no Excel para ver seus clientes.