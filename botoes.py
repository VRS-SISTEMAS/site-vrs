# =================================================================
# NOME DO SISTEMA: VRS Soluções
# MÓDULO: botoes.py (DESIGN DE ELITE + ESTABILIDADE)
# =================================================================
import streamlit as st

def aplicar_estetica_vrs():
    """ DNA Visual da VRS Soluções: Fundo Dark e Letras Brancas """
    st.markdown("""
        <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            
            /* Define a cor branca e fonte limpa conforme solicitado */
            html, body, [class*="st-"] { font-family: 'Segoe UI', sans-serif; color: #FFFFFF; }
            
            /* Nome da marca pequeno no canto conforme sua preferência */
            .vrs-brand { position: fixed; top: 10px; left: 10px; font-size: 11px; color: #666; z-index: 1000; }
            
            /* Botão de Pagamento Luxuoso (Sempre visível, mas com aviso) */
            .btn-vrs-pagar {
                display: block; width: 100%; padding: 20px;
                background: linear-gradient(135deg, #00FF7F 0%, #008040 100%);
                color: #050a0e !important; text-align: center;
                border-radius: 12px; font-weight: 900; font-size: 24px;
                text-decoration: none !important; box-shadow: 0 10px 20px rgba(0, 255, 127, 0.3);
            }
        </style>
        <div class="vrs-brand">VRS Soluções</div>
    """, unsafe_allow_html=True)

def download_instalador_vrs():
    """ Resolve o erro AttributeError e organiza o topo da página """
    st.markdown("""
        <div style="background: rgba(0, 200, 83, 0.1); border: 1px solid #00c853; border-radius: 15px; padding: 20px; text-align: center;">
            <h4 style="color:#00FF7F; margin:0;">📥 PASSO OBRIGATÓRIO</h4>
            <p style="color:#ccc; font-size:14px;">Baixe o instalador para obter o ID da sua máquina antes da ativação.</p>
        </div>
    """, unsafe_allow_html=True)
    st.download_button(
        label="CLIQUE AQUI PARA BAIXAR O INSTALADOR VRS",
        data="Instalador VRS Soluções", 
        file_name="VRS_Elite_Setup.exe",
        use_container_width=True
    )

def exibir_navegacao_venda(texto_botao, nome_cli, email_cli):
    """ Habilita o pagamento e abre em nova aba para evitar erros """
    link_final = "https://www.mercadopago.com.br/checkout/v1/payment/redirect/?preference-id=1840049752-16a7f804-585a-4e8c-9411-96860d5f850b"
    
    # O segredo: Se os dados não estiverem completos, mostramos o aviso em vez de apagar o botão
    if nome_cli and "@" in email_cli:
        st.markdown(f'''
            <form action="{link_final}" method="get" target="_blank">
                <button type="submit" class="btn-vrs-pagar">{texto_botao}</button>
            </form>
        ''', unsafe_allow_html=True)
    else:
        st.error("⚠️ Preencha Nome e E-mail acima para liberar o pagamento.")

def exibir_acesso_secreto():
    if st.button(".", help="Acesso ADM"):
        st.session_state['etapa'] = 3
        st.rerun()