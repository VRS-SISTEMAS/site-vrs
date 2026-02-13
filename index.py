# =================================================================
# NOME DO SISTEMA: VR SOLUÇÕES Sistemas
# MÓDULO: Arquivo Principal (index.py)
# =================================================================
import streamlit as st
import anuncio 
import pagamento
import botoes

st.set_page_config(page_title="VRS Soluções", layout="wide")

# Carrega o DNA Visual do botoes.py logo de cara
botoes.aplicar_estetica_vrs()

if "plano_selecionado" not in st.session_state:
    st.session_state.plano_selecionado = None

st.sidebar.markdown("<h2 style='color: #00FF7F;'>VRS Soluções</h2>", unsafe_allow_html=True)
opcao = st.sidebar.radio("Navegação:", ["Início", "Suporte"])

if opcao == "Início":
    if st.session_state.plano_selecionado is None:
        anuncio.exibir_vitrine_vrs()
    else:
        if st.button("⬅️ Voltar para Planos"):
            st.session_state.plano_selecionado = None
            st.rerun()
        
        c1, c2, c3 = st.columns([1, 2, 1])
        with c2:
            st.markdown(f"""
                <div style="background-color: #111111; padding: 25px; border-radius: 20px; border: 1px solid #00FF7F; text-align: center; margin-bottom: 20px;">
                    <h2 style="color: white; margin-bottom: 0;">Finalizar Assinatura</h2>
                    <p style="color: #00FF7F; font-size: 1.2rem; font-weight: bold;">Plano: {st.session_state.plano_selecionado}</p>
                </div>
            """, unsafe_allow_html=True)
            
            with st.container(border=True):
                nome = st.text_input("👤 Nome ou Razão Social:")
                email = st.text_input("📧 E-mail para Acesso:")
                id_pc = st.text_input("💻 ID da Máquina (veja no instalador):")
                st.divider()
                
                # Usa a lógica de pagamento do botoes.py integrada ao seu link
                botoes.exibir_navegacao_venda("ATIVAR VIA PIX AGORA", nome, email, id_pc)

elif opcao == "Suporte":
    st.markdown("<div class='card-vrs'><h3>📧 Suporte Técnico</h3><p>vrsolucoes.sistemas@gmail.com</p></div>", unsafe_allow_html=True)