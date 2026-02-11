# =================================================================
# NOME DO SISTEMA: VR SOLUÇÕES Sistemas
# MÓDULO: entrada.py (Versão High-End - Identidade Visual Restaurada)
# =================================================================
import streamlit as st
import botoes
import seguranca  # Sua lógica oficial de licenciamento
import pandas as pd
import datetime

# --- CONFIGURAÇÃO DA PÁGINA PARA OCUPAR A TELA TODA ---
st.set_page_config(layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
<style>
    /* Importando fonte moderna */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; overflow: hidden; }

    /* Nome da Empresa no Canto Superior - MAIOR */
    .vrs-header {
        position: absolute;
        top: -75px;
        left: 0;
        font-size: 18px;
        color: #00c853;
        font-weight: bold;
        letter-spacing: 3px;
        text-shadow: 0px 0px 10px rgba(0, 200, 83, 0.3);
    }

    /* Painel Compacto de Vantagens */
    .container-vantagens {
        background: linear-gradient(145deg, #161616, #0f0f0f);
        border-radius: 20px;
        padding: 20px 40px;
        border: 1px solid #222;
        margin-bottom: 20px;
        box-shadow: 0px 10px 30px rgba(0,0,0,0.5);
    }

    .box-beneficio {
        background: rgba(255, 255, 255, 0.02);
        border-radius: 12px;
        padding: 15px;
        border-left: 5px solid #00c853;
        height: 100%;
    }

    .item-lista {
        list-style: none;
        padding: 0;
        margin-top: 10px;
        color: #ccc;
        font-size: 14px;
    }
    .item-lista li { margin-bottom: 5px; }

    /* Cartões de Planos Compactos */
    .card-vrs {
        background: linear-gradient(145deg, #1e1e1e, #141414);
        border-radius: 15px;
        padding: 15px;
        border: 1px solid #333;
        text-align: center;
        transition: all 0.3s ease;
        height: 310px;
    }
    
    .card-vrs:hover {
        transform: translateY(-5px);
        border-color: #00c853;
    }

    .preco { font-size: 26px; font-weight: bold; color: #00c853; margin: 10px 0; }
    .detalhes { color: #888; font-size: 13px; line-height: 1.4; }
</style>
""", unsafe_allow_html=True)

if 'pagina_ativa' not in st.session_state:
    st.session_state['pagina_ativa'] = 'home'

def exibir_home():
    botoes.marca_topo()
    
    # Nome da Empresa MAIOR no Canto
    st.markdown("<div class='vrs-header'>VR SOLUÇÕES - SISTEMAS</div>", unsafe_allow_html=True)
    
    # PAINEL DE VANTAGENS COMPACTO
    st.markdown(f"""
    <div class="container-vantagens">
        <h2 style="font-size: 32px; margin: 0;">POR QUE OBTER <span style="color:#00c853">NOSSO PRODUTO?</span></h2>
        <p style="color: gray; font-size: 14px; margin-bottom: 15px;">A solução definitiva para quem busca performance e controle total.</p>
        <div style="display: flex; gap: 15px;">
            <div style="flex: 1;">
                <div class="box-beneficio">
                    <h4 style="color: white; margin:0; font-size: 18px;">Conectividade Digital</h4>
                    <ul class="item-lista">
                        <li>✅ Gestão de frotas</li>
                        <li>✅ Controle de manutenção</li>
                        <li>✅ Controle de Estoque</li>
                    </ul>
                </div>
            </div>
            <div style="flex: 1;">
                <div class="box-beneficio">
                    <h4 style="color: white; margin:0; font-size: 18px;">Comodidade e Fluidez</h4>
                    <ul class="item-lista">
                        <li>✅ Manutenção Correta</li>
                        <li>✅ Otimização de Tempo</li>
                        <li>✅ Relatório Detalhado</li>
                    </ul>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<h4 style='text-align: center; margin-bottom: 15px;'>Conheça os Planos <span style='color:#00c853'>VRS ELITE</span></h4>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
            <div class='card-vrs'>
                <h4 style='color: #888; margin:0;'>BÁSICO</h4>
                <div class='preco'>R$ 59,90</div>
                <hr style='border-color: #333; margin: 10px 0;'>
                <div class='detalhes'>
                    <p>✅ 30 Veículos</p>
                    <p>✅ Gestão de Frota</p>
                    <p>✅ Suporte via Chat</p>
                </div>
            </div>
        """, unsafe_allow_html=True)
        if st.button("ASSINAR BÁSICO", key="p1", use_container_width=True):
            st.session_state['plano_escolhido'] = 'Básico'
            st.session_state['pagina_ativa'] = 'checkout'
            st.rerun()

    with col2:
        st.markdown("""
            <div class='card-vrs' style='border-color: #00c853;'>
                <h4 style='color: #fff; margin:0;'>JÚNIOR 🚀</h4>
                <div class='preco'>R$ 99,90</div>
                <hr style='border-color: #333; margin: 10px 0;'>
                <div class='detalhes'>
                    <p>✅ 100 Veículos</p>
                    <p>✅ Módulo Oficina</p>
                    <p>✅ Relatórios PDF</p>
                </div>
            </div>
        """, unsafe_allow_html=True)
        if st.button("ASSINAR JÚNIOR", key="p2", use_container_width=True):
            st.session_state['plano_escolhido'] = 'Júnior'
            st.session_state['pagina_ativa'] = 'checkout'
            st.rerun()

    with col3:
        st.markdown("""
            <div class='card-vrs' style='border-color: #ffd700;'>
                <h4 style='color: #ffd700; margin:0;'>SÊNIOR 💎</h4>
                <div class='preco'>R$ 149,90</div>
                <hr style='border-color: #333; margin: 10px 0;'>
                <div class='detalhes'>
                    <p>✅ <b>ILIMITADO</b></p>
                    <p>✅ Gestão Financeira</p>
                    <p>✅ Suporte VIP 24h</p>
                </div>
            </div>
        """, unsafe_allow_html=True)
        if st.button("ASSINAR SÊNIOR", key="p3", use_container_width=True):
            st.session_state['plano_escolhido'] = 'Sênior'
            st.session_state['pagina_ativa'] = 'checkout'
            st.rerun()

    # --- ACESSO ADMINISTRATIVO DISCRETO ---
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🔐 Acesso Administrativo", key="btn_adm"):
        st.session_state['pagina_ativa'] = 'escritorio'
        st.rerun()

def exibir_escritorio():
    st.title("🏢 Administração VR Soluções")
    if 'autenticado' not in st.session_state: st.session_state['autenticado'] = False

    if not st.session_state['autenticado']:
        senha = st.text_input("Senha do Proprietário:", type="password") # Senha: Vitor123
        if st.button("Entrar no Painel"):
            if senha == "Vitor123":
                st.session_state['autenticado'] = True
                st.rerun()
            else: st.error("Acesso Negado!")
        if st.button("Voltar ao Site"):
            st.session_state['pagina_ativa'] = 'home'; st.rerun()
    else:
        st.success("Bem-vindo, Vitor!")
        # Integração com seu adm.py e seguranca.py
        st.markdown("### 🔑 Gerador de Licenças")
        col_id, col_pl = st.columns([2, 1])
        with col_id: id_cli = st.text_input("ID do Hardware:")
        with col_pl: plano_sel = st.selectbox("Plano:", ["BASICO", "JUNIOR", "SENIOR"])
        
        if st.button("GERAR CHAVE"):
            if id_cli:
                chave = seguranca.gerar_chave_final(id_cli.strip().upper(), plano_sel)
                st.code(chave)
            else: st.warning("Coloque o ID!")
        
        if st.button("Sair"):
            st.session_state['autenticado'] = False
            st.session_state['pagina_ativa'] = 'home'
            st.rerun()

# ROTEADOR
if st.session_state['pagina_ativa'] == 'home': exibir_home()
elif st.session_state['pagina_ativa'] == 'escritorio': exibir_escritorio()
elif st.session_state['pagina_ativa'] == 'checkout':
    try:
        with open("checkout.py", encoding="utf-8") as f: exec(f.read())
    except Exception as e: st.error(f"Erro: {e}")
elif st.session_state['pagina_ativa'] == 'sucesso':
    try:
        with open("sucesso.py", encoding="utf-8") as f: exec(f.read())
    except Exception as e: st.error(f"Erro: {e}")