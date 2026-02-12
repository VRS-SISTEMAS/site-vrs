# =================================================================
# NOME DO SISTEMA: VRS Soluções
# MÓDULO: entrada.py (VITRINE COMPATÍVEL + NAVEGAÇÃO 3 ETAPAS)
# =================================================================
import streamlit as st
import botoes

# 1. Configuração de Layout Elite]
st.set_page_config(layout="wide", page_title="VRS Soluções - Ativação Elite", page_icon="⚡")
botoes.aplicar_estetica_vrs()

if 'etapa' not in st.session_state:
    st.session_state['etapa'] = 0

# --- PÁGINA 1: VITRINE (CARDS 3D + PORTFÓLIO COMPATÍVEL) ---
if st.session_state['etapa'] == 0:
    st.markdown("<h1 style='text-align:center;'>VRS <span style='color:#00FF7F;'>SOLUÇÕES</span></h1>", unsafe_allow_html=True)
    
    # 3 CARDS DE PLANOS (DESIGN DE IMPACTO)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<div class="card-vrs"><div class="vrs-titulo">BÁSICO</div><div class="vrs-preco">R$ 99,99</div><p>Até 50 Veículos</p></div>', unsafe_allow_html=True)
        if st.button("ASSINAR BÁSICO", key="b1", use_container_width=True):
            st.session_state.etapa = 1; st.rerun()
    with col2:
        st.markdown('<div class="card-vrs" style="border-color:#00FF7F;"><div class="vrs-titulo">JÚNIOR</div><div class="vrs-preco">R$ 139,99</div><p>Até 100 Veículos</p></div>', unsafe_allow_html=True)
        if st.button("ASSINAR JÚNIOR", key="b2", use_container_width=True):
            st.session_state.etapa = 1; st.rerun()
    with col3:
        st.markdown('<div class="card-vrs"><div class="vrs-titulo">SÊNIOR</div><div class="vrs-preco">R$ 299,99</div><p>Até 500 Veículos</p></div>', unsafe_allow_html=True)
        if st.button("ASSINAR SÊNIOR", key="b3", use_container_width=True):
            st.session_state.etapa = 1; st.rerun()

    st.write("---")
    
    # PORTFÓLIO COMPATÍVEL (REPRODUÇÃO GARANTIDA)]
    st.markdown("### 🖥️ PORTFÓLIO DO SISTEMA")
    tab1, tab2, tab3 = st.tabs(["📊 PAINEL DE FROTAS", "🔧 OFICINA", "📦 PEÇAS"])
    
    with tab1:
        # Usei um link de imagem de servidor externo para garantir que carregue para o cliente
        st.image("https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&q=80&w=800", 
                 caption="Interface VRS: Painel de Frotas Inteligente", use_container_width=True)
    with tab2:
        st.image("https://images.unsplash.com/photo-1504328332780-bc2907595925?auto=format&fit=crop&q=80&w=800", 
                 caption="Interface VRS: Gestão de Oficina e OS", use_container_width=True)
    with tab3:
        st.image("https://images.unsplash.com/photo-1586528116311-ad8dd3c8310d?auto=format&fit=crop&q=80&w=800", 
                 caption="Interface VRS: Cadastro de Peças e Estoque", use_container_width=True)

# --- PÁGINA 2: CHECKOUT (PAGAMENTO) ---
elif st.session_state['etapa'] == 1:
    st.markdown("## 💳 FINALIZAR PAGAMENTO")
    nome = st.text_input("NOME COMPLETO:"); email = st.text_input("E-MAIL:"); id_pc = st.text_input("ID DA MÁQUINA:")
    botoes.exibir_navegacao_venda("PAGAR AGORA 🚀", nome, email, id_pc)
    if st.button("⬅️ VOLTAR"): st.session_state.etapa = 0; st.rerun()

# --- PÁGINA 3: ADM ---
elif st.session_state['etapa'] == 3:
    st.markdown("## 👨‍💼 ESCRITÓRIO ADM"); botoes.exibir_acesso_secreto()