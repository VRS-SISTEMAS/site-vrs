# =================================================================
# NOME DO SISTEMA: VRS Soluções
# MÓDULO: Processamento de Pagamentos (pagamento.py)
# =================================================================
import streamlit as st
import mercadopago

def exibir_tela_pagamento(plano, dados_venda):
    """
    Função que integra o Checkout Pro do Mercado Pago e organiza o visual.
    """
    # Cabeçalho da página de pagamento
    st.markdown(f"### 🚀 Ativando o Plano {plano}")
    st.write("Escolha sua forma de pagamento abaixo para concluir a assinatura.")

    # 1. Configuração do SDK do Mercado Pago
    try:
        # O Token de acesso deve estar configurado nos 'Secrets' do Streamlit
        sdk = mercadopago.SDK(st.secrets["ACCESS_TOKEN_MP"])
    except Exception as e:
        st.error("Erro ao carregar credenciais de pagamento. Verifique os Secrets.")
        return

    # 2. Definição dos valores conforme os planos da VR Soluções
    valores = {
        "Básico": 99.99,
        "Júnior": 149.99,
        "Sênior": 299.99
    }
    valor_final = valores.get(plano, 99.99)

    # 3. Criação da Preferência de Pagamento (Checkout Pro)
    # Define o que o cliente está comprando e os links de retorno
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

    # 4. Comunicação com a API do Mercado Pago
    # Geramos o link apenas uma vez por sessão para evitar cobranças duplicadas
    if 'link_pagamento' not in st.session_state:
        with st.spinner("Preparando ambiente seguro..."):
            result = sdk.preference().create(preference_data)
            pagamento = result["response"]
            
            if "init_point" in pagamento:
                # Armazena o link oficial de checkout do Mercado Pago
                st.session_state.link_pagamento = pagamento["init_point"]
            else:
                st.error("Erro ao gerar o link. Tente novamente mais tarde.")
                return

    # 5. Interface de Pagamento com Visual Ajustado
    # Criamos 3 colunas para centralizar e diminuir o tamanho dos botões
    # A proporção [1, 2, 1] cria margens laterais e uma coluna central maior
    col_margem_esq, col_central, col_margem_dir = st.columns([1, 2, 1])

    with col_central:
        # Caixa de informação centralizada
        st.info("Você será levado ao ambiente seguro do Mercado Pago.")
        
        # Botão de pagamento com tamanho controlado pela coluna
        st.link_button(
            "💳 PAGAR AGORA (Cartão, Boleto ou Pix)", 
            st.session_state.link_pagamento, 
            type="primary", 
            use_container_width=True
        )
        
        # Alerta sobre a liberação do acesso
        st.warning("Acesso liberado após a confirmação.")

        # Botão para retornar à vitrine caso o usuário queira mudar de plano
        if st.button("Voltar para a Vitrine", use_container_width=True):
            if 'link_pagamento' in st.session_state:
                del st.session_state.link_pagamento
            st.session_state.etapa = "vitrine"
            st.rerun()

def exibir_suporte_footer():
    """
    Exibe informações de suporte da VRS Soluções no rodapé.
    """
    st.markdown("---")
    st.markdown(f"""
        <div style='text-align: center; color: #888;'>
            <p>Dúvidas na ativação? Entre em contato com o suporte oficial da <b>VRS Soluções</b>:</p>
            <p>📧 <b>vrsolucoes.sistemas@gmail.com</b></p>
        </div>
    """, unsafe_allow_html=True)