# =================================================================
# NOME DO SISTEMA: VRS Soluções
# MÓDULO: checkout.py (VITRINE DE ELITE REORGANIZADA)
# =================================================================
import streamlit as st
import botoes 
# Os outros imports (pagamento, cad_cliente, correio_vrs) devem estar na pasta

st.set_page_config(layout="wide", page_title="VRS Soluções - Ativação")
botoes.aplicar_estetica_vrs()

# --- HEADER IMPACTANTE ---
st.markdown("<h1 style='text-align:center; font-size:60px; letter-spacing:10px;'>VRS SOLUÇÕES</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#00FF7F; margin-top:-20px;'>SISTEMA DE GESTÃO ELITE</p>", unsafe_allow_html=True)

# --- PORTFÓLIO E DOWNLOAD NO TOPO ---
c1, c2 = st.columns([1, 1])
with c1:
    st.markdown("""
        <div style='background:#161a1d; padding:20px; border-radius:15px; border-left:5px solid #00FF7F;'>
            <h4 style='margin:0;'>📊 RECURSOS INCLUSOS</h4>
            <ul style='color:#ccc; font-size:14px;'>
                <li>Painel de Frotas Inteligente</li>
                <li>Gestão de Oficina e Peças</li>
                <li>Relatórios Técnicos em PDF</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)
with c2:
    botoes.download_instalador_vrs()

st.divider()

# --- ÁREA DE ATIVAÇÃO CENTRALIZADA ---
col_a, col_b, col_c = st.columns([1, 2, 1])
with col_b:
    st.markdown("### 💳 ATIVAÇÃO DE LICENÇA")
    plano = st.selectbox("Escolha seu plano de veículos:", 
        ["Básico (50 Veículos) - R$ 99,99", "Júnior (100 Veículos) - R$ 149,99", "Sênior (500 Veículos) - R$ 299,99"])
    
    nome = st.text_input("NOME COMPLETO / EMPRESA:")
    email = st.text_input("E-MAIL PARA CHAVE:")
    id_pc = st.text_input("ID DA MÁQUINA (VEJA NO INSTALADOR):")
    
    st.write("---")
    # Agora o botão só habilita com dados, mas avisa o que falta!
    botoes.exibir_navegacao_venda("FINALIZAR E PAGAR AGORA ✅", nome, email)

st.markdown("<p style='text-align:center; color:gray; margin-top:50px;'>VR SOLUÇÕES © 2026</p>", unsafe_allow_html=True)