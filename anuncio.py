# =================================================================
# NOME DO SISTEMA: VR SOLUÇÕES Sistemas
# MÓDULO: Vitrine Publicitária (anuncio.py)
# =================================================================
import streamlit as st

def exibir_vitrine_vrs():
    # Estilização para deixar os cards e o título perfeitos
    st.markdown("""
        <style>
        .titulo-vrs {
            text-align: center; color: white; 
            font-size: 4rem !important; font-weight: 850;
            margin-bottom: 5px; letter-spacing: -1px;
        }
        .subtitulo-vrs {
            text-align: center; color: #00c853; 
            font-size: 1.4rem; margin-bottom: 30px;
        }
        .container-apresentacao {
            background-color: #1e1e1e; padding: 30px;
            border-radius: 15px; border-left: 6px solid #00c853;
            margin-bottom: 40px; line-height: 1.6;
        }
        .card {
            background-color: #1e1e1e; padding: 30px; border-radius: 20px;
            border: 1px solid #333; text-align: center; min-height: 420px;
            transition: 0.3s;
        }
        .card:hover { 
            border-color: #00c853; 
            transform: translateY(-5px);
            box-shadow: 0px 10px 20px rgba(0,0,0,0.5); 
        }
        .preco { color: #00c853; font-size: 2.2rem; font-weight: bold; }
        .stButton>button {
            width: 100%; border-radius: 10px; height: 3.5em;
            background-color: #00c853; color: white; font-weight: bold; border: none;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("<h1 class='titulo-vrs'>VRS Soluções</h1>", unsafe_allow_html=True)
    st.markdown("<p class='subtitulo-vrs'>Sistemas Inteligentes para Gestão e Controle</p>", unsafe_allow_html=True)
    
    st.markdown("""
        <div class='container-apresentacao'>
            <h3 style='color: #00c853; margin-top: 0;'>🛠️ Transforme a gestão da sua oficina e frota</h3>
            <p style='font-size: 1.1rem; color: #ddd;'>
                A <b>VRS Soluções</b> centraliza tudo o que importa: desde o cadastro de veículos até relatórios técnicos complexos. 
                Ganhe <b>agilidade no atendimento</b> e <b>segurança nos dados</b> em tempo real.
            </p>
        </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("<div class='card'><h3>BÁSICO</h3><p class='preco'>R$ 99,99</p><p style='color: #888;'>Até 50 Veículos</p><hr style='border-color: #333;'><p style='text-align: left;'>✅ Oficina<br>✅ Cadastro<br>✅ Entradas</p></div>", unsafe_allow_html=True)
        if st.button("ASSINAR BÁSICO", key="b_vrs"):
            st.session_state.plano_selecionado = "Básico (50 Veículos)"
            st.rerun()

    with col2:
        st.markdown("<div class='card' style='border: 2px solid #00c853;'><h3 style='color: #00c853;'>JÚNIOR</h3><p class='preco'>R$ 149,99</p><p style='color: #888;'>Até 100 Veículos</p><hr style='border-color: #333;'><p style='text-align: left;'>✅ Peças<br>✅ Relatórios<br>✅ Histórico</p></div>", unsafe_allow_html=True)
        if st.button("ASSINAR JÚNIOR", key="j_vrs"):
            st.session_state.plano_selecionado = "Júnior (100 Veículos)"
            st.rerun()

    with col3:
        st.markdown("<div class='card'><h3>SÊNIOR</h3><p class='preco'>R$ 299,99</p><p style='color: #888;'>Até 500 Veículos</p><hr style='border-color: #333;'><p style='text-align: left;'>✅ Painel Fleet<br>✅ Consultoria<br>✅ Suporte VIP</p></div>", unsafe_allow_html=True)
        if st.button("ASSINAR SÊNIOR", key="s_vrs"):
            st.session_state.plano_selecionado = "Sênior (500 Veículos)"
            st.rerun()