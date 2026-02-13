# =================================================================
# NOME DO SISTEMA: VRS Soluções
# MÓDULO: Arquivo Principal (index.py)
# =================================================================
import streamlit as st
import anuncio
import pagamento

st.set_page_config(page_title="VRS Soluções", layout="wide", initial_sidebar_state="collapsed")

if "etapa" not in st.session_state:
    st.session_state.etapa = "vitrine"
if "plano_selecionado" not in st.session_state:
    st.session_state.plano_selecionado = None
if "dados_venda" not in st.session_state:
    st.session_state.dados_venda = {}

# --- BARRA LATERAL (SIDEBAR) COM SUPORTE ---
with st.sidebar:
    st.markdown("<h2 style='color: #00FF7F;'>VRS Soluções</h2>", unsafe_allow_html=True)
    st.divider()
    
    # Botão de Início e E-mail lado a lado
    if st.button("🏠 INÍCIO", use_container_width=True):
        st.session_state.etapa = "vitrine"
        st.rerun()
    
    st.markdown("""
        <div style='background: #111; padding: 15px; border-radius: 10px; border-left: 3px solid #00FF7F;'>
            <p style='color: #888; font-size: 0.8rem; margin: 0;'>SUPORTE TÉCNICO:</p>
            <p style='color: white; font-size: 0.85rem; word-wrap: break-word;'>vrsolucoes.sistemas@gmail.com</p>
        </div>
    """, unsafe_allow_html=True)

# --- GESTÃO DE TELAS ---
if st.session_state.etapa == "vitrine":
    anuncio.exibir_vitrine_vrs()

elif st.session_state.etapa == "ativacao":
    esq, centro, dir = st.columns([1, 2, 1])
    with centro:
        st.markdown(f"<h2 style='text-align: center; color: #00FF7F;'>💎 Ativação: {st.session_state.plano_selecionado}</h2>", unsafe_allow_html=True)
        with st.container(border=True):
            nome = st.text_input("NOME COMPLETO / RAZÃO SOCIAL:")
            c1, c2 = st.columns(2)
            with c1: email = st.text_input("E-MAIL:")
            with c2: telefone = st.text_input("WHATSAPP:")
            c3, c4 = st.columns(2)
            with c3: doc = st.text_input("CPF OU CNPJ:")
            with c4: id_maquina = st.text_input("ID DA MÁQUINA:")
            
            st.markdown("<br>", unsafe_allow_html=True)
            if st.button("GERAR PIX PARA PAGAMENTO ⚡", use_container_width=True, type="primary"):
                if nome and email and id_maquina and telefone:
                    st.session_state.dados_venda = {"nome": nome, "email": email, "telefone": telefone, "id": id_maquina}
                    st.session_state.etapa = "pagamento"
                    st.rerun()
                else:
                    st.error("⚠️ Preencha todos os campos!")

elif st.session_state.etapa == "pagamento":
    pagamento.exibir_tela_pagamento(st.session_state.plano_selecionado, st.session_state.dados_venda)
    pagamento.exibir_suporte_footer()