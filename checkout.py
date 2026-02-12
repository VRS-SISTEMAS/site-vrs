# =================================================================
# NOME DO SISTEMA: VR SOLUÇÕES Sistemas
# MÓDULO: checkout.py (VERSÃO COM PÁGINA DE VENDAS COMPLETA)
# =================================================================
import streamlit as st
import pagamento
import botoes 
import cad_cliente
import correio_vrs

# --- DESIGN E ESTILIZAÇÃO DE ELITE ---
st.set_page_config(page_title="VRS Soluções - Gestão de Elite", page_icon="🔧")

st.markdown("""
<style>
    .main-title { font-weight: 900; font-size: 50px !important; color: #00c853; text-align: center; margin-bottom: 0px; }
    .subtitle { text-align: center; color: #888; font-size: 18px; margin-bottom: 30px; }
    .feature-card {
        background: #161a1d;
        padding: 20px;
        border-radius: 15px;
        border-left: 5px solid #00c853;
        margin-bottom: 20px;
    }
    .price-card {
        text-align: center;
        background: #00c853;
        color: white;
        padding: 10px;
        border-radius: 10px;
        font-weight: bold;
        font-size: 20px;
    }
</style>
""", unsafe_allow_html=True)

# --- 1. CABEÇALHO IMPACTANTE ---
st.markdown('<p class="main-title">VRS SOLUÇÕES</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Sistemas Inteligentes para Gestão de Frotas e Oficinas</p>', unsafe_allow_html=True)

# --- 2. VITRINE DE PRODUTO (O que o cliente está comprando) ---
st.markdown("### 🚀 Transforme sua Oficina hoje")

col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    <div class="feature-card">
        <h4 style="color:white;">🛠️ Gestão de Ordens de Serviço</h4>
        <p style="color:#ccc;">Controle total desde a entrada até a entrega técnica com laudos profissionais.</p>
    </div>
    <div class="feature-card">
        <h4 style="color:white;">⏱️ Lógica Time Guide</h4>
        <p style="color:#ccc;">Saiba o tempo exato de cada manutenção e maximize o lucro por hora do seu técnico.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <h4 style="color:white;">📦 Controle de Estoque</h4>
        <p style="color:#ccc;">Nunca mais perca venda por falta de peça. Inventário inteligente e alertas de reposição.</p>
    </div>
    <div class="feature-card">
        <h4 style="color:white;">📊 Relatórios de Frota</h4>
        <p style="color:#ccc;">Histórico completo de cada veículo. Decisões baseadas em dados, não em palpites.</p>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# --- 3. ÁREA DE COMPRA ---
st.markdown("### 💳 Escolha seu Plano e Ative agora")

plano_escolhido = st.selectbox("Selecione o plano ideal para sua frota:", 
    ["Básico (50 Veículos) - R$ 99,99", "Júnior (100 Veículos) - R$ 149,99", "Sênior (500 Veículos) - R$ 299,99"])

# Limpa o nome do plano para o processamento
plano_nome_limpo = plano_escolhido.split(" - ")[0]

with st.container():
    st.markdown('<div style="background:#161a1d; padding:30px; border-radius:20px; border:1px solid #00c853;">', unsafe_allow_html=True)
    
    # IMPORTANTE: Garanta que o botoes.py tenha a função download_instalador_vrs()
    botoes.download_instalador_vrs()
    
    st.markdown("#### 👤 Passo 1: Seus Dados")
    nome_usuario = st.text_input("Nome Completo ou Razão Social")
    
    tipo_doc = st.radio("Documento Principal:", ["CPF", "CNPJ"], horizontal=True)
    documento = st.text_input(f"Digite seu {tipo_doc}")

    col_t, col_e = st.columns(2)
    with col_t:
        tel_usuario = st.text_input("WhatsApp com DDD")
    with col_e:
        email_usuario = st.text_input("E-mail para recebimento da Chave")
    
    st.markdown("#### 🔑 Passo 2: Identificação do PC")
    id_cliente = st.text_input("ID da Máquina (exibido no instalador)")

    st.divider()

    st.markdown("#### 💰 Passo 3: Pagamento")
    escolha = st.radio("Forma de pagamento:", 
                      ["Pix (Ativação Automática ⚡)", "Cartão / Boleto / Parcelado"], 
                      horizontal=True)

    if st.button("💎 FINALIZAR ATIVAÇÃO", use_container_width=True):
        if nome_usuario and email_usuario and id_cliente and documento:
            if cad_cliente.salvar_dados_vrs(nome_usuario, documento, tel_usuario, email_usuario, id_cliente, plano_nome_limpo):
                st.success("Cadastro realizado! Processando pagamento...")
                
                # Dispara e-mail
                correio_vrs.enviar_email_entrega(email_usuario, nome_usuario, id_cliente, plano_nome_limpo)

                # Pagamento
                if "Pix" in escolha:
                    info = pagamento.criar_pix_vrs(id_cliente, plano_nome_limpo, email_usuario)
                else:
                    info = pagamento.criar_checkout_pro_vrs(id_cliente, plano_nome_limpo, email_usuario)
                
                if info:
                    pagamento.exibir_tela_pagamento(info)
        else:
            st.warning("⚠️ CEO, preencha todos os campos para liberar o acesso!")

    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<p style='text-align: center; color: gray; margin-top: 30px;'>VR SOLUÇÕES - SISTEMAS © 2026</p>", unsafe_allow_html=True)