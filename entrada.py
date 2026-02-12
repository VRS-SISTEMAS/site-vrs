import streamlit as st
import sys
import os
import botoes

# Garante a importação correta dos arquivos
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Tenta carregar o contador de visitas sem travar o site
try:
    import backend # type: ignore
    backend_ativo = True
except:
    backend_ativo = False

# 1. Configuração de Layout Elite
st.set_page_config(layout="wide", page_title="VRS Soluções - Ativação Elite")
botoes.aplicar_estetica_vrs()

if 'etapa' not in st.session_state:
    st.session_state['etapa'] = 0

# --- PÁGINA 1: VITRINE (CARDS DE IMPACTO IGUAL À IMAGEM) ---
if st.session_state['etapa'] == 0:
    st.markdown("<h1 style='text-align:center; font-size:55px; letter-spacing:10px;'>VRS SOLUÇÕES</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#888; margin-top:-20px;'>SISTEMAS DE GESTÃO AUTOMOTIVA ELITE</p>", unsafe_allow_html=True)
    
    st.write("##")
    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown('<div class="card-vrs"><div class="vrs-titulo">BÁSICO 🚀</div><div class="vrs-preco">R$ 99,99</div><div class="vrs-lista">✅ Gestão de Frota<br>✅ Até 50 Veículos<br>✅ Controle de Manutenção</div></div>', unsafe_allow_html=True)
        if st.button("ASSINAR BÁSICO", key="p1", use_container_width=True):
            st.session_state['plano'] = "Básico (50 Veículos)"
            st.session_state['etapa'] = 1
            st.rerun()

    with c2:
        st.markdown('<div class="card-vrs" style="border-color:#00FF7F;"><div class="vrs-titulo">JÚNIOR 🔥</div><div class="vrs-preco">R$ 139,99</div><div class="vrs-lista">✅ Até 100 Veículos<br>✅ Relatórios Técnicos PDF<br>✅ Histórico de Frota</div></div>', unsafe_allow_html=True)
        if st.button("ASSINAR JÚNIOR", key="p2", use_container_width=True):
            st.session_state['plano'] = "Júnior (100 Veículos)"
            st.session_state['etapa'] = 1
            st.rerun()

    with c3:
        st.markdown('<div class="card-vrs"><div class="vrs-titulo">SÊNIOR 💎</div><div class="vrs-preco">R$ 299,99</div><div class="vrs-lista">✅ Até 500 Veículos<br>✅ Gestão de Estoque<br>✅ Suporte Prioritário VIP</div></div>', unsafe_allow_html=True)
        if st.button("ASSINAR SÊNIOR", key="p3", use_container_width=True):
            st.session_state['plano'] = "Sênior (500 Veículos)"
            st.session_state['etapa'] = 1
            st.rerun()

# --- PÁGINA 2: CHECKOUT (CADASTRO E PAGAMENTO) ---
elif st.session_state['etapa'] == 1:
    st.markdown(f"### 💳 CHECKOUT: <span style='color:#00FF7F;'>{st.session_state.get('plano', '')}</span>", unsafe_allow_html=True)
    
    col_f, col_d = st.columns([2, 1])
    with col_f:
        tipo = st.radio("Cadastro:", ["CPF", "CNPJ"], horizontal=True)
        nome = st.text_input("NOME COMPLETO / EMPRESA:")
        doc = st.text_input(f"DIGITE SEU {tipo}:")
        email = st.text_input("E-MAIL PARA RECEBER A CHAVE:")
        id_pc = st.text_input("ID DA MÁQUINA (VEJA NO INSTALADOR):")
        
        st.write("---")
        botoes.exibir_navegacao_venda("CONFIRMAR PAGAMENTO 🚀", nome, email, id_pc)
        
        if st.button("⬅️ VOLTAR PARA PLANOS"):
            st.session_state['etapa'] = 0
            st.rerun()
    with col_d:
        botoes.download_instalador_vrs()

# --- PÁGINA 3: ESCRITÓRIO ADM ---
elif st.session_state['etapa'] == 3:
    st.markdown("## 👨‍💼 ESCRITÓRIO ADM")
    if backend_ativo:
        st.write(f"Visitas Totais: {backend.registrar_visita()}") # type: ignore
    if st.button("⬅️ SAIR DO ADM"):
        st.session_state['etapa'] = 0
        st.rerun()

# RODAPÉ
st.write("---")
botoes.exibir_acesso_secreto()