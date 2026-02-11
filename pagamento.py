# =================================================================
# NOME DO SISTEMA: VR SOLUÇÕES Sistemas
# MARCA EXIBIDA: VRS Soluções
# MÓDULO: Gestão de Pagamentos Integrada (Pix, Boleto e Cartão)
# =================================================================

import mercadopago
import datetime 
import streamlit as st

# --- CONFIGURAÇÃO DAS CHAVES DA VR SOLUÇÕES ---
ACCESS_TOKEN = "SEU_ACCESS_TOKEN_AQUI" 
sdk = mercadopago.SDK(ACCESS_TOKEN)

def obter_valor_plano(plano_nome):
    """
    Retorna o valor correto baseado nos novos planos da VRS Soluções.
    """
    # ATUALIZAÇÃO DE VALORES - 11/02/2026
    valores = {
        "Básico (50 Veículos)": 99.99,
        "Júnior (100 Veículos)": 149.99,
        "Sênior (500 Veículos)": 299.99
    }
    return valores.get(plano_nome, 99.99)

def criar_pix_vrs(id_maquina, plano_nome, email_cliente):
    """
    Gera um pagamento Pix personalizado para a VRS Soluções.
    """
    valor_final = obter_valor_plano(plano_nome)
    payment_data = {
        "transaction_amount": valor_final,
        "description": f"Assinatura {plano_nome} VRS Soluções - ID: {id_maquina}",
        "payment_method_id": "pix",
        "payer": {"email": email_cliente}
    }
    try:
        resultado = sdk.payment().create(payment_data)
        pag = resultado["response"]
        return {
            "metodo": "pix",
            "copia_e_cola": pag["point_of_interaction"]["transaction_data"]["qr_code"],
            "qr_code_imagem": pag["point_of_interaction"]["transaction_data"]["qr_code_base64"]
        }
    except Exception as e:
        st.error(f"Erro no Pix: {e}")
        return None

def criar_checkout_pro_vrs(id_maquina, plano_nome, email_cliente):
    """
    Gera um link de pagamento completo via Checkout Pro (Cartão/Boleto).
    """
    valor_final = obter_valor_plano(plano_nome)
    
    preference_data = {
        "items": [
            {
                "title": f"Ativação VRS Soluções - {plano_nome}",
                "quantity": 1,
                "unit_price": valor_final,
            }
        ],
        "payer": {"email": email_cliente},
        "external_reference": id_maquina,
        "back_urls": {
            "success": "https://sua-url-do-site.com", 
            "failure": "https://sua-url-do-site.com",
            "pending": "https://sua-url-do-site.com"
        },
        "auto_return": "approved"
    }

    try:
        preference_response = sdk.preference().create(preference_data)
        preference = preference_response["response"]
        return {
            "metodo": "cartao",
            "link_pagamento": preference["init_point"]
        }
    except Exception as e:
        st.error(f"Erro ao gerar checkout: {e}")
        return None

def exibir_tela_pagamento(info):
    """
    Renderiza a interface de pagamento conforme a escolha do cliente.
    """
    if info["metodo"] == "pix":
        st.info("✅ Pix Gerado! Use o QR Code abaixo:")
        st.image(f"data:image/png;base64,{info['qr_code_imagem']}", width=250)
        st.code(info['copia_e_cola'])
        st.caption("A liberação ocorre em poucos segundos após o pagamento.")
    
    elif info["metodo"] == "cartao":
        st.info("✅ Checkout de Cartão/Boleto Pronto!")
        st.markdown(f'''
            <a href="{info["link_pagamento"]}" target="_blank" style="text-decoration:none;">
                <button style="width:100%; height:60px; background-color:#00c853; color:white; border-radius:15px; border:none; font-weight:bold; font-size:18px; cursor:pointer; box-shadow: 0px 4px 15px rgba(0,200,83,0.3);">
                    💳 PAGAR COM CARTÃO / OUTROS
                </button>
            </a>
        ''', unsafe_allow_html=True)
        st.write("*(Você será redirecionado para o ambiente seguro do Mercado Pago)*")