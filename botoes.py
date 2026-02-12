# =================================================================
# NOME DO SISTEMA: VRS Soluções
# MÓDULO: botoes.py (ESTILO LUXO E DOWNLOAD DISCRETO)
# =================================================================
import streamlit as st

def aplicar_estetica_vrs():
    """ Define o DNA visual Dark Elite: fundo escuro e letras brancas """
    st.markdown("""
        <style>
            /* Esconde menus desnecessários do Streamlit */
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            
            /* Tipografia limpa e cor branca para leitura em dark mode */
            html, body, [class*="st-"] { 
                font-family: 'Segoe UI', sans-serif; 
                color: #FFFFFF; 
            }
            
            /* Nome da marca minúsculo no topo para identidade visual */
            .vrs-brand { 
                position: fixed; top: 10px; left: 10px; 
                font-size: 11px; color: #555; z-index: 1000; 
            }
            
            /* Botão de Pagamento com gradiente verde de alta performance */
            .btn-vrs-pagar {
                display: block; width: 100%; padding: 22px;
                background: linear-gradient(135deg, #00FF7F 0%, #008040 100%);
                color: #050a0e !important; text-align: center;
                border-radius: 15px; font-weight: 900; font-size: 28px;
                text-decoration: none !important; 
                box-shadow: 0 10px 30px rgba(0, 255, 127, 0.4);
                transition: 0.3s; cursor: pointer; border: none;
            }
            .btn-vrs-pagar:hover { 
                transform: scale(1.02); 
                box-shadow: 0 15px 40px rgba(0, 255, 127, 0.6); 
            }
        </style>
        <div class="vrs-brand">VRS Soluções</div>
    """, unsafe_allow_html=True)

def download_instalador_vrs():
    """ 
    Cria a área de download simplificada.
    Reduzido o tamanho para dar foco ao portfólio de vendas.
    """
    st.markdown("<p style='color:#00FF7F; font-size:12px; margin-bottom:5px; text-align:center;'>💻 NECESSÁRIO PARA ATIVAÇÃO</p>", unsafe_allow_html=True)
    st.download_button(
        label="📥 BAIXAR INSTALADOR",
        data="Executável aqui", 
        file_name="VRS_Elite_Setup.exe",
        use_container_width=True,
        help="Baixe para obter o seu ID de máquina."
    )

def exibir_navegacao_venda(texto_botao, nome_cli, email_cli, id_pc):
    """ Habilita o checkout oficial em nova aba """
    link_vrs = "https://www.mercadopago.com.br/checkout/v1/payment/redirect/?preference-id=1840049752-16a7f804-585a-4e8c-9411-96860d5f850b"
    
    # Valida se os dados essenciais foram preenchidos
    if nome_cli and "@" in email_cli and id_pc:
        st.markdown(f'''
            <form action="{link_vrs}" method="get" target="_blank">
                <button type="submit" class="btn-vrs-pagar">{texto_botao}</button>
            </form>
        ''', unsafe_allow_html=True)
    else:
        # Alerta amigável se o cliente esquecer algum dado
        st.warning("⚠️ Informe Nome, E-mail e ID da Máquina para habilitar o pagamento.")

def exibir_acesso_secreto():
    """ Botão administrativo discreto """
    if st.button(".", help="Acesso ADM"):
        st.session_state['etapa'] = 3
        st.rerun()