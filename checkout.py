# =================================================================
# NOME DO SISTEMA: VRS Soluções
# MÓDULO: checkout.py (VITRINE DE ELITE + ACESSO ADM RESTAURADO)
# =================================================================
import streamlit as st
import botoes 

# Configuração de layout de alto nível
st.set_page_config(layout="wide", page_title="VRS Soluções - Ativação Elite", page_icon="⚡")
botoes.aplicar_estetica_vrs()

# --- HEADER DE IMPACTO ---
st.markdown("<h1 style='text-align:center; font-size:65px; font-weight:900; margin-bottom:0; color:#00FF7F;'>VRS SOLUÇÕES</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#888; letter-spacing:10px; margin-top:-10px;'>O FUTURO DA GESTÃO AUTOMOTIVA</p>", unsafe_allow_html=True)

st.write("---")

# --- ÁREA DE VENDAS (ESQUERDA: PRODUTOS | DIREITA: CHECKOUT) ---
col_vitrine, col_venda = st.columns([1.4, 1])

with col_vitrine:
    st.markdown("### 🖥️ CONHEÇA SEU NOVO ECOSSISTEMA")
    
    # Seção visual do portfólio - Aqui o cliente vê o que está comprando]
    with st.expander("📊 PAINEL DE FROTAS", expanded=True):
        st.write("Controle cada detalhe da sua frota com indicadores inteligentes.")
        # 
        st.image("https://via.placeholder.com/800x400/111/00FF7F?text=PAINEL+DE+FROTAS+VRS", caption="Visualização de Frotas de Elite")

    with st.expander("🔧 EM MANUTENÇÃO / HISTÓRICO"):
        st.write("Acompanhe o status real das ordens de serviço e histórico completo.")
        # 
        st.image("https://via.placeholder.com/800x400/111/00FF7F?text=GESTAO+DE+OFICINA+VRS", caption="Gestão Técnica de Oficina")

    with st.expander("📦 CADASTRO DE PEÇAS"):
        st.write("Estoque inteligente com alertas de reposição e controle de custos.")
        # 
        st.image("https://via.placeholder.com/800x400/111/00FF7F?text=ESTOQUE+DE+PEÇAS+VRS", caption="Controle de Estoque Profissional")

    st.write("##")
    # Download discreto ao final da vitrine
    botoes.download_instalador_vrs()

with col_venda:
    st.markdown("""
        <div style='background:#111; padding:30px; border-radius:20px; border:2px solid #00FF7F;'>
            <h3 style='text-align:center; margin-bottom:20px;'>💎 ATIVAÇÃO DE LICENÇA</h3>
    """, unsafe_allow_html=True)
    
    # Seleção do Plano conforme os valores da VR Soluções]
    plano = st.selectbox("Plano de Veículos:", 
        ["Básico (50 Veículos) - R$ 99,99", "Júnior (100 Veículos) - R$ 149,99", "Sênior (500 Veículos) - R$ 299,99"])
    
    st.write("---")
    
    # Cadastro para Pessoa Física ou Jurídica]
    tipo_cad = st.radio("Selecione:", ["Pessoa Física (CPF)", "Empresa (CNPJ)"], horizontal=True)
    
    nome = st.text_input("NOME COMPLETO / RAZÃO SOCIAL:", placeholder="Ex: Vitor Ribeiro")
    
    label_doc = "CPF" if "Física" in tipo_cad else "CNPJ"
    documento = st.text_input(f"{label_doc}:", placeholder=f"Digite o seu {label_doc}")
    
    email = st.text_input("E-MAIL PARA ENVIO DA CHAVE:", placeholder="vrsolucoes@gmail.com")
    id_pc = st.text_input("ID DA MÁQUINA (VEJA NO INSTALADOR):", placeholder="Insira o código do seu PC")
    
    st.write("##")
    # Botão de pagamento que agora valida todos os campos]
    botoes.exibir_navegacao_venda("FINALIZAR E PAGAR AGORA ✅", nome, email, id_pc)
    
    st.markdown("</div>", unsafe_allow_html=True)

# --- RODAPÉ COM ACESSO ADM ---
st.write("---")
col_footer, col_adm = st.columns([10, 1])
with col_footer:
    st.markdown("<p style='color:#444; font-size:12px;'>VR SOLUÇÕES SISTEMAS © 2026 - TODOS OS DIREITOS RESERVADOS</p>", unsafe_allow_html=True)
with col_adm:
    # RESTAURADO: O seu escritório secreto voltou para o cantinho]
    botoes.exibir_acesso_secreto()