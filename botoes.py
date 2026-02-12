# =================================================================
# NOME DO SISTEMA: VRS Soluções
# MÓDULO: botoes.py (VERSÃO INTEGRADA COM DOWNLOAD E PAGAMENTO)
# =================================================================
import streamlit as st

def aplicar_estetica_vrs():
    """
    Aplica o DNA visual de Elite da VRS Soluções.
    Remove menus padrão do Streamlit e define fontes e cores da marca.
    """
    st.markdown("""
        <style>
            /* Remove elementos padrão para parecer um software nativo */
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            
            /* Define a tipografia e cor global do texto */
            html, body, [class*="st-"] { 
                font-family: 'Segoe UI', sans-serif; 
                color: #FFFFFF; 
            }
            
            /* Estilização do nome da marca no topo (VRS Soluções) */
            .marca-topo {
                font-size: 12px;
                color: #888;
                position: fixed;
                top: 10px;
                left: 10px;
            }
            
            /* Estilização luxuosa do botão de pagamento */
            .btn-vrs-pagar {
                display: block; 
                width: 100%; 
                padding: 22px;
                background: linear-gradient(135deg, #00FF7F 0%, #008040 100%);
                color: #050a0e !important; 
                text-align: center;
                border-radius: 15px; 
                font-weight: 900; 
                font-size: 26px;
                text-decoration: none !important; 
                box-shadow: 0 10px 25px rgba(0, 255, 127, 0.4);
                transition: 0.3s; 
                cursor: pointer; 
                border: none;
            }
            .btn-vrs-pagar:hover { 
                transform: translateY(-3px); 
                box-shadow: 0 15px 35px rgba(0, 255, 127, 0.6); 
            }
        </style>
        <div class="marca-topo">VRS Soluções</div>
    """, unsafe_allow_html=True)

def download_instalador_vrs():
    """
    Cria a área de download do instalador oficial.
    Esta função resolve o erro AttributeError no checkout.py.
    """
    st.markdown("#### 📥 Download do Sistema")
    
    # Texto informativo sobre o instalador
    st.info("O instalador é necessário para gerar o ID da sua máquina e ativar sua licença.")
    
    # Botão de download (O arquivo deve estar na mesma pasta ou em um link direto)
    # Nota: Você pode substituir 'Instalador_VRS.exe' pelo link real do seu servidor futuramente.
    st.download_button(
        label="CLIQUE AQUI PARA BAIXAR O INSTALADOR (EXE)",
        data="Conteúdo do instalador", # Aqui você pode apontar para o binário do seu instalador
        file_name="Instalador_VRS_Elite.exe",
        mime="application/octet-stream",
        use_container_width=True,
        help="Baixe o software para obter seu ID de ativação."
    )

def exibir_navegacao_venda(texto_botao, nome_cli, email_cli):
    """
    Gera o checkout seguro do Mercado Pago.
    Usa um formulário HTML para evitar bloqueios de segurança do banco.
    """
    # Preferência oficial de pagamento VRS Soluções
    link_vrs_final = "https://www.mercadopago.com.br/checkout/v1/payment/redirect/?preference-id=1840049752-16a7f804-585a-4e8c-9411-96860d5f850b"
    
    if nome_cli and "@" in email_cli:
        # Cria o botão de pagamento usando formulário para abrir em nova aba
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
        # Alerta caso os campos obrigatórios não estejam preenchidos
        st.warning("⚠️ Informe NOME e E-MAIL corretamente para liberar o botão de pagamento.")

def exibir_acesso_secreto():
    """
    Ponto de entrada invisível para administração.
    Localizado discretamente como um ponto final.
    """
    if st.button(".", help="Acesso Administrativo VRS"):
        st.session_state['etapa'] = 3
        st.rerun()