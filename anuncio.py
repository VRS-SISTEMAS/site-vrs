# =================================================================
# NOME DO SISTEMA: VR SOLUÇÕES Sistemas
# MÓDULO: Vitrine Publicitária (anuncio.py)
# =================================================================
import streamlit as st

def exibir_vitrine_vrs():
    st.markdown("""
        <style>
        .titulo-vrs {
            text-align: center; color: white; 
            font-size: 4.5rem !important; font-weight: 900;
            margin-bottom: 0px; letter-spacing: -2px;
        }
        .subtitulo-vrs {
            text-align: center; color: #00c853; 
            font-size: 1.5rem; margin-bottom: 40px;
        }
        .container-apresentacao {
            background-color: #1a1a1a; padding: 30px;
            border-radius: 15px; border-left: 8px solid #00c853;
            margin-bottom: 50px; box-shadow: 10px 10px 30px rgba(0,0,0,0.5);
        }
        .card {
            background-color: #262626; padding: 25px; border-radius: 20px;
            border: 1px solid #444; text-align: center; min-height: 450px;
            transition: 0.4s;
        }
        .card:hover { border-color: #00c853; transform: scale(1.03); }
        .preco { color: #00c853; font-size: 2.5rem; font-weight: bold; margin: 15px 0; }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("<h1 class='titulo-vrs'>VRS Soluções</h1>", unsafe_allow_html=True)
    st.markdown("<p class='subtitulo-vrs'>Sistemas Inteligentes para Gestão Automotiva</p>", unsafe_allow_html=True)
    
    st.markdown("""
        <div class='container-apresentacao'>
            <h3 style='color: #00c853; margin-top:0;'>🛠️ O Ecossistema Definitivo para sua Oficina</h3>
            <p style='font-size: 1.2rem; color: #eee;'>
                A <b>VRS Soluções</b> não é apenas um software, é o motor da sua produtividade. 
                Nossa plataforma elimina o caos administrativo, centralizando <b>Painel de Frotas</b>, 
                <b>Histórico Técnico</b> e <b>Gestão de Peças</b> em um só lugar. 
                Ganhe tempo, segurança e o controle total que sua frota exige.
            </p>
        </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    planos = [
        {"nome": "BÁSICO", "preco": "99,99", "frota": "50 Veículos", "features": "✅ Oficina<br>✅ Cadastro<br>✅ Entradas", "key": "b_vrs", "val": "Básico (50 Veículos)"},
        {"nome": "JÚNIOR", "preco": "149,99", "frota": "100 Veículos", "features": "✅ Peças<br>✅ Relatórios<br>✅ Histórico", "key": "j_vrs", "val": "Júnior (100 Veículos)"},
        {"nome": "SÊNIOR", "preco": "299,99", "frota": "500 Veículos", "features": "✅ Painel Fleet<br>✅ Consultoria<br>✅ Suporte VIP", "key": "s_vrs", "val": "Sênior (500 Veículos)"}
    ]

    for i, p in enumerate([col1, col2, col3]):
        with p:
            item = planos[i]
            border = "border: 2px solid #00c853;" if item['nome'] == "JÚNIOR" else ""
            st.markdown(f"""
                <div class='card' style='{border}'>
                    <h2 style='margin-bottom:0;'>{item['nome']}</h2>
                    <p class='preco'>R$ {item['preco']}</p>
                    <p style='color: #aaa;'>{item['frota']}</p>
                    <hr style='border-color: #444;'>
                    <p style='text-align: left; font-size: 1.1rem;'>{item['features']}</p>
                </div>
            """, unsafe_allow_html=True)
            if st.button(f"ASSINAR {item['nome']}", key=item['key']):
                st.session_state.plano_selecionado = item['val']
                st.rerun()