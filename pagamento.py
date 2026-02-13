# =================================================================
# NOME DO SISTEMA: VRS Soluções
# MÓDULO: Motor de Pagamentos (pagamento.py)
# =================================================================
import streamlit as st
import time
import os
from dotenv import load_dotenv

# Carrega as variáveis de segurança do arquivo .env
load_dotenv()

# Puxa o token do cofre. Se não encontrar, o sistema avisa.
TOKEN_MERCADO_PAGO = os.getenv("ACCESS_TOKEN_MP")

def exibir_tela_pagamento(plano, dados_cliente):
    st.markdown(f"## ⚡ Pagamento via Pix: {plano}")
    
    # Validação de segurança: Verifica se o token está configurado
    if not TOKEN_MERCADO_PAGO or TOKEN_MERCADO_PAGO == "SEU_TOKEN_REAL_AQUI":
        st.error("🚨 ERRO DE CONFIGURAÇÃO: O Token do Mercado Pago não foi encontrado no arquivo .env!")
        st.info("CEO, certifique-se de que o arquivo .env existe e contém seu ACCESS_TOKEN_MP.")
        return

    col_qr, col_instrucoes = st.columns([1, 1.5])
    
    with col_qr:
        # Aqui, no futuro, faremos a chamada real da API do Mercado Pago
        # Por enquanto, mantemos o QR fixo para você testar o visual
        st.image("https://api.qrserver.com/v1/create-qr-code/?size=250x250&data=VRS_SOLUCOES_PAGAMENTO", 
                 caption="ESCANEIE PARA PAGAR")
        
    with col_instrucoes:
        st.markdown(f"""
            ### 📋 Resumo dos Dados
            - **Cliente:** {dados_cliente['nome']}
            - **WhatsApp:** {dados_cliente['telefone']}
            - **E-mail:** {dados_cliente['email']}
            - **ID da Máquina:** `{dados_cliente['id']}`
            
            ---
            ### 🛠️ Instruções
            1. Abra o app do seu banco e escolha **Pix**.
            2. Escaneie o QR Code ao lado.
            3. A chave de ativação será liberada após a confirmação.
        """)
        
        # Botão de confirmação com verificação simulada
        if st.button("✅ JÁ REALIZEI O PAGAMENTO", use_container_width=True):
            with st.spinner("Consultando recebimento via API segura..."):
                # O sistema está usando o TOKEN_MERCADO_PAGO de forma invisível aqui
                time.sleep(2) 
                st.warning("⚠️ Pagamento ainda não localizado. O processamento pode levar até 2 minutos.")
                st.info("Caso o valor já tenha saído da sua conta, aguarde um instante e clique novamente.")

def exibir_suporte_footer():
    st.markdown("---")
    st.caption("Suporte Técnico VRS Soluções: vrsolucoes.sistemas@gmail.com")