# =================================================================
# NOME DO SISTEMA: VRS Soluções
# MÓDULO: checkout.py (DESIGN DE ELITE COM PORTFÓLIO REAL)
# =================================================================
import streamlit as st
import botoes 
import os

# Configuração de página de alta performance
st.set_page_config(layout="wide", page_title="VRS Soluções - Ativação Elite", page_icon="⚡")
botoes.aplicar_estetica_vrs()

# --- HEADER LUXUOSO ---
st.markdown("<h1 style='text-align:center; font-size:60px; font-weight:900; margin-bottom:0; color:#00FF7F;'>VRS SOLUÇÕES</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#888; letter-spacing:10px; margin-top:-10px;'>O FUTURO DA GESTÃO AUTOMOTIVA</p>", unsafe_allow_html=True)

st.write("---")

# --- ÁREA DE VENDAS (ESQUERDA: PRODUTOS | DIREITA: FORMULÁRIO) ---
col_vitrine, col_venda = st.columns([1.4, 1])

with col_vitrine:
    st.markdown("### 🖥️ CONHEÇA SEU NOVO ECOSSISTEMA")
    
    # Função para carregar imagem de forma segura e evitar erro de 'imagem quebrada'
    def exibir_foto_vrs(nome_arquivo, legenda):
        caminho = os.path.join("assets", nome_arquivo)
        if os.path.exists(caminho):
            st.image(caminho, caption=legenda, use_container_width=True)
        else:
            # Aviso caso você esqueça de colocar a foto na pasta assets
            st.warning(f"⚠️ CEO, coloque a foto '{nome_arquivo}' na pasta 'assets' para ela brilhar aqui!")

    # Seção visual do portfólio usando expanders para não poluir]
    with st.expander("📊 PAINEL DE FROTAS", expanded=True):
        st.write("Visão completa da sua operação em tempo real com indicadores Elite.")
        exibir_foto_vrs("painel.png", "Interface VRS - Gestão de Frotas")

    with st.expander("🔧 MANUTENÇÃO / HISTÓRICO"):
        st.write("Controle técnico total: Ordens de Serviço e histórico por veículo.")
        exibir_foto_vrs("oficina.png", "Interface VRS - Módulo Oficina")

    with st.expander("📦 CADASTRO DE PEÇAS"):
        st.write("Estoque inteligente com alertas de reposição e controle de custos.")
        exibir_foto_vrs("pecas.png", "Interface VRS - Gestão de Peças")

    st.write("##")
    # Download discreto para não roubar o foco da venda]
    botoes.download_instalador_vrs()

with col_venda:
    st.markdown("""
        <div style='background:#111; padding:30px; border-radius:20px; border:2px solid #00FF7F; box-shadow: 0 0 20px rgba(0, 255, 127, 0.1);'>
            <h3 style='text-align:center; margin-bottom:20px;'>💎 ATIVAÇÃO DE LICENÇA</h3>
    """, unsafe_allow_html=True)
    
    # 1. ESCOLHA DO PLANO]
    plano = st.selectbox("Selecione o limite de frota:", 
        ["Básico (50 Veículos) - R$ 99,99", "Júnior (100 Veículos) - R$ 149,99", "Sênior (500 Veículos) - R$ 299,99"])
    
    st.write("---")
    
    # 2. IDENTIFICAÇÃO (CPF OU CNPJ) - ÚTIL E DIRETO]
    tipo_cad = st.radio("Tipo de Cadastro:", ["Pessoa Física (CPF)", "Empresa (CNPJ)"], horizontal=True)
    
    nome = st.text_input("NOME COMPLETO OU RAZÃO SOCIAL:", placeholder="Ex: Vitor Ribeiro")
    
    label_doc = "CPF" if "Física" in tipo_cad else "CNPJ"
    documento = st.text_input(f"{label_doc}:", placeholder=f"Digite o seu {label_doc}")
    
    email = st.text_input("E-MAIL PARA ENVIO DA CHAVE:", placeholder="vrsolucoes@gmail.com")
    id_pc = st.text_input("ID DA MÁQUINA (VEJA NO INSTALADOR):", placeholder="Código exibido no seu PC")
    
    st.write("##")
    # Chama o botão de pagamento com a validação de todos os campos]
    botoes.exibir_navegacao_venda("FINALIZAR E PAGAR AGORA ✅", nome, email, id_pc)
    
    st.markdown("</div>", unsafe_allow_html=True)

# --- RODAPÉ COM ACESSO ADM ---
st.write("---")
col_footer, col_adm = st.columns([10, 1])
with col_footer:
    st.markdown("<p style='color:#444; font-size:12px;'>VRS SOLUÇÕES SISTEMAS © 2026 - TODOS OS DIREITOS RESERVADOS</p>", unsafe_allow_html=True)
with col_adm:
    # O seu escritório secreto voltou para o cantinho]
    botoes.exibir_acesso_secreto()