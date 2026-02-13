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
        # Mostra APENAS a vitrine original
        anuncio.exibir_vitrine_vrs()
    else:
        if st.button("⬅️ Voltar para Planos"):
            st.session_state.plano_selecionado = None
            st.rerun()
        
        c1, c2, c3 = st.columns([1, 2, 1])
        with c2:
            st.markdown(f"""
                <div style="background-color: #1e1e1e; padding: 25px; border-radius: 15px; border-top: 5px solid #00c853; text-align: center;">
                    <h2 style="color: white; margin-bottom: 0;">Finalizar Assinatura</h2>
                    <p style="color: #00c853; font-size: 1.2rem;">Plano: {st.session_state.plano_selecionado}</p>
                </div>
            """, unsafe_allow_html=True)
            
            with st.container(border=True):
                nome = st.text_input("👤 Nome ou Razão Social:")
                email = st.text_input("📧 E-mail:")
                telefone = st.text_input("📞 Telefone:")
                tipo_doc = st.radio("Documento:", ["CPF", "CNPJ"], horizontal=True)
                doc = st.text_input(f"Número do {tipo_doc}:")
                id_maquina = st.text_input("💻 ID da Máquina (veja no instalador):")
                
                st.divider()
                if st.button("GERAR PIX AGORA", use_container_width=True):
                    if nome and email and doc and id_maquina:
                        dados = pagamento.criar_pix_vrs(st.session_state.plano_selecionado, email, nome, tipo_doc, doc, telefone)
                        if dados:
                            pagamento.exibir_tela_pagamento(dados)
                    else:
                        st.error("⚠️ Preencha todos os campos, incluindo o ID da Máquina!")

elif opcao == "Suporte":
    st.markdown("### 📧 Suporte: vrsolucoes.sistemas@gmail.com")