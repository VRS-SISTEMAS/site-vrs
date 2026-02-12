# =================================================================
# NOME DO SISTEMA: VRS Soluções
# MÓDULO: checkout.py (VITRINE VISUAL + ESTRUTURA ELITE)
# =================================================================
import streamlit as st
import botoes 

# Configuração de layout cinematográfico para impressionar o cliente
st.set_page_config(layout="wide", page_title="VRS Soluções - Ativação Elite", page_icon="⚡")
botoes.aplicar_estetica_vrs()

# --- HEADER LUXUOSO ---
st.markdown("<h1 style='text-align:center; font-size:60px; font-weight:900; margin-bottom:0;'>VRS <span style='color:#00FF7F;'>SOLUÇÕES</span></h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#888; letter-spacing:8px; margin-top:-10px;'>O FUTURO DA GESTÃO AUTOMOTIVA</p>", unsafe_allow_html=True)

st.write("---")

# --- CORPO: VITRINE DE PRODUTO VS ATIVAÇÃO ---
col_vitrine, col_venda = st.columns([1.5, 1])

with col_vitrine:
    st.markdown("### 🖥️ CONHEÇA O SEU NOVO PAINEL")
    
    # Seção de Portfólio com abas para o cliente ver o que está comprando
    aba1, aba2, aba3 = st.tabs(["📊 PAINEL DE FROTAS", "🔧 OFICINA", "📦 PEÇAS"])
    
    with aba1:
        st.markdown("<p style='color:#00FF7F;'>Visão completa da sua operação em tempo real.</p>", unsafe_allow_html=True)
        # Substitua o link abaixo pela imagem real do seu Painel de Frotas
        st.image("https://via.placeholder.com/800x450/111/00FF7F?text=IMAGEM+PAINEL+DE+FROTAS", caption="Interface Luxo - Painel de Frotas")

    with aba2:
        st.markdown("<p style='color:#00FF7F;'>Gestão técnica e histórica de manutenções.</p>", unsafe_allow_html=True)
        # Substitua o link abaixo pela imagem real da Oficina/Histórico
        st.image("https://via.placeholder.com/800x450/111/00FF7F?text=IMAGEM+HISTORICO+GERAL+OFICINA", caption="Controle Total de Oficina")

    with aba3:
        st.markdown("<p style='color:#00FF7F;'>Inventário inteligente e controle de entrada/saída.</p>", unsafe_allow_html=True)
        # Substitua o link abaixo pela imagem real do Cadastro de Peças
        st.image("https://via.placeholder.com/800x450/111/00FF7F?text=IMAGEM+CADASTRO+DE+PEÇAS", caption="Gestão de Estoque VRS")

    st.write("##")
    # Download discreto ao final da vitrine
    botoes.download_instalador_vrs()

with col_venda:
    st.markdown("""
        <div style='background:#111; padding:25px; border-radius:20px; border:1px solid #222;'>
            <h3 style='text-align:center; margin-bottom:20px;'>💎 ATIVAÇÃO ELITE</h3>
    """, unsafe_allow_html=True)
    
    # 1. ESCOLHA DO PLANO
    plano = st.selectbox("Selecione sua categoria de frota:", 
        ["Básico (50 Veículos) - R$ 99,99", "Júnior (100 Veículos) - R$ 149,99", "Sênior (500 Veículos) - R$ 299,99"])
    
    st.write("---")
    
    # 2. IDENTIFICAÇÃO INCLUSIVA (CPF OU CNPJ)
    tipo_cad = st.radio("Tipo de Cadastro:", ["Pessoa Física (CPF)", "Empresa (CNPJ)"], horizontal=True)
    
    nome = st.text_input("NOME / RAZÃO SOCIAL:", placeholder="Digite o nome completo")
    label_doc = "CPF" if "Física" in tipo_cad else "CNPJ"
    documento = st.text_input(f"{label_doc}:", placeholder=f"Digite seu {label_doc}")
    
    email = st.text_input("E-MAIL PARA ENVIO DA CHAVE:", placeholder="seuemail@exemplo.com")
    id_pc = st.text_input("ID DA MÁQUINA:", placeholder="Pegue no instalador ao lado")
    
    st.write("##")
    # Chama o botão de pagamento com validação completa
    botoes.exibir_navegacao_venda("EFETUAR PAGAMENTO 🚀", nome, email, id_pc)
    
    st.markdown("</div>", unsafe_allow_html=True)

# --- RODAPÉ ---
st.write("##")
st.markdown("<p style='text-align:center; color:#333; font-size:12px;'>VR SOLUÇÕES SISTEMAS © 2026 - TODOS OS DIREITOS RESERVADOS</p>", unsafe_allow_html=True)