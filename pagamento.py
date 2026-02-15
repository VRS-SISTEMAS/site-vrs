# =================================================================
# NOME DO SISTEMA: VRS Soluções
# MÓDULO: Processamento de Pagamentos (pagamento.py)
# =================================================================
import streamlit as st
import mercadopago

def exibir_tela_pagamento(plano, dados_venda):
    """
    Gerencia a integração com Mercado Pago e a interface de checkout.
    """
    st.markdown(f"### 🚀 Ativando o Plano {plano}")
    st.write("Escolha sua forma de pagamento abaixo para concluir a assinatura.")

    # 1. Configuração de Segurança (Lendo do Streamlit Cloud Secrets)
    try:
        # Pega o token configurado no painel do Streamlit para evitar erros no GitHub
        sdk = mercadopago.SDK(st.secrets["ACCESS_TOKEN_MP"])
    except Exception:
        st.error("Erro técnico: Credenciais de pagamento não encontradas.")
        return

    # 2. Definição de Preços
    valores = {"Básico": 99.99, "Júnior": 149.99, "Sênior": 299.99}
    valor_final = valores.get(plano, 99.99)

    # 3. Configuração da Preferência do Mercado Pago
    preference_data = {
        "items": [
            {
                "title": f"Assinatura VRS Soluções - {plano}",
                "quantity": 1,
                "unit_price": valor_final,
            }
        ],
        "back_urls": {
            "success": "https://vr-solucoessistemas.streamlit.app/",
            "failure": "https://vr-solucoessistemas.streamlit.app/",
            "pending": "https://vr-solucoessistemas.streamlit.app/"
        },
        "auto_return": "approved",
    }

    # 4. Geração do Link de Pagamento
    if 'link_pagamento' not in st.session_state:
        with st.spinner("Conectando ao gateway seguro..."):
            result = sdk.preference().create(preference_data)
            if "init_point" in result["response"]:
                st.session_state.link_pagamento = result["response"]["init_point"]
            else:
                st.error("Falha ao gerar o link de pagamento. Contate o suporte.")
                return

    # 5. Interface Centralizada
    esq, centro, dir = st.columns([1, 2, 1])
    with centro:
        st.info("Clique no botão abaixo para pagar com Pix, Cartão ou Boleto.")
        st.link_button(
            "💳 CONCLUIR PAGAMENTO AGORA", 
            st.session_state.link_pagamento, 
            type="primary", 
            use_container_width=True
        )
        
        st.warning("Seu acesso será liberado assim que o pagamento for confirmado.")

        if st.button("Cancelar e Voltar", use_container_width=True):
            if 'link_pagamento' in st.session_state:
                del st.session_state.link_pagamento
            st.session_state.etapa = "vitrine"
            st.rerun()

def exibir_suporte_footer():
    """
    Rodapé padrão para todas as páginas de venda.
    """
    st.markdown("---")
    st.markdown(f"""
        <div style='text-align: center; color: #888;'>
            <p>Dúvidas? Suporte oficial <b>VRS Soluções</b>:</p>
            <p>📧 <b>vrsolucoes.sistemas@gmail.com</b></p>
        </div>
    """, unsafe_allow_html=True)