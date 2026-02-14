# =================================================================
# NOME DO SISTEMA: VRS Soluções
# MÓDULO: Processamento de Pagamentos (pagamento.py)
# =================================================================
import streamlit as st
import mercadopago
import time

def exibir_tela_pagamento(plano, dados_venda):
    """
    Função principal que integra com o Mercado Pago e exibe o Pix.
    """
    st.markdown(f"### 🚀 Ativando o Plano {plano}")
    st.write("Estamos gerando o seu código Pix para ativação imediata.")

    # 1. Configuração do SDK do Mercado Pago usando seu Secret Token
    # O token é puxado dos 'Secrets' do Streamlit para sua segurança.
    try:
        sdk = mercadopago.SDK(st.secrets["ACCESS_TOKEN_MP"])
    except Exception as e:
        st.error("Erro ao carregar credenciais de pagamento. Verifique os Secrets.")
        return

    # 2. Definição dos valores com base no plano selecionado
    # Valores conforme definidos na vitrine da VR Soluções.
    valores = {
        "Básico": 99.99,
        "Júnior": 149.99,
        "Sênior": 299.99
    }
    valor_final = valores.get(plano, 99.99)

    # 3. Criação da requisição de pagamento via Pix
    payment_data = {
        "transaction_amount": valor_final,
        "description": f"Assinatura VR Soluções - Plano {plano}",
        "payment_method_id": "pix",
        "payer": {
            "email": "vrsolucoes.sistemas@gmail.com", # Seu e-mail oficial
            "first_name": "Cliente",
            "last_name": "VRS"
        }
    }

    # 4. Execução da chamada à API
    if 'qr_code' not in st.session_state:
        with st.spinner("Comunicando com o Mercado Pago..."):
            result = sdk.payment().create(payment_data)
            pagamento = result["response"]
            
            if "point_of_interaction" in pagamento:
                st.session_state.qr_code = pagamento["point_of_interaction"]["transaction_data"]["qr_code"]
                st.session_state.qr_code_base64 = pagamento["point_of_interaction"]["transaction_data"]["qr_code_base64"]
            else:
                st.error("Erro ao gerar o Pix. Tente novamente mais tarde.")
                return

    # 5. Exibição da Interface de Pagamento
    col1, col2 = st.columns([1, 1])

    with col1:
        st.image(f"data:image/png;base64,{st.session_state.qr_code_base64}", caption="Aponte a câmera do celular")

    with col2:
        st.info("Copia e Cola")
        st.code(st.session_state.qr_code)
        st.warning("O acesso será liberado imediatamente após a confirmação do pagamento.")

    if st.button("Voltar para a Vitrine"):
        # Limpa o estado e volta para a seleção de planos
        del st.session_state.qr_code
        st.session_state.etapa = "vitrine"
        st.rerun()