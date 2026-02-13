# =================================================================
# NOME DO SISTEMA: VRS Soluções
# MÓDULO: Vitrine Publicitária (anuncio.py)
# =================================================================
import streamlit as st

def exibir_vitrine_vrs():
    st.markdown("""
        <style>
        /* Estilos Globais de Luxo */
        .titulo-vrs { text-align: center; color: white; font-size: 3.8rem !important; font-weight: 900; letter-spacing: -1px; margin-bottom: 0px; }
        .subtitulo-vrs { text-align: center; color: #00FF7F; font-size: 1.2rem; font-weight: 300; letter-spacing: 3px; margin-bottom: 30px; text-transform: uppercase; }
        
        .container-nome-programa {
            background: rgba(0, 255, 127, 0.05);
            border: 1px solid rgba(0, 255, 127, 0.3);
            padding: 20px; border-radius: 15px; text-align: center; margin-bottom: 40px;
        }
        .nome-programa { color: #00FF7F; font-size: 2.2rem; font-weight: 800; margin: 0; text-shadow: 0 0 10px rgba(0, 255, 127, 0.5); }

        .card-plano {
            background: linear-gradient(180deg, #111111 0%, #0a0a0a 100%);
            border: 1px solid #222; padding: 30px; border-radius: 25px; 
            text-align: center; min-height: 480px; transition: 0.3s;
        }
        .card-plano:hover { border-color: #00FF7F; transform: translateY(-5px); }
        .card-popular { border: 2px solid #00FF7F !important; box-shadow: 0 0 20px rgba(0, 255, 127, 0.2); }
        
        .preco-vrs { color: #00FF7F; font-size: 2.5rem; font-weight: 800; margin: 10px 0; }
        .texto-suporte { color: #888; font-size: 1.1rem; margin-bottom: 20px; line-height: 1.2; }
        .lista-recursos { text-align: left; color: #ccc; font-size: 0.95rem; line-height: 2; margin-top: 20px; }
        .item-check { color: #00FF7F; font-weight: bold; margin-right: 10px; }

        /* Container de Benefícios Lux */
        .container-beneficios {
            background: #050505;
            padding: 40px; border-radius: 25px; margin-top: 60px;
            border: 1px solid #111; border-top: 4px solid #00FF7F;
        }
        .beneficio-item { color: #aaa; font-size: 1.1rem; margin-bottom: 15px; display: flex; align-items: center; }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("<h1 class='titulo-vrs'>VRS SOLUÇÕES</h1>", unsafe_allow_html=True)
    st.markdown("<p class='subtitulo-vrs'>Evolução Digital em Gestão</p>", unsafe_allow_html=True)

    st.markdown("""
        <div class='container-nome-programa'>
            <p style='color: #888; font-size: 0.9rem; margin-bottom: 5px;'>SOFTWARE EXCLUSIVO:</p>
            <h2 class='nome-programa'>GERENCIADOR PARA OFICINA</h2>
        </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    # --- PLANO BÁSICO ---
    with col1:
        st.markdown("""
            <div class='card-plano'>
                <h4 style='color: white; margin-bottom: 0;'>Plano Básico</h4>
                <div class='preco-vrs'>99.99</div>
                <div class='texto-suporte'>Com suporte para 50<br>Veículos</div>
                <hr style='border-color: #222;'>
                <div class='lista-recursos'>
                    <div><span class='item-check'>✔</span> Gestão de Peças & Estoque</div>
                    <div><span class='item-check'>✔</span> Relatórios Técnicos PDF</div>
                    <div><span class='item-check'>✔</span> Suporte VRS Chat</div>
                </div>
            </div>
        """, unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("ATIVAR BÁSICO 💎", key="b_vrs", use_container_width=True):
            st.session_state.plano_selecionado = "Básico"
            st.session_state.etapa = "ativacao"
            st.rerun()

    # --- PLANO JÚNIOR ---
    with col2:
        st.markdown("""
            <div class='card-plano card-popular'>
                <h4 style='color: #00FF7F; margin-bottom: 0;'>Plano Júnior</h4>
                <div class='preco-vrs'>149.99</div>
                <div class='texto-suporte'>Com suporte para 100<br>Veículos</div>
                <hr style='border-color: #222;'>
                <div class='lista-recursos'>
                    <div><span class='item-check'>✔</span> Gestão de Peças & Estoque</div>
                    <div><span class='item-check'>✔</span> Relatórios Técnicos PDF</div>
                    <div><span class='item-check'>✔</span> Suporte VRS Chat</div>
                </div>
            </div>
        """, unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("ATIVAR JÚNIOR 💎", key="j_vrs", use_container_width=True):
            st.session_state.plano_selecionado = "Júnior"
            st.session_state.etapa = "ativacao"
            st.rerun()

    # --- PLANO SÊNIOR ---
    with col3:
        st.markdown("""
            <div class='card-plano'>
                <h4 style='color: white; margin-bottom: 0;'>Plano Sênior</h4>
                <div class='preco-vrs'>299.99</div>
                <div class='texto-suporte'>Com suporte para 500<br>Veículos</div>
                <hr style='border-color: #222;'>
                <div class='lista-recursos'>
                    <div><span class='item-check'>✔</span> Gestão de Peças & Estoque</div>
                    <div><span class='item-check'>✔</span> Relatórios Técnicos PDF</div>
                    <div><span class='item-check'>✔</span> Suporte VRS Chat</div>
                </div>
            </div>
        """, unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("ATIVAR SÊNIOR 💎", key="s_vrs", use_container_width=True):
            st.session_state.plano_selecionado = "Sênior"
            st.session_state.etapa = "ativacao"
            st.rerun()

    # --- CONTAINER DE BENEFÍCIOS (O QUE TINHA SUMIDO) ---
    st.markdown("""
        <div class='container-beneficios'>
            <h2 style='color: white; margin-top: 0;'>🚀 Por que a VRS é a escolha da Elite?</h2>
            <div style='display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-top: 30px;'>
                <div class='beneficio-item'><span class='item-check'>✔</span> <b>Zero Papelada:</b> Digitalização total da sua oficina.</div>
                <div class='beneficio-item'><span class='item-check'>✔</span> <b>Histórico Instantâneo:</b> Tudo sobre o veículo em segundos.</div>
                <div class='beneficio-item'><span class='item-check'>✔</span> <b>Lucratividade:</b> Controle real de entradas e saídas.</div>
                <div class='beneficio-item'><span class='item-check'>✔</span> <b>Simplicidade:</b> Feito para quem foca no trabalho, não no PC.</div>
            </div>
        </div>
    """, unsafe_allow_html=True)