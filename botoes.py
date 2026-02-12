# =================================================================
# NOME DO SISTEMA: VRS Soluções
# MÓDULO: botoes.py (DESIGN DE ELITE INCLUSIVO)
# =================================================================
import streamlit as st

def aplicar_estetica_vrs():
    """ DNA Visual: Fundo Dark, Letras Brancas e Estilo Software de Luxo """
    st.markdown("""
        <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            
            /* Tipografia limpa e cores de alto contraste para leitura fácil */
            html, body, [class*="st-"] { 
                font-family: 'Segoe UI', sans-serif; 
                color: #FFFFFF; 
            }
            
            /* Nome da marca discreto no topo conforme solicitado */
            .vrs-brand { 
                position: fixed; top: 10px; left: 10px; 
                font-size: 11px; color: #555; z-index: 1000; 
            }
            
            /* Botão de Pagamento com brilho e gradiente de alta conversão */
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
    """ Organiza a área de download com visual moderno """
    st.markdown("""
        <div style="background: rgba(0, 255, 127, 0.05); border: 1px dashed #00FF7F; border-radius: 15px; padding: 20px; text-align: center;">
            <h4 style="color:#00FF7F; margin:0;">📥 PRIMEIRO PASSO</h4>
            <p style="color:#888; font-size:13px;">Baixe o instalador para identificar sua máquina.</p>
        </div>
    """, unsafe_allow_html=True)
    st.download_button(
        label="📥 BAIXAR INSTALADOR VRS ELITE",
        data="Executável aqui", 
        file_name="VRS_Elite_Setup.exe",
        use_container_width=True,
        help="Execute para obter o seu ID de ativação."
    )

def exibir_navegacao_venda(texto_botao, nome_cli, email_cli, id_pc):
    """ Habilita o checkout apenas com dados preenchidos para segurança """
    link_vrs = "https://www.mercadopago.com.br/checkout/v1/payment/redirect/?preference-id=1840049752-16a7f804-585a-4e8c-9411-96860d5f850b"
    
    # Validação inteligente: nome, e-mail válido e ID da máquina presente
    if nome_cli and "@" in email_cli and id_pc:
        st.markdown(f'''
            <form action="{link_vrs}" method="get" target="_blank">
                <button type="submit" class="btn-vrs-pagar">{texto_botao}</button>
            </form>
        ''', unsafe_allow_html=True)
    else:
        st.warning("⚠️ Preencha Nome, E-mail e ID da Máquina para habilitar o pagamento.")

def exibir_acesso_secreto():
    if st.button(".", help="Acesso ADM"):
        st.session_state['etapa'] = 3
        st.rerun()