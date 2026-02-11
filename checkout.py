# =================================================================
# NOME DO SISTEMA: VR SOLUÇÕES Sistemas
# MÓDULO: checkout.py (VERSÃO COM CPF/CNPJ DINÂMICO)
# =================================================================
import streamlit as st
import pagamento
import botoes 
import cad_cliente
import correio_vrs

# --- CABEÇALHO E ESTILO ---
st.markdown('<p style="font-weight:900; font-size:42px; color:#00c853; text-align:center;">VRS SOLUÇÕES</p>', unsafe_allow_html=True)

# 1. Escolha do Plano
plano_escolhido = st.selectbox("Selecione seu plano:", 
    ["Básico (50 Veículos)", "Júnior (100 Veículos)", "Sênior (500 Veículos)"])

# 2. Caixa Principal de Cadastro
with st.container():
    st.markdown('<div style="background:#161a1d; padding:30px; border-radius:20px; border:1px solid #00c853;">', unsafe_allow_html=True)
    
    botoes.download_instalador_vrs()
    
    st.markdown("#### 👤 1. Dados do Cliente")
    nome_usuario = st.text_input("Nome Completo ou Razão Social")
    
    # --- SELEÇÃO DE DOCUMENTO (A sacada que faltava) ---
    tipo_doc = st.radio("Tipo de Documento:", ["CPF", "CNPJ"], horizontal=True)
    if tipo_doc == "CPF":
        documento = st.text_input("Digite seu CPF", placeholder="000.000.000-00")
    else:
        documento = st.text_input("Digite seu CNPJ", placeholder="00.000.000/0000-00")

    col_t, col_e = st.columns(2)
    with col_t:
        tel_usuario = st.text_input("WhatsApp", placeholder="(00) 00000-0000")
    with col_e:
        email_usuario = st.text_input("E-mail para Chave de Ativação")
    
    st.divider()
    st.markdown("#### 🔑 2. Identificação do Dispositivo")
    id_cliente = st.text_input("ID do Computador (veja no instalador)")

    st.divider()

    # 3. Escolha da Forma de Pagamento
    st.markdown("#### 💰 3. Forma de Pagamento")
    escolha = st.radio("Como prefere pagar?", 
                      ["Pix (Ativação Instantânea ⚡)", "Cartão de Crédito / Boleto (Mercado Pago)"], 
                      horizontal=True)

    # 4. Ação Final
    if st.button("💎 FINALIZAR E PAGAR AGORA", use_container_width=True):
        if nome_usuario and email_usuario and id_cliente and documento:
            # Salva no banco de dados com o novo campo de documento
            if cad_cliente.salvar_dados_vrs(nome_usuario, documento, tel_usuario, email_usuario, id_cliente, plano_escolhido):
                st.success("Cadastro realizado!")
                
                # Dispara o e-mail
                correio_vrs.enviar_email_entrega(email_usuario, nome_usuario, id_cliente, plano_escolhido)

                # Gera o pagamento
                if "Pix" in escolha:
                    info = pagamento.criar_pix_vrs(id_cliente, plano_escolhido, email_usuario)
                else:
                    # Passamos o documento para o Mercado Pago também
                    info = pagamento.criar_checkout_pro_vrs(id_cliente, plano_escolhido, email_usuario)
                
                if info:
                    pagamento.exibir_tela_pagamento(info)
        else:
            st.warning("⚠️ Preencha todos os campos, incluindo o CPF/CNPJ.")

    st.markdown('</div>', unsafe_allow_html=True)