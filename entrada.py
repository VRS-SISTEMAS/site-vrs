# =================================================================
# NOME DO SISTEMA: VRS Soluções
# MÓDULO: entrada.py (ESTRUTURA 3 PÁGINAS - DESIGN CARDS 3D)
# =================================================================
import streamlit as st
import sys
import os
import botoes

# Resolve erros de importação do Pylance]
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
try:
    import backend # type: ignore
    backend_ativo = True
except ImportError:
    backend_ativo = False

# 1. Configuração de Layout e Sessão]
st.set_page_config(layout="wide", page_title="VRS Soluções - Ativação Elite")
botoes.aplicar_estetica_vrs()

if 'etapa' not in st.session_state:
    st.session_state['etapa'] = 0

# --- PÁGINA 1: VITRINE (CARDS DE PLANOS) ---
if st.session_state['etapa'] == 0:
    st.markdown("<h1 style='text-align:center; font-size:50px;'>VRS <span style='color:#00FF7F;'>SOLUÇÕES</span></h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#888; margin-top:-20px;'>ESCOLHA SEU PLANO DE GESTÃO ELITE</p>", unsafe_allow_html=True)
    
    st.write("##")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown('<div class="card-vrs"><h3>BÁSICO 🚀</h3><div class="vrs-price">R$ 99,99</div><p>• Gestão de Frota<br>• Até 50 Veículos<br>• Suporte Standard</p></div>', unsafe_allow_html=True)
        if st.button("ASSINAR BÁSICO", key="b1", use_container_width=True):
            st.session_state['plano_vrs'] = "Básico (50 Veículos) - R$ 99,99"
            st.session_state['etapa'] = 1
            st.rerun()

    with col2:
        st.markdown('<div class="card-vrs" style="border-color:#00FF7F;"><h3>JÚNIOR 🔥</h3><div class="vrs-price">R$ 139,99</div><p>• Histórico Completo<br>• Até 100 Veículos<br>• Relatórios Premium</p></div>', unsafe_allow_html=True)
        if st.button("ASSINAR JÚNIOR", key="b2", use_container_width=True):
            st.session_state['plano_vrs'] = "Júnior (100 Veículos) - R$ 139,99"
            st.session_state['etapa'] = 1
            st.rerun()

    with col3:
        st.markdown('<div class="card-vrs"><h3>SÊNIOR 💎</h3><div class="vrs-price">R$ 299,99</div><p>• Estoque e Peças<br>• Até 500 Veículos<br>• Relatório em PDF</p></div>', unsafe_allow_html=True)
        if st.button("ASSINAR SÊNIOR", key="b3", use_container_width=True):
            st.session_state['plano_vrs'] = "Sênior (500 Veículos) - R$ 299,99"
            st.session_state['etapa'] = 1
            st.rerun()

# --- PÁGINA 2: CHECKOUT (CADASTRO E PAGAMENTO) ---
elif st.session_state['etapa'] == 1:
    st.markdown(f"### 💳 FINALIZAR ATIVAÇÃO: <span style='color:#00FF7F;'>{st.session_state.get('plano_vrs', '')}</span>", unsafe_allow_html=True)
    
    col_f, col_d = st.columns([2, 1])
    with col_f:
        tipo = st.radio("Cadastro:", ["CPF", "CNPJ"], horizontal=True)
        nome = st.text_input("NOME COMPLETO / EMPRESA:")
        doc = st.text_input(f"DIGITE O {tipo}:")
        email = st.text_input("E-MAIL PARA CHAVE:")
        id_pc = st.text_input("ID DA MÁQUINA (VEJA NO INSTALADOR):")
        
        st.write("---")
        # Botão de Pagamento Mercado Pago
        botoes.exibir_navegacao_venda("PAGAR E ATIVAR AGORA 🚀", nome, email, id_pc)
        
        if st.button("⬅️ VOLTAR PARA PLANOS"):
            st.session_state['etapa'] = 0
            st.rerun()
    with col_d:
        botoes.download_instalador_vrs()

# --- PÁGINA 3: ESCRITÓRIO ADM] ---
elif st.session_state['etapa'] == 3:
    st.markdown("## 👨‍💼 ESCRITÓRIO ADM VRS")
    if backend_ativo:
        st.success(f"Visitas Totais: {backend.registrar_visita()}") # type: ignore
    if st.button("⬅️ SAIR DO ESCRITÓRIO"):
        st.session_state['etapa'] = 0
        st.rerun()

# --- RODAPÉ ---
st.write("---")
botoes.exibir_acesso_secreto()