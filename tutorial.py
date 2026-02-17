# ==============================================================================
# NOME DO SISTEMA: VRS SOLUÇÕES - SISTEMAS
# MÓDULO: Central de Ajuda e Tutorial (tutorial.py)
# OBJETIVO: Orientar o cliente sobre instalação, desbloqueio e uso do sistema
# DESENVOLVEDOR: Iara & Vitor
# ==============================================================================
import streamlit as st

def exibir_tutorial_vrs():
    """
    Renderiza a central de ajuda com foco em facilitar a vida do cliente.
    """
    # Estilos CSS para manter o padrão Elite
    st.markdown("""
        <style>
        .sessao-tutorial {
            background: #0a0a0a;
            border: 1px solid #222;
            padding: 25px;
            border-radius: 15px;
            margin-bottom: 20px;
        }
        .passo-numero {
            color: #00FF7F;
            font-size: 1.5rem;
            font-weight: bold;
            margin-right: 10px;
        }
        .alerta-vrs {
            border-left: 5px solid #00FF7F;
            background: rgba(0, 255, 127, 0.05);
            padding: 15px;
            border-radius: 5px;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("<h1 style='text-align: center; color: white;'>📖 Central de Ajuda VRS</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #00FF7F;'>Tudo o que você precisa para rodar seu Gerenciador de Oficina</p>", unsafe_allow_html=True)

    # --- SEÇÃO 1: DESBLOQUEIO DO WINDOWS ---
    with st.container():
        st.markdown("### 🛡️ 1. Como liberar o programa no Windows")
        st.write("""
            Como o sistema **VRS Elite** é um software de gestão profissional novo, o Windows SmartScreen pode exibir um alerta. 
            Isso é normal para programas executáveis (.exe) recém-lançados.
        """)
        
        st.markdown("""
            <div class='sessao-tutorial'>
                <p><span class='passo-numero'>01</span> Quando a tela azul aparecer, clique em <b>"Mais informações"</b>.</p>
                <p><span class='passo-numero'>02</span> Clique no botão <b>"Executar assim mesmo"</b> que aparecerá no canto inferior.</p>
                <p><span class='passo-numero'>03</span> O sistema abrirá e criará o banco de dados local automaticamente.</p>
            </div>
        """, unsafe_allow_html=True)

    # --- SEÇÃO 2: ATIVAÇÃO ---
    with st.container():
        st.markdown("### 🔑 2. Como Ativar sua Licença")
        st.write("Siga o fluxo abaixo para liberar o acesso total:")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
                <div class='alerta-vrs'>
                    <b>Passo A:</b> Escolha seu plano na vitrine e preencha seus dados reais (Nome, CPF/CNPJ, WhatsApp).
                </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown("""
                <div class='alerta-vrs'>
                    <b>Passo B:</b> Após o pagamento, nossa equipe enviará sua chave vinculada ao <b>ID da Máquina</b> informado.
                </div>
            """, unsafe_allow_html=True)

    # --- SEÇÃO 3: SUPORTE DIRETO ---
    st.markdown("---")
    st.markdown("### 🆘 Ainda precisa de ajuda?")
    
    c1, c2 = st.columns(2)
    with c1:
        st.info("📧 **E-mail Oficial:** vrsolucoes.sistemas@gmail.com")
    with c2:
        st.success("💬 **Suporte VIP:** Via WhatsApp (Link disponível no checkout)")

    # Adicionada KEY única para evitar conflito com botões de outras telas
    if st.button("⬅ VOLTAR PARA A VITRINE", use_container_width=True, key="btn_voltar_vrs_tutorial"):
        st.session_state.etapa = "vitrine"
        st.rerun()

# --- RODAPÉ VRS ---
def exibir_footer_vrs():
    st.markdown("<br><p style='text-align: center; color: #444; font-size: 0.8rem;'>VRS Soluções © 2026 - Tecnologia para Oficinas de Elite</p>", unsafe_allow_html=True)