# =================================================================
# NOME DO SISTEMA: VRS Soluções
# MÓDULO: botoes.py (DNA VISUAL ELITE)
# =================================================================
import streamlit as st

def aplicar_estetica_vrs():
    """ DNA Visual: Fundo Dark e Cards com Estilo Profissional """
    st.markdown("""
        <style>
            #MainMenu {visibility: hidden;} footer {visibility: hidden;} header {visibility: hidden;}
            html, body, [class*="st-"] { font-family: 'Segoe UI', sans-serif; color: #FFFFFF; }
            
            /* Estilo dos Cards de Planos - Padrão Elite */
            .card-vrs {
                background: #111111;
                border: 1px solid #333333;
                border-radius: 15px;
                padding: 35px 20px;
                text-align: center;
                transition: 0.3s ease-in-out;
                margin-bottom: 15px;
            }
            .card-vrs:hover {
                border-color: #00FF7F;
                transform: translateY(-5px);
                box-shadow: 0 10px 20px rgba(0, 255, 127, 0.1);
            }
            .vrs-titulo { font-size: 26px; font-weight: 800; letter-spacing: 1px; color: #FFFFFF; }
            .vrs-preco { font-size: 34px; color: #00FF7F; font-weight: 900; margin: 15px 0; }
            .vrs-recursos { color: #AAAAAA; font-size: 14px; line-height: 1.6; text-align: left; padding: 0 10px; }
            
            /* Botão de Pagamento Mercado Pago] */
            .btn-vrs-pagar {
                display: block; width: 100%; padding: 18px;
                background: linear-gradient(135deg, #00FF7F 0%, #008040 100%);
                color: #050a0e !important; text-align: center;
                border-radius: 10px; font-weight: 900; font-size: 22px;
                text-decoration: none !important;
            }
        </style>
    """, unsafe_allow_html=True)

def download_instalador_vrs():
    """ Área de download compacta no checkout """
    st.markdown("<p style='color:#00FF7F; font-size:12px; margin-bottom:5px; text-align:center;'>💻 INSTALADOR OBRIGATÓRIO</p>", unsafe_allow_html=True)
    st.download_button(label="📥 BAIXAR INSTALADOR VRS", data="Setup", file_name="VRS_Setup.exe", use_container_width=True)

def exibir_navegacao_venda(texto_botao, nome_cli, email_cli, id_pc):
    """ Gera o link seguro do Mercado Pago] """
    link_vrs = "https://www.mercadopago.com.br/checkout/v1/payment/redirect/?preference-id=1840049752-16a7f804-585a-4e8c-9411-96860d5f850b"
    if nome_cli and "@" in email_cli and id_pc:
        st.markdown(f'<a href="{link_vrs}" target="_blank" class="btn-vrs-pagar">{texto_botao}</a>', unsafe_allow_html=True)
    else:
        st.warning("⚠️ Preencha os dados e o ID da Máquina para ativar.")

def exibir_acesso_secreto():
    """ Botão administrativo discreto] """
    if st.button(".", help="Acesso ADM"):
        st.session_state['etapa'] = 3
        st.rerun()