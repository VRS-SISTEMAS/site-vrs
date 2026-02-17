# =================================================================
# NOME DO SISTEMA: VRS Soluções
# MÓDULO: Arquivo Principal (index.py)
# OBJETIVO: Gestão de Navegação e Integração de Dados
# =================================================================
import streamlit as st
import importlib
import sys
import os
import requests 

# Força o Python a ler a pasta atual
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def carregar_modulo(nome_modulo):
    try:
        module = importlib.import_module(nome_modulo)
        importlib.reload(module) 
        return module
    except Exception as e:
        st.error(f"Erro ao carregar {nome_modulo}: {e}")
        return None

# Carregando módulos da VRS Soluções
anuncio = carregar_modulo("anuncio")
pagamento = carregar_modulo("pagamento")
backend = carregar_modulo("backend") 
bancodedados = carregar_modulo("bancodedados") 

# Inicializa o banco de dados
if bancodedados:
    bancodedados.inicializar_banco()

st.set_page_config(page_title="VRS Soluções", layout="wide", initial_sidebar_state="collapsed")

# Inicialização da Sessão
if "etapa" not in st.session_state: st.session_state.etapa = "vitrine"
if "plano_selecionado" not in st.session_state: st.session_state.plano_selecionado = None
if "dados_venda" not in st.session_state: st.session_state.dados_venda = {}

# Sidebar VRS
with st.sidebar:
    st.markdown("<p style='font-size: 10px; color: grey;'>VRS Soluções</p>", unsafe_allow_html=True)
    st.markdown("<h2 style='color: #00FF7F;'>Painel VRS</h2>", unsafe_allow_html=True)
    if st.button("🏠 VOLTAR AO INÍCIO", use_container_width=True):
        st.session_state.etapa = "vitrine"
        st.rerun()
    st.sidebar.markdown("---")
    # E-mail oficial VRS Soluções
    st.markdown("<p style='text-align: center; font-size: 14px;'>vrsolucoes.sistemas@gmail.com</p>", unsafe_allow_html=True)

# --- NAVEGAÇÃO ---

if st.session_state.etapa == "vitrine":
    if anuncio:
        anuncio.exibir_vitrine_vrs()

elif st.session_state.etapa == "ativacao":
    st.markdown(f"<h2 style='text-align: center; color: #00FF7F;'>💎 Dados de Ativação: Plano {st.session_state.plano_selecionado}</h2>", unsafe_allow_html=True)
    
    esq, centro, dir = st.columns([1, 2, 1])
    with centro:
        with st.container(border=True):
            # CAMPOS OBRIGATÓRIOS DO VITOR - NOME, EMAIL, TELEFONE, CPF/CNPJ
            nome = st.text_input("NOME COMPLETO / RAZÃO SOCIAL:")
            email = st.text_input("E-MAIL:")
            telefone = st.text_input("WHATSAPP (DDD + NÚMERO):")
            doc = st.text_input("CPF OU CNPJ:")
            id_maquina = st.text_input("ID DA MÁQUINA (8 DÍGITOS):", max_chars=8)
            
            if st.button("PROSSEGUIR PARA PAGAMENTO 💳", use_container_width=True, type="primary"):
                # Validação rigorosa: Não prossegue se faltar informação
                if nome and email and telefone and doc and len(id_maquina) == 8:
                    dados_vrs = {
                        "nome": nome,
                        "email": email,
                        "telefone": telefone,
                        "documento": doc,
                        "id": id_maquina,
                        "plano": st.session_state.plano_selecionado
                    }
                    
                    # 1. Salva no Banco de Dados SQLite local (vrs_gestao.db)
                    if backend and backend.salvar_ativacao(dados_vrs):
                        # 2. Envia para o Painel ADM via Ngrok (Monitoramento em tempo real)
                        try:
                            url_painel = "https://multidentate-presumingly-shauna.ngrok-free.dev/webhook"
                            requests.post(url_painel, json=dados_vrs, timeout=5)
                        except: pass
                        
                        st.session_state.dados_venda = dados_vrs
                        st.session_state.etapa = "pagamento"
                        st.rerun()
                    else:
                        st.error("Erro ao salvar dados no banco VRS.")
                else:
                    st.warning("⚠️ Atenção: Preencha NOME, EMAIL, WHATSAPP, CPF/CNPJ e o ID de 8 dígitos!")

elif st.session_state.etapa == "pagamento":
    if pagamento:
        pagamento.exibir_tela_pagamento(st.session_state.plano_selecionado, st.session_state.dados_venda)
        pagamento.exibir_suporte_footer()