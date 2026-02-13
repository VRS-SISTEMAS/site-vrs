# =================================================================
# NOME DO SISTEMA: VR SOLUÇÕES Sistemas
# MÓDULO: Arquivo Principal (index.py)
# =================================================================
import streamlit as st
import anuncio 
import pagamento

st.set_page_config(page_title="VRS Soluções", layout="wide")

# Inicialização de memória para o VS Code não esquecer o link
if "plano_selecionado" not in st.session_state:
    st.session_state.plano_selecionado = None
if "link_ativo" not in st.session_state:
    st.session_state.link_ativo = None

st.sidebar.markdown("<h2 style='color: #00c853;'>VRS Soluções</h2>", unsafe_allow_html=True)
opcao = st.sidebar.radio("Navegação:", ["Início", "Suporte"])

if opcao == "Início":
    if st.session_state.plano_selecionado is None:
        anuncio.exibir_vitrine_vrs()
    else:
        # Botão de voltar limpa TUDO
        if st.button("⬅️ Voltar para Planos"):
            st.session_state.link_ativo = None
            st.session_state.plano_selecionado = None
            st.rerun()
        
        c1, c2, c3 = st.columns([1, 2, 1])
        with c2:
            # SÓ MOSTRA O FORMULÁRIO SE NÃO TIVER LINK GERADO
            if st.session_state.link_ativo is None:
                st.markdown(f"""
                    <div style="background-color: #1e1e1e; padding: 25px; border-radius: 15px; border-top: 5px solid #00c853; text-align: center; margin-bottom: 20px;">
                        <h2 style="color: white; margin-bottom: 5px;">Finalizar Assinatura</h2>
                        <h4 style="color: #00c853; margin-top: 0px;">{st.session_state.plano_selecionado}</h4>
                    </div>
                """, unsafe_allow_html=True)
                
                with st.container(border=True):
                    nome = st.text_input("👤 Nome Completo ou Razão Social:")
                    email = st.text_input("📧 E-mail para acesso:")
                    telefone = st.text_input("📞 Telefone (DDD + Número):")
                    tipo_doc = st.radio("Documento:", ["CPF", "CNPJ"], horizontal=True)
                    documento = st.text_input(f"Número do {tipo_doc}:")
                    
                    st.divider()
                    metodo = st.selectbox("Forma de Pagamento:", ["Pix (Liberação na Hora)", "Cartão de Crédito ou Boleto"])

                    if st.button("GERAR PAGAMENTO AGORA", use_container_width=True):
                        if nome and email and documento:
                            if "Pix" in metodo:
                                with st.spinner("Gerando Pix..."):
                                    dados = pagamento.criar_pix_vrs(st.session_state.plano_selecionado, email, nome, tipo_doc, documento, telefone)
                                    if dados:
                                        pagamento.exibir_tela_pagamento(dados)
                            else:
                                with st.spinner("Conectando ao Mercado Pago..."):
                                    # GERA E TRAVA NA MEMÓRIA
                                    link = pagamento.criar_checkout_pro_vrs(st.session_state.plano_selecionado, email, nome, tipo_doc, documento)
                                    if link:
                                        st.session_state.link_ativo = link
                                        st.rerun()
                        else:
                            st.error("⚠️ Preencha Nome, E-mail e Documento!")
            
            # SE O LINK JÁ EXISTE, MOSTRA APENAS O BOTÃO FINAL
            else:
                st.success("### ✅ Tudo pronto para o pagamento!")
                st.write(f"Plano: **{st.session_state.plano_selecionado}**")
                
                st.link_button("💳 CLIQUE AQUI PARA PAGAR (CARTÃO OU BOLETO)", 
                               st.session_state.link_ativo, 
                               use_container_width=True, 
                               type="primary")
                
                st.info("O Boleto estará disponível na página que abrirá.")
                if st.button("Corrigir dados / Gerar novo link"):
                    st.session_state.link_ativo = None
                    st.rerun()

elif opcao == "Suporte":
    st.markdown(f"### Suporte: vrsolucoes.sistemas@gmail.com")