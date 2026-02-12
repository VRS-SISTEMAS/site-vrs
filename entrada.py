# =================================================================
# NOME DO SISTEMA: VRS Soluções
# MÓDULO: entrada.py (DESIGN DE CARDS ELITE - 3 PÁGINAS)
# =================================================================
import streamlit as st
import sys
import os
import botoes

# Garante que o Python ache os módulos na pasta do Windows]
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Silenciador de erro para o VS Code]
try:
    import backend # type: ignore
    backend_ativo = True
except ImportError:
    backend_ativo = False

# 1. ESTÉTICA LUXO VRS
st.set_page_config(layout="wide", page_title="VRS Soluções - Sistemas Elite", page_icon="💎")
botoes.aplicar_estetica_vrs()

# Inicializa a etapa (0: Vitrine, 1: Checkout, 3: ADM)
if 'etapa' not in st.session_state:
    st.session_state['etapa'] = 0

# Estilização Extra para os Cards (idêntico à imagem enviada)
st.markdown("""
    <style>
        .card-plano {
            background: #111;
            border: 1px solid #333;
            border-radius: 20px;
            padding: 40px 20px;
            text-align: center;
            transition: 0.4s;
            min-height: 450px;
        }
        .card-plano:hover {
            border-color: #00FF7F;
            transform: translateY(-10px);
            box-shadow: 0 15px 30px rgba(0, 255, 127, 0.1);
        }
        .titulo-plano { font-size: 32px; font-weight: 900; letter-spacing: 2px; margin-bottom: 10px; }
        .preco-plano { font-size: 36px; color: #00FF7F; font-weight: 800; margin: 20px 0; }
        .recursos-plano { color: #888; font-size: 16px; line-height: 1.8; margin-bottom: 30px; }
    </style>
""", unsafe_allow_html=True)

# --- PÁGINA 1: VITRINE DE IMPACTO (CARDS 3D) ---
if st.session_state['etapa'] == 0:
    st.markdown("<h1 style='text-align:center; font-size:50px; letter-spacing:10px;'>VRS SOLUÇÕES</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#888; margin-top:-20px;'>SISTEMAS ELITE</p>", unsafe_allow_html=True)
    
    st.write("##")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(f"""
            <div class="card-plano">
                <div class="titulo-plano">BÁSICO 🚀</div>
                <div class="preco-plano">R$ 99,99</div>
                <div class="recursos-plano">
                    • Gestão de controle frota<br>
                    • Cadastro para 50 veículos<br>
                    • Serviço Inteligente
                </div>
            </div>
        """, unsafe_allow_html=True)
        if st.button("ASSINAR BÁSICO", key="btn_basico", use_container_width=True):
            st.session_state['plano'] = "Básico"
            st.session_state['etapa'] = 1
            st.rerun()

    with col2:
        st.markdown(f"""
            <div class="card-plano" style="border-color: #00FF7F; background: #0a0a0a;">
                <div class="titulo-plano">JÚNIOR 🚀</div>
                <div class="preco-plano">R$ 139,99</div>
                <div class="recursos-plano">
                    • Cadastro para 100 veículos<br>
                    • Histórico de manutenção<br>
                    • Relatórios em tempo real
                </div>
            </div>
        """, unsafe_allow_html=True)
        if st.button("ASSINAR JÚNIOR", key="btn_junior", use_container_width=True):
            st.session_state['plano'] = "Júnior"
            st.session_state['etapa'] = 1
            st.rerun()

    with col3:
        st.markdown(f"""
            <div class="card-plano">
                <div class="titulo-plano">SÊNIOR 💎</div>
                <div class="preco-plano">R$ 299,99</div>
                <div class="recursos-plano">
                    • Cadastro até 500 veículos<br>
                    • Controle de estoque<br>
                    • Relatórios técnicos em PDF
                </div>
            </div>
        """, unsafe_allow_html=True)
        if st.button("ASSINAR SÊNIOR", key="btn_senior", use_container_width=True):
            st.session_state['plano'] = "Sênior"
            st.session_state['etapa'] = 1
            st.rerun()

# --- PÁGINA 2: CHECKOUT (CADASTRO E PAGAMENTO) ---
elif st.session_state['etapa'] == 1:
    st.markdown(f"## 💳 FINALIZAR ASSINATURA: <span style='color:#00FF7F;'>{st.session_state.get('plano', '')}</span>", unsafe_allow_html=True)
    
    col_form, col_down = st.columns([2, 1])
    with col_form:
        tipo = st.radio("Tipo de Cadastro:", ["Pessoa Física (CPF)", "Empresa (CNPJ)"], horizontal=True)
        nome = st.text_input("NOME COMPLETO / RAZÃO SOCIAL:")
        doc = st.text_input(f"DIGITE SEU {tipo}:")
        email = st.text_input("E-MAIL PARA RECEBER A CHAVE:")
        id_pc = st.text_input("ID DA MÁQUINA (VEJA NO INSTALADOR):")
        
        st.write("---")
        botoes.exibir_navegacao_venda("PAGAR AGORA 🚀", nome, email, id_pc)
        
        if st.button("⬅️ VOLTAR PARA PLANOS"):
            st.session_state['etapa'] = 0
            st.rerun()
    with col_down:
        botoes.download_instalador_vrs()

# --- PÁGINA 3: ESCRITÓRIO ADM ---
elif st.session_state['etapa'] == 3:
    st.markdown("## 👨‍💼 ESCRITÓRIO VRS")
    if backend_ativo:
        st.write(f"Visitas: {backend.registrar_visita()}") # type: ignore
    if st.button("⬅️ SAIR"):
        st.session_state['etapa'] = 0
        st.rerun()

# RODAPÉ
st.write("---")
botoes.exibir_acesso_secreto()