import streamlit as st

def aplicar_estetica_vrs():
    """DNA Visual Elite da VR Soluções"""
    st.markdown("""
        <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            html, body, [class*="st-"] { font-family: 'Segoe UI', sans-serif; color: #FFFFFF; }
            
            /* Botão de Pagamento de Alta Conversão */
            .btn-vrs-pagar {
                display: block; width: 100%; padding: 22px;
                background: linear-gradient(135deg, #00FF7F 0%, #008040 100%);
                color: #050a0e !important; text-align: center;
                border-radius: 15px; font-weight: 900; font-size: 26px;
                text-decoration: none !important; 
                box-shadow: 0 10px 25px rgba(0, 255, 127, 0.4);
                transition: 0.3s; cursor: pointer; border: none;
            }
            .btn-vrs-pagar:hover { transform: translateY(-3px); box-shadow: 0 15px 35px rgba(0, 255, 127, 0.6); }
        </style>
    """, unsafe_allow_html=True)

def exibir_navegacao_venda(texto_botao, nome_cli, email_cli):
    """Gera o checkout seguro que pula o erro de processamento"""
    
    # Este link aponta direto para a sua preferência de pagamento de R$ 99,99
    # Ele é mais estável que o link de perfil
    link_vrs_final = "https://www.mercadopago.com.br/checkout/v1/payment/redirect/?preference-id=1840049752-16a7f804-585a-4e8c-9411-96860d5f850b"
    
    if nome_cli and "@" in email_cli:
        # Forçamos a abertura em uma aba totalmente limpa do navegador
        st.markdown(f'''
            <div style="width: 100%; margin-top: 15px;">
                <form action="{link_vrs_final}" method="get" target="_blank">
                    <button type="submit" class="btn-vrs-pagar">
                        {texto_botao}
                    </button>
                </form>
            </div>
        ''', unsafe_allow_html=True)
    else:
        st.warning("⚠️ Informe NOME e E-MAIL corretamente para liberar o pagamento.")

def exibir_acesso_secreto():
    """Mantém o ponto de acesso administrativo"""
    if st.button(".", help="Acesso"):
        st.session_state['etapa'] = 3
        st.rerun()