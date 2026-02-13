# =================================================================
# NOME DO SISTEMA: VR SOLUÇÕES Sistemas
# MÓDULO: database.py (Back-end de Processamento de Dados)
# =================================================================
import os
import json
from datetime import datetime

# Ficheiros que servem como "Banco de Dados" simples
LOG_VISITAS = "visitas.txt"
LOG_VENDAS = "vendas_vrs.json"

def contar_visita_real():
    """Soma uma visita ao contador real"""
    if not os.path.exists(LOG_VISITAS):
        with open(LOG_VISITAS, "w") as f: f.write("0")
    
    with open(LOG_VISITAS, "r+") as f:
        contagem = int(f.read()) + 1
        f.seek(0)
        f.write(str(contagem))
        f.truncate()
    return contagem

def obter_total_visitas():
    """Lê o total de visitas para o Escritório"""
    if os.path.exists(LOG_VISITAS):
        with open(LOG_VISITAS, "r") as f:
            return f.read()
    return "0"

def registrar_venda_real(cliente, plano, valor):
    """Guarda a venda para o teu Fluxo de Caixa"""
    nova_venda = {
        "data": datetime.now().strftime("%d/%m/%Y %H:%M"),
        "cliente": cliente,
        "plano": plano,
        "valor": valor
    }
    # Aqui a lógica para anexar ao JSON de vendas
    return True