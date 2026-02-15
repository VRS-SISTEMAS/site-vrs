# =================================================================
# NOME DO SISTEMA: VRS Soluções
# MÓDULO: Arquivo Principal (index.py)
# =================================================================
import streamlit as st
import sys
import os

# Força o Python a olhar a pasta atual para evitar o KeyError
sys.path.append(os.path.dirname(__file__))

# Importação dos módulos da VR Soluções (Nomes sem acento)
try:
    import anuncio
    import pagamento
except ImportError as e:
    st.error(f"Erro ao carregar módulos: {e}. Certifique-se de que os nomes dos arquivos estão sem acento (anuncio.py).")

# Configuração da Página: Nome correto VRS Soluções no topo
st.set_page_config(page_title="VRS Soluções", layout="wide", initial_sidebar_state="collapsed")

# Inicialização do Estado da Sessão para persistência de dados
if "etapa" not in st.session_state:
    st.session_state.etapa = "vitrine"
if "plano_selecionado" not in st.session_state:
    st.session_state.plano_selecionado = None
if "dados_venda" not in st.session_state:
    st.session_state.dados_venda = {}

# --- BARRA LATERAL (SIDEBAR) ---
with st.sidebar:
    st.markdown("<h2 style='color: #00FF7F;'>VRS Soluções</h2>", unsafe_allow_html=True)
    st.divider()
    
    # Botão para resetar a navegação
    if st.button("🏠 VOLTAR AO INÍCIO", use_container_width=True):
        st.session_state.etapa = "vitrine"
        st.rerun()
    
    # Informação de suporte oficial unificada
    st.markdown("""
        <div style='background: #111; padding: 15px; border-radius: 10px; border-left: 3px solid #00FF7F;'>
            <p style='color: #888; font-size: 0.8rem; margin: 0;'>SUPORTE TÉCNICO:</p>
            <p style='color: white; font-size: 0.85rem; word-wrap: break-word;'>vrsolucoes.sistemas@gmail.com</p>
        </div>
    """, unsafe_allow_html=True)

# --- GESTÃO DE TELAS ---

# Tela 1: Vitrine de Planos
if st.session_state.etapa == "vitrine":
    anuncio.exibir_vitrine_vrs()

# Tela 2: Formulário de Cadastro/Ativação
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
                # Validação simples de campos
                if nome and email and id_maquina and telefone:
                    st.session_state.dados_venda = {"nome": nome, "email": email, "telefone": telefone, "id": id_maquina}
                    st.session_state.etapa = "pagamento"
                    st.rerun()
                else:
                    st.error("⚠️ Preencha todos os campos obrigatórios!")

# Tela 3: Checkout do Mercado Pago
elif st.session_state.etapa == "pagamento":
    pagamento.exibir_tela_pagamento(st.session_state.plano_selecionado, st.session_state.dados_venda)
    pagamento.exibir_suporte_footer()