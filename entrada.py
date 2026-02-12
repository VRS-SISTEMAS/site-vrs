# =================================================================
# NOME DO SISTEMA: VRS Soluções
# MÓDULO: entrada.py (SISTEMA DE 3 PÁGINAS - VERSÃO SEM ERROS)
# =================================================================
import streamlit as st
import sys
import os

# 1. FORÇA O PYTHON A LOCALIZAR OS ARQUIVOS NA PASTA ATUAL]
# Isso ajuda o VS Code e o Streamlit Cloud a encontrarem o 'backend' e 'botoes'
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Importação do módulo de botões (Essencial para o visual)
import botoes

# Importação segura do backend para não travar o VS Code
backend = None
try:
    import backend as vrs_backend
    backend = vrs_backend
    backend_ativo = True
except ImportError:
    backend_ativo = False

# 2. CONFIGURAÇÃO DE LAYOUT ELITE]
st.set_page_config(layout="wide", page_title="VRS Soluções - Gestão Elite", page_icon="⚡")
botoes.aplicar_estetica_vrs()

# 3. CONTROLE DE NAVEGAÇÃO (0: VITRINE, 1: CHECKOUT, 3: ADM)]
if 'etapa' not in st.session_state:
    st.session_state['etapa'] = 0

# --- PÁGINA 1: VITRINE (FOCO TOTAL NO PRODUTO) ---
if st.session_state['etapa'] == 0:
    st.markdown("<h1 style='text-align:center; font-size:60px; color:#FFFFFF;'>VRS <span style='color:#00FF7F;'>SOLUÇÕES</span></h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#888; letter-spacing:5px;'>SISTEMAS DE GESTÃO AUTOMOTIVA DE ALTA PERFORMANCE</p>", unsafe_allow_html=True)
    
    st.write("---")
    
    col_port, col_btn = st.columns([1.6, 1])
    
    with col_port:
        st.markdown("### 🖥️ O QUE VOCÊ ESTÁ ADQUIRINDO:")
        # Abas para o cliente ver o visual do sistema antes de comprar]
        aba1, aba2, aba3 = st.tabs(["📊 PAINEL DE FROTAS", "🔧 OFICINA / OS", "📦 PEÇAS"])
        with aba1:
            st.image("assets/painel.png", caption="Visualização de Frotas em Tempo Real", use_container_width=True)
        with aba2:
            st.image("assets/oficina.png", caption="Gestão de O.S e Manutenções", use_container_width=True)
        with aba3:
            st.image("assets/pecas.png", caption="Controle de Estoque e Almoxarifado", use_container_width=True)

    with col_btn:
        st.markdown("### 💎 VANTAGENS DO SISTEMA")
        st.write("✅ **PAINEL DE FROTAS**: Indicadores precisos.")
        st.write("✅ **HISTORICO GERAL**: Rastreabilidade total.")
        st.write("✅ **RELATORIO TECNICO**: Profissionalismo puro.")
        st.write("✅ **CADASTRO DE PEÇAS**: Estoque sob controle.")
        
        st.write("##")
        # Botão para avançar para a próxima página
        if st.button("QUERO ADQUIRIR ESTE SISTEMA ➡️", use_container_width=True):
            st.session_state['etapa'] = 1
            st.rerun()

# --- PÁGINA 2: CHECKOUT (CADASTRO E PAGAMENTO) ---
elif st.session_state['etapa'] == 1:
    st.markdown("## 💳 FINALIZAR ATIVAÇÃO")
    
    col_form, col_down = st.columns([2, 1])
    
    with col_form:
        tipo_cad = st.radio("Selecione o tipo de cadastro:", ["Pessoa Física (CPF)", "Empresa (CNPJ)"], horizontal=True)
        nome_cli = st.text_input("NOME COMPLETO OU RAZÃO SOCIAL:")
        doc_cli = st.text_input(f"DIGITE O {tipo_cad}:")
        email_cli = st.text_input("E-MAIL PARA RECEBER A CHAVE:")
        id_pc_cli = st.text_input("ID DA MÁQUINA (VEJA NO INSTALADOR):")
        
        st.write("---")
        # Botão de pagamento integrado no botoes.py]
        botoes.exibir_navegacao_venda("EFETUAR PAGAMENTO 🚀", nome_cli, email_cli, id_pc_cli)
        
        st.write("##")
        # Botão de Voltar para a Vitrine
        if st.button("⬅️ VOLTAR PARA VITRINE"):
            st.session_state['etapa'] = 0
            st.rerun()

    with col_down:
        botoes.download_instalador_vrs()

# --- PÁGINA 3: ESCRITÓRIO ADM (GERENCIAMENTO) ---
elif st.session_state['etapa'] == 3:
    st.markdown("## 👨‍💼 ESCRITÓRIO VRS SOLUÇÕES")
    
    # Executa funções do backend se ele estiver disponível]
    if backend_ativo:
        visitas = backend.registrar_visita()
        st.success(f"Sistema Online - Visitas Totais: {visitas}")
    else:
        st.warning("Aviso: Módulo backend não carregado no VS Code, mas o site continuará funcionando.")
        
    st.info("Espaço reservado para gestão de licenças e vendas.")
    
    if st.button("⬅️ SAIR DO PAINEL ADM"):
        st.session_state['etapa'] = 0
        st.rerun()

# --- RODAPÉ COM ACESSO ADM ---
st.write("---")
col_foo, col_adm_btn = st.columns([10, 1])
with col_foo:
    st.markdown("<p style='color:#333; font-size:12px;'>VRS SOLUÇÕES SISTEMAS © 2026 - TODOS OS DIREITOS RESERVADOS</p>", unsafe_allow_html=True)
with col_adm_btn:
    # O seu escritório secreto voltou para o cantinho]
    botoes.exibir_acesso_secreto()