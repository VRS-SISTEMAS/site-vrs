import streamlit as st

def aplicar_estetica_vrs():
    """ Estilização Cinematográfica para os Cards de Planos """
    st.markdown("""
        <style>
            #MainMenu, footer, header {visibility: hidden;}
            html, body, [class*="st-"] { font-family: 'Segoe UI', sans-serif; color: #FFFFFF; }
            
            /* Design dos Cards 3D (Inspirado na sua imagem) */
            .card-vrs {
                background: linear-gradient(145deg, #1a1a1a, #0d0d0d);
                border: 1px solid #333;
                border-radius: 20px;
                padding: 40px 25px;
                text-align: center;
                transition: 0.4s;
                height: 480px;
                display: flex;
                flex-direction: column;
                justify-content: space-between;
                box-shadow: 10px 10px 20px #050505, -5px -5px 15px #1a1a1a;
            }
            .card-vrs:hover {
                border-color: #00FF7F;
                transform: scale(1.03);
                box-shadow: 0 0 30px rgba(0, 255, 127, 0.2);
            }
            .vrs-titulo { font-size: 30px; font-weight: 900; letter-spacing: 2px; text-transform: uppercase; }
            .vrs-preco { font-size: 42px; color: #00FF7F; font-weight: 900; margin: 20px 0; text-shadow: 0 0 10px rgba(0, 255, 127, 0.5); }
            .vrs-lista { color: #888; font-size: 15px; text-align: left; line-height: 1.8; margin-bottom: 30px; }
            
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
    """ Área de download compacta """
    st.markdown("<p style='color:#00FF7F; font-size:12px; text-align:center;'>💻 INSTALADOR OBRIGATÓRIO</p>", unsafe_allow_html=True)
    st.download_button(label="📥 BAIXAR SETUP VRS", data="Setup", file_name="VRS_Elite.exe", use_container_width=True)

def exibir_navegacao_venda(texto_botao, nome_cli, email_cli, id_pc):
    """ Link oficial de ativação """
    link_vrs = "https://www.mercadopago.com.br/checkout/v1/payment/redirect/?preference-id=1840049752-16a7f804-585a-4e8c-9411-96860d5f850b"
    if nome_cli and "@" in email_cli and id_pc:
        st.markdown(f'<a href="{link_vrs}" target="_blank" class="btn-vrs-pagar">{texto_botao}</a>', unsafe_allow_html=True)
    else:
        st.warning("⚠️ Preencha os campos para liberar o botão de pagamento.")

def exibir_acesso_secreto():
    if st.button(".", help="ADM"):
        st.session_state['etapa'] = 3
        st.rerun()