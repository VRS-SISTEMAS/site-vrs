# =================================================================
# NOME DO SISTEMA: VRS Soluções
# MÓDULO: Arquivo Principal (index.py)
# =================================================================
import streamlit as st
import importlib
import sys
import os
import requests # Necessário para enviar os dados para o Painel ADM

# Força o Python a ler a pasta atual da VRS Soluções para evitar erros de importação
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Função para carregar módulos com segurança e evitar o erro KeyError no Streamlit
def carregar_modulo(nome_modulo):
    try:
        module = importlib.import_module(nome_modulo)
        importlib.reload(module) # Força a atualização do cache para ler mudanças recentes
        return module
    except Exception as e:
        st.error(f"Erro ao carregar {nome_modulo}: {e}")
        return None

# Carregando os módulos necessários para o funcionamento do site
anuncio = carregar_modulo("anuncio")
pagamento = carregar_modulo("pagamento")
backend = carregar_modulo("backend") 

# Configuração da Página: Define o nome da marca na aba do navegador
st.set_page_config(page_title="VRS Soluções", layout="wide", initial_sidebar_state="collapsed")

# Verificação de segurança: O site só carrega se os arquivos vitais estiverem presentes
if anuncio is None or pagamento is None or backend is None:
    st.warning("⚠️ Atenção: Módulos críticos da VRS Soluções não foram detectados.")
    st.info("Verifique se 'anuncio.py', 'pagamento.py' e 'backend.py' estão no GitHub.")
    st.stop()

# Inicialização do Estado da Sessão (Memória do site durante a navegação)
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
    
    # Botão para o cliente resetar a navegação e voltar ao início
    if st.button("🏠 VOLTAR AO INÍCIO", use_container_width=True):
        st.session_state.etapa = "vitrine"
        st.rerun()
    
    # Informação unificada de suporte oficial
    st.markdown("""
        <div style='background: #111; padding: 15px; border-radius: 10px; border-left: 3px solid #00FF7F;'>
            <p style='color: #888; font-size: 0.8rem; margin: 0;'>SUPORTE TÉCNICO:</p>
            <p style='color: white; font-size: 0.85rem; word-wrap: break-word;'>vrsolucoes.sistemas@gmail.com</p>
        </div>
    """, unsafe_allow_html=True)

# --- GESTÃO DE TELAS (NAVEGAÇÃO DO USUÁRIO) ---

# TELA 1: Vitrine de Planos (anuncio.py)
if st.session_state.etapa == "vitrine":
    anuncio.exibir_vitrine_vrs()

# TELA 2: Formulário de Ativação (Captura de dados do cliente)
elif st.session_state.etapa == "ativacao":
    esq, centro, dir = st.columns([1, 2, 1])
    with centro:
        st.markdown(f"<h2 style='text-align: center; color: #00FF7F;'>💎 Ativação: {st.session_state.plano_selecionado}</h2>", unsafe_allow_html=True)
        with st.container(border=True):
            # Campos de entrada de dados
            nome = st.text_input("NOME COMPLETO / RAZÃO SOCIAL:")
            c1, c2 = st.columns(2)
            with c1: email = st.text_input("E-MAIL:")
            with c2: telefone = st.text_input("WHATSAPP:")
            c3, c4 = st.columns(2)
            with c3: doc = st.text_input("CPF OU CNPJ:")
            with c4: id_maquina = st.text_input("ID DA MÁQUINA:")
            
            # Botão de ação principal: Salva no banco e vai para o pagamento
            if st.button("GERAR PIX PARA PAGAMENTO ⚡", use_container_width=True, type="primary"):
                if nome and email and id_maquina and telefone:
                    # Organiza os dados em um dicionário para o backend e para o Painel ADM
                    dados_vrs = {
                        "nome": nome,
                        "email": email,
                        "telefone": telefone,
                        "documento": doc,
                        "id": id_maquina,
                        "plano": st.session_state.plano_selecionado
                    }
                    
                    # 1. SALVA NO BANCO DE DADOS LOCAL (backend.py)
                    if backend.salvar_ativacao(dados_vrs):
                        
                        # 2. TENTA ENVIAR PARA O PAINEL ADM (admin.py) VIA WEBHOOK
                        # Nota: Use o seu endereço de IP real ou o domínio do túnel se usar Ngrok
                        try:
                            requests.post("http://SEU_IP_OU_DOMINIO:5000/webhook", json=dados_vrs, timeout=3)
                        except:
                            pass # Silencia erro se o painel desktop estiver fechado

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