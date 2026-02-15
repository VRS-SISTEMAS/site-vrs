# =================================================================
# NOME DO SISTEMA: VRS Soluções
# MÓDULO: Arquivo Principal (index.py)
# =================================================================
import streamlit as st
import importlib
import sys
import os
import requests 

# --- NOVO: SISTEMA DE RASTREAMENTO VRS SOLUÇÕES ---
def rastrear_visitante(acao):
    """ Envia um sinal para o Painel ADM (Ngrok) informando entrada ou saída """
    try:
        # Link do seu Ngrok atualizado
        url_ngrok = "https://multidentate-presumingly-shauna.ngrok-free.dev/contador"
        headers = {"ngrok-skip-browser-warning": "true"}
        requests.post(url_ngrok, json={"acao": acao}, headers=headers, timeout=2)
    except:
        pass

# Dispara o rastreio assim que o site é carregado pela primeira vez na sessão
if 'visitante_rastreado' not in st.session_state:
    rastrear_visitante("entrada")
    st.session_state.visitante_rastreado = True
# --------------------------------------------------

# Força o Python a ler a pasta atual da VRS Soluções para evitar erros de importação
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Função para carregar módulos com segurança e evitar erros de cache
def carregar_modulo(nome_modulo):
    try:
        module = importlib.import_module(nome_modulo)
        importlib.reload(module) 
        return module
    except Exception as e:
        st.error(f"Erro ao carregar {nome_modulo}: {e}")
        return None

# Carregando os módulos necessários para a operação da VRS Soluções
anuncio = carregar_modulo("anuncio")
pagamento = carregar_modulo("pagamento")
backend = carregar_modulo("backend") 
bancodedados = carregar_modulo("bancodedados") 

# Inicialização automática do banco de dados para garantir que as tabelas existam
if bancodedados:
    bancodedados.inicializar_banco()

# Configuração da Página: Define o nome da marca VRS Soluções na aba do navegador
st.set_page_config(page_title="VRS Soluções", layout="wide", initial_sidebar_state="collapsed")

# Verificação de segurança: O site só carrega se os arquivos essenciais estiverem ativos
if anuncio is None or pagamento is None or backend is None:
    st.warning("⚠️ Atenção: Módulos críticos da VRS Soluções não foram detectados.")
    st.stop()

# Inicialização do Estado da Sessão (Memória temporária do site)
if "etapa" not in st.session_state:
    st.session_state.etapa = "vitrine"
if "plano_selecionado" not in st.session_state:
    st.session_state.plano_selecionado = None
if "dados_venda" not in st.session_state:
    st.session_state.dados_venda = {}

# --- BARRA LATERAL (SIDEBAR) ---
with st.sidebar:
    # Nome no cantinho conforme solicitado
    st.markdown("<p style='font-size: 10px; color: grey;'>VRS Soluções</p>", unsafe_allow_html=True)
    st.markdown("<h2 style='color: #00FF7F;'>Painel VRS</h2>", unsafe_allow_html=True)
    st.divider()
    if st.button("🏠 VOLTAR AO INÍCIO", use_container_width=True):
        st.session_state.etapa = "vitrine"
        st.rerun()

# --- GESTÃO DE TELAS E NAVEGAÇÃO ---

# TELA 1: Vitrine de Planos (anuncio.py)
if st.session_state.etapa == "vitrine":
    anuncio.exibir_vitrine_vrs()

# TELA 2: Formulário de Ativação (Captura de dados)
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
            
            # Botão principal: Inicia o processo de registro e pagamento
            if st.button("GERAR PIX PARA PAGAMENTO ⚡", use_container_width=True, type="primary"):
                if nome and email and id_maquina and telefone:
                    # Organiza os dados capturados
                    dados_vrs = {
                        "nome": nome,
                        "email": email,
                        "telefone": telefone,
                        "documento": doc,
                        "id": id_maquina,
                        "plano": st.session_state.plano_selecionado
                    }
                    
                    # 1. Salva no banco de dados do servidor
                    if backend.salvar_ativacao(dados_vrs):
                        
                        # 2. ENVIO EM TEMPO REAL PARA O PAINEL ADM (Via Ngrok)
                        try:
                            url_painel = "https://multidentate-presumingly-shauna.ngrok-free.dev/webhook"
                            headers = {"ngrok-skip-browser-warning": "true"}
                            requests.post(url_painel, json=dados_vrs, headers=headers, timeout=10)
                        except:
                            pass

                        st.session_state.dados_venda = dados_vrs
                        st.session_state.etapa = "pagamento"
                        st.rerun()
                    else:
                        st.error("❌ Erro ao registrar os dados no sistema VRS Soluções.")
                else:
                    st.error("⚠️ Preencha todos os campos obrigatórios!")

# TELA 3: Tela de Checkout (pagamento.py)
elif st.session_state.etapa == "pagamento":
    pagamento.exibir_tela_pagamento(st.session_state.plano_selecionado, st.session_state.dados_venda)
    pagamento.exibir_suporte_footer()