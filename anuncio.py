# =================================================================
# NOME DO SISTEMA: VR SOLUÇÕES Sistemas
# MÓDULO: Vitrine Publicitária (anuncio.py)
# =================================================================
import streamlit as st

def exibir_vitrine_vrs():
    # Título imponente usando o estilo neon
    st.markdown("<h1 style='text-align: center; color: #00FF7F; font-size: 4rem; font-weight: 900; margin-bottom:0;'>VRS SOLUÇÕES</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #888; letter-spacing: 5px; margin-bottom: 50px;'>TECNOLOGIA ELITE PARA GESTÃO DE FROTAS</p>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)

    # Dados dos planos para evitar repetição de código
    planos = [
        {"nome": "BÁSICO", "preco": "99,99", "frota": "Até 50 Veículos", "lista": "✅ Oficina<br>✅ Cadastro<br>✅ Entradas", "key": "b_vrs", "label": "Básico (50 Veículos)"},
        {"nome": "JÚNIOR", "preco": "149,99", "frota": "Até 100 Veículos", "lista": "✅ Peças<br>✅ Relatórios<br>✅ Histórico", "key": "j_vrs", "label": "Júnior (100 Veículos)"},
        {"nome": "SÊNIOR", "preco": "299,99", "frota": "Até 500 Veículos", "lista": "✅ Painel Fleet<br>✅ Consultoria<br>✅ Suporte VIP", "key": "s_vrs", "label": "Sênior (500 Veículos)"}
    ]

    for i, col in enumerate([col1, col2, col3]):
        with col:
            p = planos[i]
            # Usando EXATAMENTE a classe card-vrs do botoes.py
            st.markdown(f"""
                <div class="card-vrs">
                    <div>
                        <div class="vrs-titulo">{p['nome']}</div>
                        <div class="vrs-preco">R$ {p['preco']}</div>
                        <p style="color: #666;">{p['frota']}</p>
                        <hr style="border-color: #222;">
                        <div class="vrs-lista">{p['lista']}</div>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            if st.button(f"SELECIONAR {p['nome']}", key=p['key'], use_container_width=True):
                st.session_state.plano_selecionado = p['label']
                st.rerun()