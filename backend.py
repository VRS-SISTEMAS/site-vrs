# =================================================================
# NOME DO SISTEMA: VR SOLUÇÕES Sistemas
# MÓDULO: backend.py (O Coração do Servidor)
# =================================================================
import json
import os
import datetime

# Nomes dos arquivos de banco de dados locais
DB_VENDAS = "vendas_vrs.json"
DB_VISITAS = "visitas.txt"

def registrar_visita():
    """Soma +1 ao contador de visitas real do site"""
    if not os.path.exists(DB_VISITAS):
        with open(DB_VISITAS, "w") as f: f.write("0")
    with open(DB_VISITAS, "r+") as f:
        try:
            conteudo = f.read()
            cont = int(conteudo) if conteudo else 0
        except ValueError:
            cont = 0
        cont += 1
        f.seek(0)
        f.write(str(cont))
        f.truncate()
    return cont

def salvar_venda(cliente, plano, valor):
    """Registra uma venda confirmada no banco de dados JSON"""
    # Captura a data e hora exata da venda
    agora = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    
    venda = {
        "data": agora, 
        "cliente": cliente if cliente else "Cliente Não Identificado",
        "plano": plano,
        "valor": valor,
        "status": "Pago"
    }
    
    vendas = []
    # Se o arquivo já existir, lê as vendas anteriores
    if os.path.exists(DB_VENDAS):
        with open(DB_VENDAS, "r", encoding="utf-8") as f:
            try:
                vendas = json.load(f)
            except Exception:
                vendas = []
                
    # Adiciona a nova venda na lista
    vendas.append(venda)
    
    # Salva a lista atualizada
    with open(DB_VENDAS, "w", encoding="utf-8") as f:
        json.dump(vendas, f, indent=4, ensure_ascii=False)
    return True