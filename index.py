# =================================================================
# NOME DO SISTEMA: VRS Soluções
# MÓDULO: Arquivo Principal (index.py)
# OBJETIVO: Gestão de Navegação, Integração de Dados e Tutorial
# DESENVOLVEDOR: Iara & Vitor
# =================================================================
import streamlit as st
import importlib
import sys
import os
import requests 

# Força o Python a ler a pasta atual da VRS Soluções
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Função para carregar módulos com segurança e evitar erros de cache
def carregar_modulo(nome_modulo):
    try:
        module = importlib.import_module(nome_modulo)
        importlib.reload(module) 
        return module
    except Exception as e:
        return None

# Carregando módulos da VRS Soluções
anuncio = carregar_modulo("anuncio")
pagamento = carregar_modulo("pagamento")
backend = carregar_modulo("backend") 
bancodedados = carregar_modulo("bancodedados") 
tutorial = carregar_modulo("tutorial") 

# Inicializa o banco de dados automaticamente
if bancodedados:
    bancodedados.inicializar_banco()

# Configuração da Página VRS
st.set_page_config(page_title="VRS Soluções", layout="wide", initial_sidebar_state="collapsed")

# Inicialização da Sessão (Memória temporária do site)
if "etapa" not in st.session_state: st.session_state.etapa = "vitrine"
if "plano_selecionado" not in st.session_state: st.session_state.plano_selecionado = None
if "dados_venda" not in st.session_state: st.session_state.dados_venda = {}

# --- BARRA LATERAL (SIDEBAR) VRS ---
with st.sidebar:
    st.markdown("<p style='font-size: 10px; color: grey;'>VRS Soluções</p>", unsafe_allow_html=True)
    st.markdown("<h2 style='color: #00FF7F;'>Painel VRS</h2>", unsafe_allow_html=True)
    st.divider()
    
    # Botão de Início com KEY única
    if st.button("🏠 VOLTAR AO INÍCIO", use_container_width=True, key="btn_home_vrs"):
        st.session_state.etapa = "vitrine"
        st.rerun()

    # Botão de Tutorial com KEY única
    if st.button("📖 TUTORIAL DE INSTALAÇÃO", use_container_width=True, key="btn_tutorial_vrs"):
        st.session_state.etapa = "tutorial"
        st.rerun()

    st.sidebar.markdown("---")
    st.markdown("<p style='text-align: center; font-size: 14px;'>vrsolucoes.sistemas@gmail.com</p>", unsafe_allow_html=True)

# --- GESTÃO DE NAVEGAÇÃO (TELAS) ---

# TELA 1: Vitrine de Planos
if st.session_state.etapa == "vitrine":
    if anuncio:
        anuncio.exibir_vitrine_vrs()

# TELA 2: Formulário de Ativação
elif st.session_state.etapa == "ativacao":
    st.markdown(f"<h2 style='text-align: center; color: #00FF7F;'>💎 Dados de Ativação: Plano {st.session_state.plano_selecionado}</h2>", unsafe_allow_html=True)
    
    esq, centro, dir = st.columns([1, 2, 1])
    with centro:
        with st.container(border=True):
            # CAMPOS COM KEYS ÚNICAS PARA EVITAR CONFLITO
            nome = st.text_input("NOME COMPLETO / RAZÃO SOCIAL:", key="vrs_nome")
            email = st.text_input("E-MAIL:", key="vrs_email")
            telefone = st.text_input("WHATSAPP (DDD + NÚMERO):", key="vrs_tel")
            doc = st.text_input("CPF OU CNPJ:", key="vrs_doc")
            id_maquina = st.text_input("ID DA MÁQUINA (8 DÍGITOS):", max_chars=8, key="vrs_id_maq")
            
            if st.button("PROSSEGUIR PARA PAGAMENTO 💳", use_container_width=True, type="primary", key="vrs_btn_pagar"):
                if nome and email and telefone and doc and len(id_maquina) == 8:
                    dados_vrs = {
                        "nome": nome, "email": email, "telefone": telefone,
                        "documento": doc, "id": id_maquina, "plano": st.session_state.plano_selecionado
                    }
                    
                    if backend and backend.salvar_ativacao(dados_vrs):
                        try:
                            url_painel = "https://multidentate-presumingly-shauna.ngrok-free.dev/webhook"
                            requests.post(url_painel, json=dados_vrs, timeout=5)
                        except: pass
                        
                        st.session_state.dados_venda = dados_vrs
                        st.session_state.etapa = "pagamento"
                        st.rerun()
                    else:
                        st.error("Erro ao salvar dados no sistema VRS.")
                else:
                    st.warning("⚠️ Atenção: Preencha todos os campos e o ID de 8 dígitos!")

# TELA 3: Pagamento
elif st.session_state.etapa == "pagamento":
    if pagamento:
        pagamento.exibir_tela_pagamento(st.session_state.plano_selecionado, st.session_state.dados_venda)
        pagamento.exibir_suporte_footer()

# TELA 4: Tutorial
elif st.session_state.etapa == "tutorial":
    if tutorial:
        tutorial.exibir_tutorial_vrs()
    else:
        st.error("Módulo tutorial.py não encontrado.")