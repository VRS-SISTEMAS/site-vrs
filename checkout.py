# =================================================================
# NOME DO SISTEMA: VRS Soluções
# MÓDULO: checkout.py (VITRINE COMPLETA E INCLUSIVA)
# =================================================================
import streamlit as st
import botoes 

# Configuração de página larga para visual cinematográfico
st.set_page_config(layout="wide", page_title="VRS Soluções - Ativação Elite", page_icon="⚡")
botoes.aplicar_estetica_vrs()

# --- TOPO: TÍTULO COM DESIGN ---
st.markdown("<h1 style='text-align:center; font-size:55px; font-weight:900; color:#FFFFFF;'>VRS <span style='color:#00FF7F;'>SOLUÇÕES</span></h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#888; margin-top:-20px; letter-spacing:5px;'>O PODER DA GESTÃO EM SUAS MÃOS</p>", unsafe_allow_html=True)

st.write("##")

# --- CORPO: DIVISÃO EM COLUNAS ---
col_info, col_venda = st.columns([1.2, 1])

with col_info:
    st.markdown("""
        <div style='background:#111; padding:30px; border-radius:20px; border:1px solid #222;'>
            <h3 style='color:#00FF7F;'>🚀 Por que escolher a VRS?</h3>
            <p style='color:#ccc;'>Sistema projetado para maximizar o lucro de oficinas e frotas de todos os tamanhos.</p>
            <hr style='border: 0.5px solid #222;'>
            <p>✅ <b>Gestão Completa:</b> OS, Estoque e Peças.</p>
            <p>✅ <b>Relatórios:</b> PDF técnicos e gerenciais.</p>
            <p>✅ <b>Suporte:</b> Atendimento prioritário Elite.</p>
        </div>
    """, unsafe_allow_html=True)
    st.write("##")
    # Área de Download integrada na coluna de informações
    botoes.download_instalador_vrs()

with col_venda:
    st.markdown("### 💳 ATIVAÇÃO DE LICENÇA")
    
    # 1. ESCOLHA DO PLANO
    plano = st.selectbox("Selecione sua categoria:", 
        ["Básico (50 Veículos) - R$ 99,99", "Júnior (100 Veículos) - R$ 149,99", "Sênior (500 Veículos) - R$ 299,99"])
    
    # 2. IDENTIFICAÇÃO DO CLIENTE (CPF ou CNPJ)
    st.write("---")
    tipo_pessoa = st.radio("Tipo de Cadastro:", ["Pessoa Física (CPF)", "Empresa (CNPJ)"], horizontal=True)
    
    nome = st.text_input("NOME COMPLETO OU RAZÃO SOCIAL:", placeholder="Ex: Vitor Ribeiro")
    doc_label = "CPF" if "Física" in tipo_pessoa else "CNPJ"
    documento = st.text_input(f"{doc_label}:", placeholder=f"Digite seu {doc_label}")
    
    email = st.text_input("E-MAIL PARA RECEBER A CHAVE:", placeholder="vrsolucoes@exemplo.com")
    id_pc = st.text_input("ID DA MÁQUINA:", placeholder="Pegue este ID no instalador acima")
    
    st.write("##")
    # Chama o botão de pagamento com a validação de todos os campos
    botoes.exibir_navegacao_venda("EFETUAR PAGAMENTO 💎", nome, email, id_pc)

# --- RODAPÉ ---
st.write("##")
st.markdown("<p style='text-align:center; color:#333; font-size:12px;'>VR SOLUÇÕES SISTEMAS © 2026 - TODOS OS DIREITOS RESERVADOS</p>", unsafe_allow_html=True)