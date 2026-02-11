# =================================================================
# NOME DO SISTEMA: VR SOLUÇÕES Sistemas
# MÓDULO: entrada.py (Versão 3D Destravada)
# =================================================================
import streamlit as st
import botoes
import escritorio 
import os

# Configuração de página
st.set_page_config(layout="wide", initial_sidebar_state="collapsed")
botoes.aplicar_estetica_vrs()

# --- ESTILIZAÇÃO DE ELITE (CSS 3D FLIP COM DESTRAVE DE CLIQUE) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@700;900&display=swap');
    .stApp { background-color: #050a0e; }
    
    .vrs-logo-main {
        font-family: 'Orbitron', sans-serif;
        background: linear-gradient(180deg, #FFFFFF 0%, #A9A9A9 50%, #4F4F4F 100%);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        font-size: 72px; font-weight: 900; text-align: center;
        margin-top: -50px;
    }

    /* CONTAINER DO CARD 3D - Ajustado para não bloquear o botão */
    .flip-card {
        background-color: transparent;
        width: 100%;
        height: 380px; /* Reduzi um pouco para dar ar ao botão */
        perspective: 1000px;
        margin-bottom: 10px;
        position: relative;
        z-index: 1;
    }

    .flip-card-inner {
        position: relative;
        width: 100%;
        height: 100%;
        text-align: center;
        transition: transform 0.8s;
        transform-style: preserve-3d;
    }

    .flip-card:hover .flip-card-inner { transform: rotateY(180deg); }

    .flip-card-front, .flip-card-back {
        position: absolute;
        width: 100%;
        height: 100%;
        -webkit-backface-visibility: hidden;
        backface-visibility: hidden;
        border-radius: 20px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        padding: 30px;
        border: 1px solid rgba(0, 229, 255, 0.2);
    }

    .flip-card-front { background: rgba(16, 24, 32, 0.9); color: white; }

    .flip-card-back {
        background: linear-gradient(145deg, #0b1622, #101820);
        color: #00FF7F;
        transform: rotateY(180deg);
        border: 1px solid #00FF7F;
    }

    .list-features {
        text-align: left;
        font-size: 16px;
        line-height: 1.4;
        color: #FFFFFF;
        list-style-type: '⚡ ';
    }

    /* GARANTE QUE O BOTÃO FIQUE POR CIMA DE TUDO */
    .stButton {
        position: relative;
        z-index: 10 !important;
    }

    .checkout-box {
        background: rgba(16, 24, 32, 0.9);
        border: 1px solid rgba(0, 229, 255, 0.3);
        border-radius: 20px;
        padding: 50px;
        max-width: 800px;
        margin: 0 auto;
    }
</style>
""", unsafe_allow_html=True)

if 'etapa' not in st.session_state: st.session_state['etapa'] = 1

# --- ETAPA 1: VITRINE ---
if st.session_state['etapa'] == 1:
    st.markdown("<div class='vrs-logo-main'>VRS SOLUÇÕES</div>", unsafe_allow_html=True)
    st.markdown("<p style='color:#00e5ff; text-align:center; letter-spacing:8px;'>SISTEMAS ELITE</p>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    planos_info = {
        "BÁSICO": {"preco": "99,99", "info": ["Gestão de controle frota", "Cadastro para 30 veículos", "Serviço inteligente"]},
        "JÚNIOR 🚀": {"preco": "139,99", "info": ["Cadastro para 30 veículos", "Gestão de oficina", "Histórico de manutenção"]},
        "SÊNIOR 💎": {"preco": "299,99", "info": ["Cadastro até 500 veículos", "Controle de estoque", "Relatórios técnicos em PDF"]}
    }
    
    cols = [col1, col2, col3]
    for i, (nome, dados) in enumerate(planos_info.items()):
        with cols[i]:
            beneficios_html = "".join([f"<li>{item}</li>" for item in dados["info"]])
            st.markdown(f"""
            <div class="flip-card">
                <div class="flip-card-inner">
                    <div class="flip-card-front">
                        <h2 style='font-family:Orbitron;'>{nome}</h2>
                        <h1 style='color:#00FF7F; font-family:Orbitron;'>R$ {dados['preco']}</h1>
                        <p style='color:#00e5ff; font-size:12px;'>TOQUE/MOUSE PARA DETALHES</p>
                    </div>
                    <div class="flip-card-back">
                        <h3 style='font-family:Orbitron; color:#00FF7F; font-size:18px;'>FUNCIONALIDADES</h3>
                        <ul class="list-features">{beneficios_html}</ul>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            # Botão de Assinatura com chave única para evitar conflitos
            if st.button(f"ASSINAR {nome.split()[0]}", key=f"btn_vrs_final_{i}"):
                st.session_state['plano'] = nome
                st.session_state['etapa'] = 2
                st.rerun()

    st.write("---")
    if st.button("🔐 ACESSO ADMINISTRATIVO"):
        st.session_state['etapa'] = 3
        st.rerun()

elif st.session_state['etapa'] == 2:
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("<div class='checkout-box'>", unsafe_allow_html=True)
    st.markdown(f"<h2 style='font-family:Orbitron; color:#00e5ff; text-align:center;'>💳 CHECKOUT: {st.session_state.get('plano')}</h2>", unsafe_allow_html=True)
    nome_input = st.text_input("NOME COMPLETO DO TITULAR:")
    email_input = st.text_input("E-MAIL PARA RECEBIMENTO:")
    st.write("---")
    botoes.exibir_navegacao_venda("PAGAR AGORA ✅", nome_cli=nome_input, email_cli=email_input)
    st.markdown("</div>", unsafe_allow_html=True)

elif st.session_state['etapa'] == 3:
    escritorio.exibir_painel_vitor()