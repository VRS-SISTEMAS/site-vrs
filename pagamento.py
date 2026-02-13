# =================================================================
# NOME DO SISTEMA: VRS Soluções
# MÓDULO: Motor de Pagamentos Real (pagamento.py)
# =================================================================
import streamlit as st
import mercadopago
import os
from dotenv import load_dotenv

# Carrega o .env primeiro para garantir que o local funcione
load_dotenv()

# Tenta carregar o token sem deixar o Streamlit travar o site
TOKEN_MP = os.getenv("ACCESS_TOKEN_MP") # Primeiro tenta o .env (Local)

if not TOKEN_MP:
    try:
        # Se estiver no site (Nuvem), tenta pegar dos Secrets
        if "ACCESS_TOKEN_MP" in st.secrets:
            TOKEN_MP = st.secrets["ACCESS_TOKEN_MP"]
    except Exception:
        # Se der erro de segredo não encontrado, mantém como None
        TOKEN_MP = None

def criar_pagamento_pix(plano, dados_cliente):
    # Define o valor baseado no plano selecionado
    valores = {"Básico": 99.99, "Júnior": 149.99, "Sênior": 299.99}
    valor = valores.get(plano, 99.99)

    sdk = mercadopago.SDK(TOKEN_MP)
    
    payment_data = {
        "transaction_amount": valor,
        "description": f"Plano {plano} - VRS Soluções",
        "payment_method_id": "pix",
        "payer": {
            "email": dados_cliente['email'],
            "first_name": dados_cliente['nome'],
        }
    }

    result = sdk.payment().create(payment_data)
    return result["response"]

def exibir_tela_pagamento(plano, dados_cliente):
    st.markdown(f"## ⚡ Finalizar Ativação: {plano}")
    
    # Se depois de todas as tentativas o token ainda for nulo
    if not TOKEN_MP:
        st.error("🚨 Erro de Configuração: O Token de acesso não foi encontrado.")
        st.info("Verifique se o seu arquivo .env no PC ou os 'Secrets' no site estão configurados.")
        return

    # Gera o pagamento real na API do Mercado Pago
    with st.spinner("Gerando seu Pix de ativação..."):
        try:
            pagamento = criar_pagamento_pix(plano, dados_cliente)
            
            # Pega os dados do Pix gerado pela API
            transaction_data = pagamento.get('point_of_interaction', {}).get('transaction_data', {})
            qr_code_base64 = transaction_data.get('qr_code_base64')
            pix_copia_cola = transaction_data.get('qr_code')
            
            if qr_code_base64:
                col_qr, col_dados = st.columns([1, 1.2])
                
                with col_qr:
                    st.image(f"data:image/png;base64,{qr_code_base64}", caption="Aponte a câmera do banco")
                    st.success(f"Valor: R$ {pagamento.get('transaction_amount'):.2f}")
                
                with col_dados:
                    st.markdown("### 📋 Pix Copia e Cola")
                    st.code(pix_copia_cola, language="text")
                    st.info("💡 Copie o código acima e cole no seu banco na opção 'Pix Copia e Cola'.")
                    
                    if st.button("🔄 JÁ PAGUEI, VERIFICAR AGORA"):
                        st.toast("Verificando com o Banco Central...")
                        st.warning("Pagamento em processamento. Aguarde 30 segundos.")
            else:
                st.error("Erro ao gerar os dados do QR Code. Verifique seu token.")
        
        except Exception as e:
            st.error(f"Erro ao conectar com Mercado Pago: {e}")

def exibir_suporte_footer():
    st.markdown("---")
    st.caption("Suporte Oficial VRS Soluções: vrsolucoes.sistemas@gmail.com")