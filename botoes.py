import streamlit as st

def aplicar_estetica_vrs():
    """ DNA Visual: Fundo Dark e Design via Código (Sem Erros de Imagem) """
    st.markdown("""
        <style>
            #MainMenu, footer, header {visibility: hidden;}
            html, body, [class*="st-"] { font-family: 'Segoe UI', sans-serif; color: #FFFFFF; }
            
            /* Cards Luxuosos em CSS Puro */
            .card-vrs {
                background: #111111;
                border: 2px solid #333;
                border-radius: 15px;
                padding: 30px;
                text-align: center;
                transition: 0.3s;
                height: 380px;
                display: flex;
                flex-direction: column;
                justify-content: center;
            }
            .card-vrs:hover {
                border-color: #00FF7F;
                transform: translateY(-5px);
                box-shadow: 0 10px 20px rgba(0, 255, 127, 0.2);
            }
            .vrs-titulo { font-size: 28px; font-weight: 800; color: #FFFFFF; margin-bottom: 10px; }
            .vrs-preco { font-size: 38px; color: #00FF7F; font-weight: 900; margin: 10px 0; }
            .vrs-desc { color: #888; font-size: 14px; line-height: 1.6; }
            
            /* Botão de Pagamento Mercado Pago */
            .btn-vrs-pagar {
                display: block; width: 100%; padding: 20px;
                background: linear-gradient(135deg, #00FF7F 0%, #008040 100%);
                color: #050a0e !important; text-align: center;
                border-radius: 12px; font-weight: 900; font-size: 24px;
                text-decoration: none !important;
            }
        </style>
    """, unsafe_allow_html=True)

def download_instalador_vrs():
    st.markdown("<p style='color:#00FF7F; font-size:12px; text-align:center;'>💻 INSTALADOR OBRIGATÓRIO</p>", unsafe_allow_html=True)
    st.download_button(label="📥 BAIXAR SETUP VRS", data="Setup", file_name="VRS_Setup.exe", use_container_width=True)

def exibir_navegacao_venda(texto_botao, nome_cli, email_cli, id_pc):
    link_vrs = "https://www.mercadopago.com.br/checkout/v1/payment/redirect/?preference-id=1840049752-16a7f804-585a-4e8c-9411-96860d5f850b"
    if nome_cli and id_pc:
        st.markdown(f'<a href="{link_vrs}" target="_blank" class="btn-vrs-pagar">{texto_botao}</a>', unsafe_allow_html=True)
    else:
        st.warning("⚠️ Preencha os dados e o ID para liberar o pagamento.")

def exibir_acesso_secreto():
    if st.button(".", help="ADM"):
        st.session_state['etapa'] = 3
        st.rerun()