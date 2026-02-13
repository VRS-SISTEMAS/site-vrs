# =================================================================
# NOME DO SISTEMA: VR SOLUÇÕES Sistemas
# MÓDULO: Vitrine Publicitária (anuncio.py)
# =================================================================
import streamlit as st

def exibir_vitrine_vrs():
    # Estilização Profissional
    st.markdown("""
        <style>
        .titulo-vrs { text-align: center; color: white; font-size: 3.5rem !important; font-weight: 850; margin-bottom: 5px; }
        .subtitulo-vrs { text-align: center; color: #00c853; font-size: 1.3rem; margin-bottom: 30px; }
        .card { background-color: #1e1e1e; padding: 25px; border-radius: 20px; border: 1px solid #333; text-align: center; min-height: 400px; transition: 0.3s; }
        .card:hover { border-color: #00c853; transform: translateY(-5px); box-shadow: 0px 10px 20px rgba(0,0,0,0.5); }
        .preco { color: #00c853; font-size: 2.2rem; font-weight: bold; }
        .stButton>button { width: 100%; border-radius: 10px; height: 3.5em; background-color: #00c853; color: white; font-weight: bold; border: none; }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("<h1 class='titulo-vrs'>VRS Soluções</h1>", unsafe_allow_html=True)
    st.markdown("<p class='subtitulo-vrs'>Tecnologia de Ponta para Gestão de Frotas</p>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("<div class='card'><h3>BÁSICO</h3><p class='preco'>R$ 99,99</p><p style='color: #888;'>Até 50 Veículos</p><hr style='border-color: #333;'><p style='text-align: left;'>✅ Oficina<br>✅ Cadastro</p></div>", unsafe_allow_html=True)
        if st.button("ASSINAR BÁSICO", key="btn_basico"):
            st.session_state.plano_selecionado = "Básico (50 Veículos)"
            st.rerun()

    with col2:
        st.markdown("<div class='card' style='border: 2px solid #00c853;'><h3 style='color: #00c853;'>JÚNIOR</h3><p class='preco'>R$ 149,99</p><p style='color: #888;'>Até 100 Veículos</p><hr style='border-color: #333;'><p style='text-align: left;'>✅ Peças<br>✅ Relatórios</p></div>", unsafe_allow_html=True)
        if st.button("ASSINAR JÚNIOR", key="btn_junior"):
            st.session_state.plano_selecionado = "Júnior (100 Veículos)"
            st.rerun()

    with col3:
        st.markdown("<div class='card'><h3>SÊNIOR</h3><p class='preco'>R$ 299,99</p><p style='color: #888;'>Até 500 Veículos</p><hr style='border-color: #333;'><p style='text-align: left;'>✅ Painel Total<br>✅ Consultoria</p></div>", unsafe_allow_html=True)
        if st.button("ASSINAR SÊNIOR", key="btn_senior"):
            st.session_state.plano_selecionado = "Sênior (500 Veículos)"
            st.rerun()