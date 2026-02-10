# =================================================================
# NOME DO SISTEMA: VR SOLUÇÕES Sistemas
# MÓDULO: checkout.py (Versão Final - Modularizada)
# =================================================================
import streamlit as st
import pagamento
import botoes # <--- Todas as funções visuais vêm daqui agora
import cad_cliente
import correio_vrs

# --- DESIGN ELITE E ESTILIZAÇÃO DO CABEÇALHO ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap');
    
    .block-container { max-width: 900px !important; padding-top: 2rem !important; }
    
    .brand-title {
        font-family: 'Inter', sans-serif;
        font-weight: 900;
        font-size: 42px !important;
        color: #00c853;
        text-align: center;
        letter-spacing: 2px;
        margin-bottom: 0px;
        text-transform: uppercase;
        text-shadow: 0px 0px 15px rgba(0, 200, 83, 0.4);
    }
    
    .brand-subtitle {
        font-size: 14px;
        color: gray;
        text-align: center;
        margin-top: -10px;
        margin-bottom: 40px;
    }

    .main-box {
        background: #161a1d;
        padding: 35px;
        border-radius: 20px;
        border: 1px solid #00c853;
        box-shadow: 0px 10px 30px rgba(0, 200, 83, 0.1);
    }

    /* Estilização do Botão de Download que está no botoes.py */
    div.stDownloadButton > button {
        background-color: #262626 !important;
        color: #00c853 !important;
        border: 1px solid #00c853 !important;
        font-weight: bold !important;
        width: 100% !important;
        height: 45px !important;
        border-radius: 10px !important;
    }
</style>
""", unsafe_allow_html=True)

# 1. Identidade e Cabeçalho
st.markdown('<p class="brand-title">VR SOLUÇÕES - SISTEMAS</p>', unsafe_allow_html=True)
st.markdown('<p class="brand-subtitle">Tecnologia de Elite para Gestão de Frotas</p>', unsafe_allow_html=True)

# 2. Vitrine de Benefícios
st.markdown("<h1 style='text-align: center;'>POR QUE OBTER <br><span style='color: #00c853;'>NOSSO PRODUTO?</span></h1>", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    <div style='background: #1c2127; padding: 25px; border-radius: 15px; border-left: 5px solid #00c853; height: 180px;'>
        <h4 style='color: white;'>Inclusão Digital de Sistema</h4>
        <p style='color: #ccc;'>✅ Gestão de frotas<br>✅ Controle de manutenção<br>✅ Controle de Estoque</p>
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown("""
    <div style='background: #1c2127; padding: 25px; border-radius: 15px; border-left: 5px solid #00c853; height: 180px;'>
        <h4 style='color: white;'>Comodidade e Fluidez</h4>
        <p style='color: #ccc;'>✅ Manutenção Correta<br>✅ Otimização de Tempo<br>✅ Relatório Detalhado</p>
    </div>
    """, unsafe_allow_html=True)

st.write("")
plano_escolhido = st.selectbox("Escolha seu plano para ativar:", ["Básico (30 Veículos)", "Júnior (50 Veículos)", "Sênior (200 Veículos)"])

st.divider()

# 3. Checkout e Download
with st.container():
    st.markdown('<div class="main-box">', unsafe_allow_html=True)
    
    # CHAMADA DO BOTÃO INTEGRADO NO BOTOES.PY
    botoes.download_instalador_vrs()

    st.markdown("<hr style='border: 0.5px solid #333'>", unsafe_allow_html=True)

    st.markdown("#### 👤 2. Seus Dados de Contato")
    nome_usuario = st.text_input("Nome Completo", placeholder="Ex: Vitor Ribeiro")
    
    col_t, col_e = st.columns(2)
    with col_t:
        tel_usuario = st.text_input("WhatsApp", placeholder="(00) 00000-0000")
    with col_e:
        email_usuario = st.text_input("E-mail Profissional", placeholder="exemplo@vrsolucoes.com")
    
    st.markdown("<br>#### 🔑 3. Chave de Ativação", unsafe_allow_html=True)
    id_cliente = st.text_input("ID do Computador", placeholder="Ex: PC-VRS-7788")
    
    st.write("")
    
    # Lógica de Finalização
    if st.button("⚡ GERAR PIX E ATIVAR AGORA", key="btn_gerar_pix"):
        if nome_usuario and tel_usuario and email_usuario and id_cliente:
            if cad_cliente.salvar_dados_vrs(nome_usuario, tel_usuario, email_usuario, id_cliente, plano_escolhido):
                st.success("Dados salvos! Gerando Pix...")
                
                # Envia e-mail automático
                correio_vrs.enviar_email_entrega(email_usuario, nome_usuario, id_cliente, plano_escolhido)
                
                # Gera o QR Code do Mercado Pago
                info = pagamento.criar_pix_vrs(id_cliente, plano_escolhido)
                if info:
                    pagamento.exibir_tela_pagamento(info)
        else:
            st.warning("⚠️ Preencha todos os campos para continuar.")

    st.markdown('</div>', unsafe_allow_html=True)

# Rodapé da marca
st.markdown("---")
st.markdown("<p style='text-align: center; font-size: 12px; color: #444;'>VR SOLUÇÕES - SISTEMAS © 2026 | Ambiente Criptografado 🛡️</p>", unsafe_allow_html=True)