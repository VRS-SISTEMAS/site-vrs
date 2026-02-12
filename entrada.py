import streamlit as st
import sys
import os
import botoes

# Força o Python a ignorar erros de pastas locais
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Configuração de Layout Elite
st.set_page_config(layout="wide", page_title="VRS Soluções - Ativação Elite")
botoes.aplicar_estetica_vrs()

if 'etapa' not in st.session_state:
    st.session_state['etapa'] = 0

# --- PÁGINA 1: VITRINE (CARDS DE IMPACTO) ---
if st.session_state['etapa'] == 0:
    st.markdown("<h1 style='text-align:center; font-size:50px;'>VRS <span style='color:#00FF7F;'>SOLUÇÕES</span></h1>", unsafe_allow_html=True)
    st.write("##")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<div class="card-vrs"><div class="vrs-titulo">BÁSICO 🚀</div><div class="vrs-preco">R$ 99,99</div><div class="vrs-desc">✅ Gestão de Frota<br>✅ Até 50 Veículos<br>✅ Controle de Manutenção</div></div>', unsafe_allow_html=True)
        if st.button("ASSINAR BÁSICO", key="b1", use_container_width=True):
            st.session_state['etapa'] = 1; st.rerun()
    with col2:
        st.markdown('<div class="card-vrs" style="border-color:#00FF7F;"><div class="vrs-titulo">JÚNIOR 🔥</div><div class="vrs-preco">R$ 139,99</div><div class="vrs-desc">✅ Até 100 Veículos<br>✅ Relatórios Técnicos PDF<br>✅ Histórico de Frota</div></div>', unsafe_allow_html=True)
        if st.button("ASSINAR JÚNIOR", key="b2", use_container_width=True):
            st.session_state['etapa'] = 1; st.rerun()
    with col3:
        st.markdown('<div class="card-vrs"><div class="vrs-titulo">SÊNIOR 💎</div><div class="vrs-preco">R$ 299,99</div><div class="vrs-desc">✅ Até 500 Veículos<br>✅ Gestão de Peças<br>✅ Suporte VIP</div></div>', unsafe_allow_html=True)
        if st.button("ASSINAR SÊNIOR", key="b3", use_container_width=True):
            st.session_state['etapa'] = 1; st.rerun()

# --- PÁGINA 2: CHECKOUT (PAGAMENTO) ---
elif st.session_state['etapa'] == 1:
    st.markdown("### 💳 FINALIZAR ATIVAÇÃO")
    col_f, col_d = st.columns([2, 1])
    with col_f:
        nome = st.text_input("NOME COMPLETO:"); doc = st.text_input("CPF/CNPJ:"); id_pc = st.text_input("ID DA MÁQUINA:")
        botoes.exibir_navegacao_venda("PAGAR AGORA 🚀", nome, "vrs@email.com", id_pc)
        if st.button("⬅️ VOLTAR"):
            st.session_state['etapa'] = 0; st.rerun()
    with col_d:
        botoes.download_instalador_vrs()

# --- PÁGINA 3: ADM ---
elif st.session_state['etapa'] == 3:
    st.markdown("## 👨‍💼 ESCRITÓRIO ADM")
    if st.button("⬅️ SAIR"):
        st.session_state['etapa'] = 0; st.rerun()

st.write("---")
botoes.exibir_acesso_secreto()