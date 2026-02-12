# =================================================================
# NOME DO SISTEMA: VRS Soluções
# MÓDULO: entrada.py (VERSÃO RESET - SEM ERROS DE CACHE)
# =================================================================
import streamlit as st
import sys
import os

# Limpa o caminho de importação para evitar erros de 'arquivos fantasmas'
if os.path.dirname(os.path.abspath(__file__)) not in sys.path:
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import botoes

# Tenta carregar o backend de forma blindada
try:
    import backend # type: ignore
    backend_ativo = True
except:
    backend_ativo = False

# 1. ESTÉTICA VRS ELITE]
st.set_page_config(layout="wide", page_title="VRS Soluções - Ativação Elite")
botoes.aplicar_estetica_vrs()

# 2. CONTROLE DE ETAPAS (Garante que comece do zero)
if 'etapa' not in st.session_state:
    st.session_state['etapa'] = 0

# --- PÁGINA 1: VITRINE (CARDS 3D) ---
if st.session_state['etapa'] == 0:
    st.markdown("<h1 style='text-align:center; font-size:55px;'>VRS <span style='color:#00FF7F;'>SOLUÇÕES</span></h1>", unsafe_allow_html=True)
    st.write("##")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<div class="card-vrs"><div class="vrs-titulo">BÁSICO 🚀</div><div class="vrs-preco">R$ 99,99</div><p>Até 50 Veículos</p></div>', unsafe_allow_html=True)
        if st.button("ASSINAR BÁSICO", key="b1", use_container_width=True):
            st.session_state['etapa'] = 1; st.rerun()
    with col2:
        st.markdown('<div class="card-vrs" style="border-color:#00FF7F;"><div class="vrs-titulo">JÚNIOR 🔥</div><div class="vrs-preco">R$ 139,99</div><p>Até 100 Veículos</p></div>', unsafe_allow_html=True)
        if st.button("ASSINAR JÚNIOR", key="b2", use_container_width=True):
            st.session_state['etapa'] = 1; st.rerun()
    with col3:
        st.markdown('<div class="card-vrs"><div class="vrs-titulo">SÊNIOR 💎</div><div class="vrs-preco">R$ 299,99</div><p>Até 500 Veículos</p></div>', unsafe_allow_html=True)
        if st.button("ASSINAR SÊNIOR", key="b3", use_container_width=True):
            st.session_state['etapa'] = 1; st.rerun()

# --- PÁGINA 2: CHECKOUT (PAGAMENTO) ---
elif st.session_state['etapa'] == 1:
    st.markdown("### 💳 FINALIZAR ATIVAÇÃO")
    col_f, col_d = st.columns([2, 1])
    with col_f:
        nome = st.text_input("NOME COMPLETO:"); doc = st.text_input("CPF/CNPJ:"); id_pc = st.text_input("ID DA MÁQUINA:")
        botoes.exibir_navegacao_venda("EFETUAR PAGAMENTO 🚀", nome, "vrs@email.com", id_pc)
        if st.button("⬅️ VOLTAR"):
            st.session_state['etapa'] = 0; st.rerun()
    with col_d:
        botoes.download_instalador_vrs()

# --- PÁGINA 3: ADM ---
elif st.session_state['etapa'] == 3:
    st.markdown("## 👨‍💼 ESCRITÓRIO ADM")
    if st.button("⬅️ SAIR"):
        st.session_state['etapa'] = 0; st.rerun()

st.write("---")
botoes.exibir_acesso_secreto()