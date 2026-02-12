# =================================================================
# NOME DO SISTEMA: VR SOLUÇÕES Sistemas
# MARCA EXIBIDA: VRS Soluções
# MÓDULO: Gestão de Pagamentos Integrada (Pix, Boleto e Cartão)
# =================================================================

import mercadopago
import datetime 
import streamlit as st
import os  # Biblioteca para ler as chaves do sistema de forma segura
from dotenv import load_dotenv  # Carrega as chaves do arquivo .env

# --- CONFIGURAÇÃO DE SEGURANÇA DA VR SOLUÇÕES ---
# O comando abaixo carrega as chaves que você salvará no arquivo .env
load_dotenv()

# Buscamos o Token novo de forma protegida para evitar vazamentos no GitHub
ACCESS_TOKEN = os.getenv("MP_ACCESS_TOKEN")

# Inicialização do SDK do Mercado Pago
if ACCESS_TOKEN:
    sdk = mercadopago.SDK(ACCESS_TOKEN)
else:
    # Caso o token não seja encontrado, exibe um alerta no sistema
    st.error("⚠️ Erro de Configuração: Token do Mercado Pago não encontrado. Verifique o arquivo .env.")

def obter_valor_plano(plano_nome):
    """
    Retorna o valor correto baseado nos novos planos da VRS Soluções.
    """
    # ATUALIZAÇÃO DE VALORES - 11/02/2026
    # Mantendo os valores conforme o planejamento comercial da VR Soluções
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
        
        # Retorna os dados necessários para exibir o QR Code no site da VR Soluções
        return {
            "metodo": "pix",
            "copia_e_cola": pag["point_of_interaction"]["transaction_data"]["qr_code"],
            "qr_code_imagem": pag["point_of_interaction"]["transaction_data"]["qr_code_base64"]
        }
    except Exception as e:
        # Registro de erro para suporte técnico da VR Soluções
        st.error(f"Erro ao gerar Pix: {e}")
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
            # URLs de retorno do site da VR Soluções
            "success": "https://vrsolusoes.com.br/sucesso", 
            "failure": "https://vrsolusoes.com.br/erro",
            "pending": "https://vrsolusoes.com.br/pendente"
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
    Mantém a marca VRS Soluções visível e organizada.
    """
    if info["metodo"] == "pix":
        st.info("✅ Pix Gerado! Use o QR Code abaixo:")
        st.image(f"data:image/png;base64,{info['qr_code_imagem']}", width=250)
        st.code(info['copia_e_cola'])
        st.caption("A liberação ocorre em poucos segundos após o pagamento.")
    
    elif info["metodo"] == "cartao":
        st.info("✅ Checkout de Cartão/Boleto Pronto!")
        # Botão personalizado com as cores da VRS Soluções
        st.markdown(f'''
            <a href="{info["link_pagamento"]}" target="_blank" style="text-decoration:none;">
                <button style="width:100%; height:60px; background-color:#00c853; color:white; border-radius:15px; border:none; font-weight:bold; font-size:18px; cursor:pointer; box-shadow: 0px 4px 15px rgba(0,200,83,0.3);">
                    💳 PAGAR COM CARTÃO / OUTROS
                </button>
            </a>
        ''', unsafe_allow_html=True)
        st.write("*(Você será redirecionado para o ambiente seguro do Mercado Pago)*")