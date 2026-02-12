# =================================================================
# NOME DO SISTEMA: VRS Soluções
# MÓDULO: botoes.py (NAVEGAÇÃO ELITE E ESTÉTICA)
# =================================================================
import streamlit as st

def aplicar_estetica_vrs():
    """ DNA Visual: Fundo Dark, Letras Brancas e Estilo Software Premium """
    st.markdown("""
        <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            html, body, [class*="st-"] { font-family: 'Segoe UI', sans-serif; color: #FFFFFF; }
            
            /* Botão de Próxima Etapa / Avançar */
            .stButton>button {
                width: 100%;
                background: linear-gradient(135deg, #00FF7F 0%, #008040 100%);
                color: #050a0e !important;
                font-weight: 900;
                border-radius: 10px;
                border: none;
                height: 50px;
                transition: 0.3s;
            }
            
            /* Botão Voltar (Estilo mais discreto) */
            .btn-voltar button {
                background: #333 !important;
                color: white !important;
            }

            /* Botão de Pagamento Mercado Pago */
            .btn-vrs-pagar {
                display: block; width: 100%; padding: 20px;
                background: linear-gradient(135deg, #00FF7F 0%, #008040 100%);
                color: #050a0e !important; text-align: center;
                border-radius: 15px; font-weight: 900; font-size: 24px;
                text-decoration: none !important; 
                box-shadow: 0 10px 30px rgba(0, 255, 127, 0.4);
            }
        </style>
    """, unsafe_allow_html=True)

def download_instalador_vrs():
    """ Área de download para obter o ID da máquina """
    st.markdown("<p style='color:#00FF7F; font-size:12px; margin-bottom:5px;'>💻 INSTALADOR OBRIGATÓRIO</p>", unsafe_allow_html=True)
    st.download_button(
        label="📥 BAIXAR INSTALADOR VRS",
        data="Binário aqui", 
        file_name="VRS_Elite_Setup.exe",
        use_container_width=True
    )

def exibir_navegacao_venda(texto_botao, nome_cli, email_cli, id_pc):
    """ Gera o link de pagamento final do Mercado Pago """
    link_vrs = "https://www.mercadopago.com.br/checkout/v1/payment/redirect/?preference-id=1840049752-16a7f804-585a-4e8c-9411-96860d5f850b"
    if nome_cli and "@" in email_cli and id_pc:
        st.markdown(f'<a href="{link_vrs}" target="_blank" class="btn-vrs-pagar" style="text-decoration:none;">{texto_botao}</a>', unsafe_allow_html=True)
    else:
        st.warning("⚠️ Preencha Nome, E-mail e ID da Máquina para pagar.")

def proxima_etapa(nova_etapa):
    """ Função para avançar entre as páginas do site """
    st.session_state['etapa'] = nova_etapa
    st.rerun()

def exibir_acesso_secreto():
    """ Botão discreto para o seu escritório """
    if st.button(".", help="Acesso ADM"):
        proxima_etapa(3)