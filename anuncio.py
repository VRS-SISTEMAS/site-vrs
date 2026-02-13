import streamlit as st

def exibir_vitrine_vrs():
    # CSS para forçar os cards a ficarem centralizados e limpos
    st.markdown("""
        <style>
        .titulo-vrs { text-align: center; color: #00FF7F; font-size: 3.5rem !important; font-weight: 900; }
        .card-vrs {
            background: #111111; border: 1px solid #333; border-radius: 20px;
            padding: 30px; text-align: center; min-height: 380px; margin-bottom: 20px;
        }
        .preco-vrs { color: #00FF7F; font-size: 2.5rem; font-weight: bold; }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("<h1 class='titulo-vrs'>VRS SOLUÇÕES</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #888;'>SISTEMAS DE GESTÃO AUTOMOTIVA</p>", unsafe_allow_html=True)
    st.divider()

    # Cards Lado a Lado - Isso vai substituir a bagunça que está na sua tela
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("<div class='card-vrs'><h2>BÁSICO</h2><p class='preco-vrs'>R$ 99,99</p><hr><p>✅ Oficina<br>✅ Cadastro</p></div>", unsafe_allow_html=True)
        if st.button("SELECIONAR BÁSICO", key="vrs_b"):
            st.session_state.plano_selecionado = "Básico (50 Veículos)"
            st.rerun()

    with col2:
        st.markdown("<div class='card-vrs' style='border-color: #00FF7F;'><h2>JÚNIOR</h2><p class='preco-vrs'>R$ 149,99</p><hr><p>✅ Peças<br>✅ Relatórios</p></div>", unsafe_allow_html=True)
        if st.button("SELECIONAR JÚNIOR", key="vrs_j"):
            st.session_state.plano_selecionado = "Júnior (100 Veículos)"
            st.rerun()

    with col3:
        st.markdown("<div class='card-vrs'><h2>SÊNIOR</h2><p class='preco-vrs'>R$ 299,99</p><hr><p>✅ Painel Fleet<br>✅ Suporte VIP</p></div>", unsafe_allow_html=True)
        if st.button("SELECIONAR SÊNIOR", key="vrs_s"):
            st.session_state.plano_selecionado = "Sênior (500 Veículos)"
            st.rerun()