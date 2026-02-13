# =================================================================
# NOME DO SISTEMA: VR SOLUÇÕES Sistemas
# MÓDULO: Arquivo Principal (index.py)
# =================================================================
import streamlit as st
import anuncio 
import pagamento

st.set_page_config(page_title="VRS Soluções", layout="wide")

if "plano_selecionado" not in st.session_state:
    st.session_state.plano_selecionado = None

st.sidebar.markdown("<h2 style='color: #00c853;'>VRS Soluções</h2>", unsafe_allow_html=True)
opcao = st.sidebar.radio("Navegação:", ["Início", "Suporte"])

if opcao == "Início":
    if st.session_state.plano_selecionado is None:
        # EXIBE APENAS A VITRINE LIMPA
        anuncio.exibir_vitrine_vrs()
    else:
        if st.button("⬅️ Voltar para Planos"):
            st.session_state.plano_selecionado = None
            st.rerun()
        
        c1, c2, c3 = st.columns([1, 2, 1])
        with c2:
            st.markdown(f"### Ativação: {st.session_state.plano_selecionado}")
            with st.container(border=True):
                nome = st.text_input("NOME COMPLETO OU RAZÃO SOCIAL:")
                email = st.text_input("E-MAIL PARA ENVIO DA CHAVE:")
                id_pc = st.text_input("ID DA MÁQUINA (VEJA NO INSTALADOR):")
                st.divider()
                if st.button("GERAR PIX PARA ATIVAÇÃO", use_container_width=True):
                    if nome and email and id_pc:
                        dados = pagamento.criar_pix_vrs(st.session_state.plano_selecionado, email, nome, "CPF", "000", "00")
                        if dados: pagamento.exibir_tela_pagamento(dados)
                    else:
                        st.error("Preencha todos os campos!")

elif opcao == "Suporte":
    st.markdown("### Suporte: vrsolucoes.sistemas@gmail.com")