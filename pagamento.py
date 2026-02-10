# =================================================================
# NOME DO SISTEMA: VR SOLUÇÕES Sistemas
# MARCA EXIBIDA: VRS Soluções
# MÓDULO: Gestão de Pagamentos via API Mercado Pago
# =================================================================

import mercadopago
import datetime  # <--- ESSA LINHA RESOLVE O ERRO "reportUndefinedVariable"
import streamlit as st

# --- CONFIGURAÇÃO DAS CHAVES DA VR SOLUÇÕES ---
ACCESS_TOKEN = "SEU_ACCESS_TOKEN_AQUI" 
sdk = mercadopago.SDK(ACCESS_TOKEN)

def criar_pix_vrs(id_maquina, plano_nome):
    """
    Gera um pagamento Pix personalizado com base no plano escolhido.
    """
    # Lógica de preços da VR Soluções
    valores = {
        "Básico": 59.90,
        "Junior": 99.90,
        "Senior": 149.90
    }
    
    valor_final = valores.get(plano_nome, 59.90)

    payment_data = {
        "transaction_amount": valor_final,
        "description": f"Assinatura {plano_nome} VRS Soluções - ID: {id_maquina}",
        "payment_method_id": "pix",
        "payer": {
            "email": "vrsolucoes.vendas@gmail.com", 
            "first_name": "Cliente",
            "last_name": "VRS"
        },
        # Agora o datetime está definido e vai funcionar aqui:
        "date_of_expiration": (datetime.datetime.now() + datetime.timedelta(minutes=30)).isoformat()
    }

    try:
        resultado = sdk.payment().create(payment_data)
        pagamento = resultado["response"]

        info_pagamento = {
            "id": pagamento["id"],
            "copia_e_cola": pagamento["point_of_interaction"]["transaction_data"]["qr_code"],
            "qr_code_imagem": pagamento["point_of_interaction"]["transaction_data"]["qr_code_base64"],
            "status": pagamento["status"]
        }
        return info_pagamento
    except Exception as e:
        st.error(f"Erro ao conectar com Mercado Pago: {e}")
        return None

# Restante do código (verificar_pagamento_vrs, etc...)