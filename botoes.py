# =================================================================
# NOME DO SISTEMA: VRS Soluções
# MÓDULO: botoes.py (ESTÉTICA CARDS 3D E NAVEGAÇÃO)
# =================================================================
import streamlit as st

def aplicar_estetica_vrs():
    """ DNA Visual Elite: Fundo Dark e Efeito Cards 3D """
    st.markdown("""
        <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            html, body, [class*="st-"] { font-family: 'Segoe UI', sans-serif; color: #FFFFFF; }
            
            /* Estilo dos Cards de Planos */
            .card-vrs {
                background: #111;
                border: 1px solid #333;
                border-radius: 20px;
                padding: 30px;
                text-align: center;
                transition: 0.5s;
                margin-bottom: 20px;
            }
            .card-vrs:hover {
                border-color: #00FF7F;
                transform: translateY(-10px);
                box-shadow: 0 10px 30px rgba(0, 255, 127, 0.2);
            }
            .vrs-price { font-size: 38px; color: #00FF7F; font-weight: 800; margin: 15px 0; }
            
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
    """ Área de download compacta no checkout """
    st.markdown("<p style='color:#00FF7F; font-size:12px; margin-bottom:5px;'>💻 INSTALADOR OBRIGATÓRIO</p>", unsafe_allow_html=True)
    st.download_button(label="📥 BAIXAR INSTALADOR VRS", data="Binário", file_name="VRS_Setup.exe", use_container_width=True)

def exibir_navegacao_venda(texto_botao, nome_cli, email_cli, id_pc):
    """ Link oficial de pagamento """
    link_vrs = "https://www.mercadopago.com.br/checkout/v1/payment/redirect/?preference-id=1840049752-16a7f804-585a-4e8c-9411-96860d5f850b"
    if nome_cli and "@" in email_cli and id_pc:
        st.markdown(f'<a href="{link_vrs}" target="_blank" class="btn-vrs-pagar" style="text-decoration:none;">{texto_botao}</a>', unsafe_allow_html=True)
    else:
        st.warning("⚠️ CEO, preencha todos os campos para liberar o pagamento.")

def exibir_acesso_secreto():
    """ Ponto ADM discreto no rodapé] """
    if st.button(".", help="Acesso ADM"):
        st.session_state['etapa'] = 3
        st.rerun()