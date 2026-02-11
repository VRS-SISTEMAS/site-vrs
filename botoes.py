# =================================================================
# NOME DO SISTEMA: VR SOLUÇÕES Sistemas
# MÓDULO: botoes.py (Versão Elite Final de Produção)
# DESCRIÇÃO: Gerenciamento de checkout PIX e integração Mercado Pago
# =================================================================
import streamlit as st
import json
import os
import datetime
import servico_email
import mercadopago

# --- CONFIGURAÇÃO MERCADO PAGO ---
# Token de produção oficial da VR Soluções
ACCESS_TOKEN = "APP_USR-2172848802037320-020911-a95977c8dfa2d0579a1fa8bcc796a834-130182760" 
sdk = mercadopago.SDK(ACCESS_TOKEN)

def aplicar_estetica_vrs():
    """Injeta o CSS que padroniza a beleza de todos os botões do site"""
    st.markdown("""
    <style>
        .stButton>button {
            width: 220px !important;
            height: 3.2em !important;
            border-radius: 12px !important;
            font-weight: 700 !important;
            letter-spacing: 1px !important;
            transition: all 0.4s ease !important;
            text-transform: uppercase !important;
            border: 1px solid rgba(255,255,255,0.1) !important;
            display: block !important;
            margin: 0 auto !important;
        }
        /* Estilo específico para o botão de ação principal (verde) */
        div[data-testid="stHorizontalBlock"] > div:last-child button {
            background: linear-gradient(145deg, #00FF7F, #00CC66) !important;
            color: #050a0e !important;
            box-shadow: 0px 4px 15px rgba(0, 255, 127, 0.3) !important;
        }
    </style>
    """, unsafe_allow_html=True)

def criar_pix_vrs(nome_cli, email_cli, plano_nome):
    """Gera o pagamento Pix oficial via API do Mercado Pago com valores REAIS"""
    
    # Dicionário de preços oficiais da VR Soluções
    valores = {
        "BÁSICO": 99.99, 
        "JÚNIOR 🚀": 139.99, 
        "SÊNIOR 💎": 299.99
    }
    
    # Busca o valor baseado no plano ou assume o básico como padrão
    valor_final = valores.get(plano_nome, 99.99)

    # Montagem do corpo da requisição para o Mercado Pago
    payment_data = {
        "transaction_amount": valor_final,
        "description": f"Assinatura {plano_nome} - VR Soluções",
        "payment_method_id": "pix",
        "payer": {
            "email": email_cli.strip(),
            "first_name": nome_cli.strip(),
            "last_name": "VRS"
        }
    }

    try:
        # Chamada oficial para criar o pagamento no servidor
        resultado = sdk.payment().create(payment_data)
        pagamento = resultado["response"]
        
        # Validação: Se não retornar ID, algo deu errado com as credenciais
        if "id" not in pagamento:
            st.error(f"Erro Mercado Pago: {pagamento.get('message', 'Verifique seu Token')}")
            return None
            
        # Retorna os dados necessários para exibir o QR Code na tela
        return {
            "id": pagamento["id"],
            "copia_e_cola": pagamento["point_of_interaction"]["transaction_data"]["qr_code"],
            "qr_code_imagem": pagamento["point_of_interaction"]["transaction_data"]["qr_code_base64"]
        }
    except Exception as e:
        st.error(f"Falha técnica na API: {e}")
        return None

def salvar_venda_local(cliente, plano, email, status="Aguardando"):
    """Registra a tentativa de venda ou confirmação no arquivo JSON local"""
    arquivo_vendas = "vendas_vrs.json"
    agora = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    
    nova_venda = {
        "data": agora, 
        "cliente": cliente, 
        "email": email, 
        "plano": plano, 
        "status": status
    }
    
    vendas = []
    # Carrega vendas existentes se o arquivo já existir
    if os.path.exists(arquivo_vendas):
        with open(arquivo_vendas, "r", encoding="utf-8") as f:
            try: vendas = json.load(f)
            except: vendas = []
            
    vendas.append(nova_venda)
    
    # Salva a lista atualizada
    with open(arquivo_vendas, "w", encoding="utf-8") as f:
        json.dump(vendas, f, indent=4, ensure_ascii=False)

def exibir_navegacao_venda(texto_avancar="PRÓXIMO ➡️", nome_cli="", email_cli=""):
    """Gerencia a interface de navegação entre as etapas de compra e o QR Code"""
    aplicar_estetica_vrs()
    col_v, _, col_a = st.columns([1, 1, 1])
    
    with col_v:
        # Botão para retornar à seleção de planos
        if st.button("⬅️ VOLTAR"):
            st.session_state['etapa'] = 1
            st.rerun()
            
    with col_a:
        # Botão para avançar e gerar o PIX
        if st.button(texto_avancar):
            if not nome_cli.strip() or not email_cli.strip():
                st.error("⚠️ Preencha Nome e E-mail!")
            else:
                plano = st.session_state.get('plano', 'BÁSICO')
                pix = criar_pix_vrs(nome_cli, email_cli, plano)
                if pix:
                    # Armazena os dados do PIX e do cliente na sessão para uso posterior
                    st.session_state['pix'] = pix
                    st.session_state['pagando'] = True
                    st.session_state['cliente_atual'] = nome_cli
                    st.session_state['email_atual'] = email_cli
                    salvar_venda_local(nome_cli, plano, email_cli)

    # Bloco de exibição do QR Code após o clique em avançar
    if st.session_state.get('pagando'):
        st.markdown("---")
        st.markdown("<h2 style='text-align:center; color:#00FF7F;'>ESCANEIE PARA PAGAR</h2>", unsafe_allow_html=True)
        
        # Exibe a imagem do QR Code centralizada
        st.markdown(f'<p align="center"><img src="data:image/png;base64,{st.session_state["pix"]["qr_code_imagem"]}" width="300"></p>', unsafe_allow_html=True)
        
        # Campo para facilitar o Copia e Cola
        st.text_input("PIX COPIA E COLA:", value=st.session_state["pix"]["copia_e_cola"])
        
        # --- BLINDAGEM MESTRE: VERIFICAÇÃO REAL DO BANCO ---
        if st.button("VERIFICAR PAGAMENTO 🛡️"):
            with st.spinner("Consultando banco de dados do Mercado Pago..."):
                ID_PAGAMENTO = st.session_state['pix']['id']
                # Consulta o status direto no servidor do Mercado Pago
                consulta = sdk.payment().get(ID_PAGAMENTO)
                status_real = consulta["response"].get("status")

                if status_real == "approved":
                    # AÇÃO CRÍTICA: Envia o e-mail apenas se o banco confirmou o dinheiro
                    servico_email.enviar_chave_vrs(
                        st.session_state['email_atual'], 
                        st.session_state['cliente_atual'], 
                        st.session_state.get('plano')
                    )
                    
                    # Atualiza o registro local para "Pago ✅"
                    salvar_venda_local(
                        st.session_state['cliente_atual'], 
                        st.session_state.get('plano'), 
                        st.session_state['email_atual'], 
                        status="Pago ✅"
                    )
                    
                    # Efeitos visuais de sucesso
                    st.balloons()
                    st.success("✅ PAGAMENTO CONFIRMADO!")
                    st.info("📧 Verifique seu e-mail, sua licença de 30 dias foi enviada.")
                    st.session_state['pagando'] = False
                    st.stop()
                else:
                    # Mensagem de erro caso o Pix ainda não tenha sido concluído
                    st.error("⚠️ PAGAMENTO NÃO IDENTIFICADO! Por favor, realize o Pix e aguarde alguns segundos antes de verificar novamente.")