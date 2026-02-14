# =================================================================
# NOME DO SISTEMA: VRS Soluções
# MÓDULO: Processamento de Pagamentos (pagamento.py)
# =================================================================
import streamlit as st
import mercadopago

def exibir_tela_pagamento(plano, dados_venda):
    """
    Função que integra o Checkout Pro do Mercado Pago (Cartão, Boleto e Pix).
    """
    st.markdown(f"### 🚀 Ativando o Plano {plano}")
    st.write("Clique no botão abaixo para escolher sua forma de pagamento (Cartão, Boleto ou Pix).")

    # 1. Configuração do SDK do Mercado Pago
    try:
        sdk = mercadopago.SDK(st.secrets["ACCESS_TOKEN_MP"])
    except Exception as e:
        st.error("Erro ao carregar credenciais de pagamento. Verifique os Secrets.")
        return

    # 2. Definição dos valores conforme os planos da VRS Soluções
    valores = {
        "Básico": 99.99,
        "Júnior": 149.99,
        "Sênior": 299.99
    }
    valor_final = valores.get(plano, 99.99)

    # 3. Criação da Preferência de Pagamento (Checkout Pro)
    # Aqui configuramos o item, o preço e para onde o cliente volta depois.
    preference_data = {
        "items": [
            {
                "title": f"Assinatura Mensal - Plano {plano}",
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

    # 4. Execução da chamada à API e geração do Link de Pagamento
    if 'link_pagamento' not in st.session_state:
        with st.spinner("Preparando seu pagamento seguro..."):
            result = sdk.preference().create(preference_data)
            pagamento = result["response"]
            
            if "init_point" in pagamento:
                # O 'init_point' é o link oficial da tela de pagamento do Mercado Pago
                st.session_state.link_pagamento = pagamento["init_point"]
            else:
                st.error("Erro ao gerar a tela de pagamento. Tente novamente mais tarde.")
                return

    # 5. Interface de Pagamento Profissional
    st.info("Você será redirecionado para o ambiente seguro do Mercado Pago.")
    
    # Criamos um botão que abre o link de pagamento em uma nova aba
    st.link_button("💳 PAGAR AGORA (Cartão, Boleto ou Pix)", st.session_state.link_pagamento, type="primary", use_container_width=True)
    
    st.warning("O acesso será liberado imediatamente após a confirmação do pagamento.")

    if st.button("Voltar para a Vitrine"):
        # Limpa o estado para permitir novas tentativas
        if 'link_pagamento' in st.session_state:
            del st.session_state.link_pagamento
        st.session_state.etapa = "vitrine"
        st.rerun()

def exibir_suporte_footer():
    """
    Exibe informações de suporte ao final da página.
    """
    st.markdown("---")
    st.markdown(f"""
        <div style='text-align: center; color: #888;'>
            <p>Dúvidas na ativação? Entre em contato com o suporte oficial da <b>VR Soluções</b>:</p>
            <p>📧 <b>vrsolucoes.sistemas@gmail.com</b></p>
        </div>
    """, unsafe_allow_html=True)