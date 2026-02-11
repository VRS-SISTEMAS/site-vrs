# =================================================================
# NOME DO SISTEMA: VR SOLUÇÕES Sistemas
# MÓDULO: entrada.py (Versão High-End com Administração Integrada)
# =================================================================
import streamlit as st
import botoes
import seguranca  # Usa a tua lógica de criptografia oficial
import pandas as pd
import datetime

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(layout="wide", initial_sidebar_state="collapsed")

# (Mantive todo o teu CSS original aqui para não mudar o visual)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
    .vrs-header { position: absolute; top: -75px; left: 0; font-size: 18px; color: #00c853; font-weight: bold; letter-spacing: 3px; }
    .card-vrs { background: linear-gradient(145deg, #1e1e1e, #141414); border-radius: 15px; padding: 15px; border: 1px solid #333; text-align: center; height: 310px; }
    .preco { font-size: 26px; font-weight: bold; color: #00c853; margin: 10px 0; }
</style>
""", unsafe_allow_html=True)

if 'pagina_ativa' not in st.session_state:
    st.session_state['pagina_ativa'] = 'home'

def exibir_home():
    botoes.marca_topo()
    st.markdown("<div class='vrs-header'>VR SOLUÇÕES - SISTEMAS</div>", unsafe_allow_html=True)
    
    # ... (Seu conteúdo de vantagens e planos continua aqui igual ao original) ...
    st.markdown("<h4 style='text-align: center;'>Conheça os Planos <span style='color:#00c853'>VRS ELITE</span></h4>", unsafe_allow_html=True)
    
    # Exemplo simplificado dos seus colunas/botões para o código não ficar gigante:
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("ASSINAR BÁSICO", use_container_width=True):
            st.session_state['plano_escolhido'] = 'Básico'; st.session_state['pagina_ativa'] = 'checkout'; st.rerun()
    with col2:
        if st.button("ASSINAR JÚNIOR", use_container_width=True):
            st.session_state['plano_escolhido'] = 'Júnior'; st.session_state['pagina_ativa'] = 'checkout'; st.rerun()
    with col3:
        if st.button("ASSINAR SÊNIOR", use_container_width=True):
            st.session_state['plano_escolhido'] = 'Sênior'; st.session_state['pagina_ativa'] = 'checkout'; st.rerun()

    # Botão para o teu Escritório
    st.markdown("<br><br>", unsafe_allow_html=True)
    if st.button("🔐 Acesso Administrativo (Vitor)", key="btn_admin"):
        st.session_state['pagina_ativa'] = 'escritorio'
        st.rerun()

def exibir_escritorio():
    st.title("🏢 Administração VR Soluções")
    
    if 'autenticado' not in st.session_state:
        st.session_state['autenticado'] = False

    if not st.session_state['autenticado']:
        # Usando a tua senha do gerador_mestre.py
        senha = st.text_input("Senha do Proprietário:", type="password")
        if st.button("Entrar no Painel"):
            if senha == "Vitor123": # Tua senha oficial
                st.session_state['autenticado'] = True
                st.rerun()
            else:
                st.error("Acesso Negado!")
    else:
        st.success("Bem-vindo, Vitor! Painel de Licenciamento Ativo.")
        
        # --- TEU GERADOR DE LICENÇAS INTEGRADO ---
        st.markdown("### 🔑 Gerar Chave de Ativação")
        col_id, col_pl = st.columns([2, 1])
        with col_id:
            id_cli = st.text_input("ID do Hardware do Cliente:", placeholder="Ex: B32163D3")
        with col_pl:
            plano_sel = st.selectbox("Plano:", ["BASICO", "JUNIOR", "SENIOR"])
        
        if st.button("GERAR CHAVE AGORA"):
            if id_cli:
                # Usa a tua lógica do seguranca.py
                chave = seguranca.gerar_chave_final(id_cli.strip().upper(), plano_sel)
                st.code(chave, language="text")
                st.info(f"Licença {plano_sel} pronta para envio.")
            else:
                st.warning("Insira o ID do cliente!")

        if st.button("Sair do Escritório"):
            st.session_state['autenticado'] = False
            st.session_state['pagina_ativa'] = 'home'
            st.rerun()

# ROTEADOR (Mantém os teus redirecionamentos)
if st.session_state['pagina_ativa'] == 'home':
    exibir_home()
elif st.session_state['pagina_ativa'] == 'escritorio':
    exibir_escritorio()
# ... (Continua com checkout e sucesso)