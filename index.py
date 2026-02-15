# =================================================================
# NOME DO SISTEMA: VRS Soluções
# MÓDULO: Arquivo Principal (index.py)
# =================================================================
import streamlit as st
import importlib
import sys
import os
import requests 

# Força o Python a ler a pasta atual da VRS Soluções
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Função para carregar módulos com segurança
def carregar_modulo(nome_modulo):
    try:
        module = importlib.import_module(nome_modulo)
        importlib.reload(module) 
        return module
    except Exception as e:
        st.error(f"Erro ao carregar {nome_modulo}: {e}")
        return None

# Carregando os módulos necessários
anuncio = carregar_modulo("anuncio")
pagamento = carregar_modulo("pagamento")
backend = carregar_modulo("backend") 
bancodedados = carregar_modulo("bancodedados") # Módulo de criação da tabela

# --- NOVIDADE: INICIALIZAÇÃO AUTOMÁTICA DO BANCO ---
if bancodedados:
    bancodedados.inicializar_banco()

# Configuração da Página
st.set_page_config(page_title="VRS Soluções", layout="wide", initial_sidebar_state="collapsed")

# Verificação de segurança
if anuncio is None or pagamento is None or backend is None:
    st.warning("⚠️ Atenção: Módulos críticos da VRS Soluções não foram detectados.")
    st.stop()

# Inicialização do Estado da Sessão
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
    if st.button("🏠 VOLTAR AO INÍCIO", use_container_width=True):
        st.session_state.etapa = "vitrine"
        st.rerun()

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
            
            if st.button("GERAR PIX PARA PAGAMENTO ⚡", use_container_width=True, type="primary"):
                if nome and email and id_maquina and telefone:
                    dados_vrs = {
                        "nome": nome,
                        "email": email,
                        "telefone": telefone,
                        "documento": doc,
                        "id": id_maquina,
                        "plano": st.session_state.plano_selecionado
                    }
                    
                    # Tenta salvar no banco
                    if backend.salvar_ativacao(dados_vrs):
                        # Envia para o seu painel se ele estiver online
                        try:
                            requests.post("http://SEU_IP_AQUI:5000/webhook", json=dados_vrs, timeout=2)
                        except:
                            pass

                        st.session_state.dados_venda = dados_vrs
                        st.session_state.etapa = "pagamento"
                        st.rerun()
                    else:
                        st.error("❌ Erro ao registrar os dados no sistema VRS Soluções.")
                else:
                    st.error("⚠️ Preencha todos os campos obrigatórios!")

elif st.session_state.etapa == "pagamento":
    pagamento.exibir_tela_pagamento(st.session_state.plano_selecionado, st.session_state.dados_venda)
    pagamento.exibir_suporte_footer()