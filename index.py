# =================================================================
# NOME DO SISTEMA: VRS Soluções
# MÓDULO: Arquivo Principal (index.py)
# =================================================================
import streamlit as st
import sys
import os

# Adiciona o diretório atual ao caminho do Python para garantir que os módulos sejam achados
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Importação dos módulos da VRS Soluções
# IMPORTANTE: O arquivo no GitHub deve se chamar exatamente 'anuncio.py' (sem acento)
try:
    import anuncio
    import pagamento
except ModuleNotFoundError as e:
    st.error(f"❌ Erro de Sistema: O arquivo '{e.name}' não foi encontrado no GitHub.")
    st.info("💡 Dica: Verifique se os arquivos 'anuncio.py' e 'pagamento.py' estão na pasta principal e sem acentos no nome.")
    st.stop()

# Configuração da Página: Nome da marca VRS Soluções no topo do navegador
st.set_page_config(
    page_title="VRS Soluções", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# Inicialização do Estado da Sessão para navegação entre telas
if "etapa" not in st.session_state:
    st.session_state.etapa = "vitrine"
if "plano_selecionado" not in st.session_state:
    st.session_state.plano_selecionado = None
if "dados_venda" not in st.session_state:
    st.session_state.dados_venda = {}

# --- MENU LATERAL (SIDEBAR) ---
with st.sidebar:
    st.markdown("<h2 style='color: #00FF7F;'>VRS Soluções</h2>", unsafe_allow_html=True)
    st.divider()
    
    # Botão para o usuário voltar ao início (Vitrine)
    if st.button("🏠 VOLTAR AO INÍCIO", use_container_width=True):
        st.session_state.etapa = "vitrine"
        st.rerun()
    
    # Informação de suporte técnico da marca
    st.markdown("""
        <div style='background: #111; padding: 15px; border-radius: 10px; border-left: 3px solid #00FF7F;'>
            <p style='color: #888; font-size: 0.8rem; margin: 0;'>SUPORTE TÉCNICO:</p>
            <p style='color: white; font-size: 0.85rem; word-wrap: break-word;'>vrsolucoes.sistemas@gmail.com</p>
        </div>
    """, unsafe_allow_html=True)

# --- SISTEMA DE GESTÃO DE TELAS (NAVEGAÇÃO) ---

# TELA 1: Vitrine Publicitária
if st.session_state.etapa == "vitrine":
    anuncio.exibir_vitrine_vrs()

# TELA 2: Formulário de Cadastro e Ativação
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
            
            # Botão que leva para o checkout do Mercado Pago
            if st.button("GERAR PIX PARA PAGAMENTO ⚡", use_container_width=True, type="primary"):
                if nome and email and id_maquina and telefone:
                    # Salva os dados para o processo de pagamento
                    st.session_state.dados_venda = {
                        "nome": nome, 
                        "email": email, 
                        "telefone": telefone, 
                        "id": id_maquina
                    }
                    st.session_state.etapa = "pagamento"
                    st.rerun()
                else:
                    st.error("⚠️ Por favor, preencha todos os campos obrigatórios!")

# TELA 3: Tela de Pagamento Final
elif st.session_state.etapa == "pagamento":
    pagamento.exibir_tela_pagamento(st.session_state.plano_selecionado, st.session_state.dados_venda)
    pagamento.exibir_suporte_footer()