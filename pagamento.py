# =================================================================
# MÓDULO: Motor de Pagamentos (pagamento.py)
# =================================================================
import mercadopago
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()
sdk = mercadopago.SDK(os.getenv("MP_ACCESS_TOKEN"))

def obter_valor_plano(plano_nome):
    valores = {"Básico (50 Veículos)": 99.99, "Júnior (100 Veículos)": 149.99, "Sênior (500 Veículos)": 299.99}
    return valores.get(plano_nome, 99.99)

def criar_pix_vrs(plano_nome, email, nome, doc_tipo, doc_numero, telefone):
    payment_data = {
        "transaction_amount": obter_valor_plano(plano_nome),
        "description": f"Assinatura {plano_nome} - VRS Soluções",
        "payment_method_id": "pix",
        "payer": {
            "email": email,
            "first_name": nome,
            "identification": {"type": doc_tipo, "number": doc_numero},
            "phone": {"number": telefone}
        }
    }
    try:
        res = sdk.payment().create(payment_data)["response"]
        return {
            "metodo": "pix",
            "copia_e_cola": res["point_of_interaction"]["transaction_data"]["qr_code"],
            "qr_code_imagem": res["point_of_interaction"]["transaction_data"]["qr_code_base64"]
        }
    except: return None

def criar_checkout_pro_vrs(plano_nome, email, nome, doc_tipo, doc_numero):
    preference_data = {
        "items": [{"title": f"Assinatura {plano_nome}", "quantity": 1, "unit_price": obter_valor_plano(plano_nome)}],
        "payer": {"name": nome, "email": email, "identification": {"type": doc_tipo, "number": doc_numero}},
        "payment_methods": {"excluded_payment_types": [], "installments": 12},
        "auto_return": "approved"
    }
    try:
        res = sdk.preference().create(preference_data)["response"]
        return res["init_point"]
    except: return None

def exibir_tela_pagamento(info):
    st.success("✅ Pix Gerado!")
    c_qr, c_txt = st.columns([1, 1.2])
    with c_qr: st.image(f"data:image/png;base64,{info['qr_code_imagem']}", width=200)
    with c_txt:
        st.write("**Copia e Cola:**")
        st.code(info['copia_e_cola'])
        st.caption("Suporte: vrsolucoes.sistemas@gmail.com")