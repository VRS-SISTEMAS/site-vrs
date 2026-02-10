# =================================================================
# NOME DO SISTEMA: VR SOLUÇÕES Sistemas
# MÓDULO: sucesso.py (Versão Refinada Elite)
# =================================================================
import streamlit as st
import botoes  # Nossa fábrica de botões

# --- ESTILO CSS PREMIUM (PADRÃO VRS ELITE) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; }

    .success-box {
        background: linear-gradient(145deg, #1e1e1e, #141414);
        padding: 40px;
        border-radius: 25px;
        border: 1px solid #00c853;
        box-shadow: 0px 15px 40px rgba(0, 200, 83, 0.1);
        text-align: center;
    }

    .download-text {
        color: #888;
        font-size: 14px;
        margin-bottom: 20px;
    }

    /* Estilo para o botão de download do Streamlit */
    .stDownloadButton>button {
        background: linear-gradient(90deg, #00c853, #00a443) !important;
        color: white !important;
        font-weight: bold !important;
        border: none !important;
        padding: 15px !important;
        border-radius: 12px !important;
        font-size: 18px !important;
        transition: transform 0.3s ease !important;
    }

    .stDownloadButton>button:hover {
        transform: scale(1.05) !important;
        box-shadow: 0px 5px 15px rgba(0, 200, 83, 0.3) !important;
    }
</style>
""", unsafe_allow_html=True)

# 1. Identidade e Ajuste de Altura
botoes.marca_topo()
botoes.dar_espaco(3)

# 2. Comemoração Visual
st.balloons()

# 3. Título de Sucesso
st.markdown("""
    <div style='text-align: center;'>
        <h1 style='font-size: 45px; margin-bottom: 0; color: #00c853;'>PAGAMENTO <span style='color:#fff'>CONFIRMADO</span></h1>
        <p style='color: gray; font-size: 20px;'>Seja bem-vindo à elite da gestão de frotas.</p>
    </div>
""", unsafe_allow_html=True)

botoes.dar_espaco(2)

# 4. Área de Download Premium
col1, col_centro, col2 = st.columns([1, 2, 1])

with col_centro:
    st.markdown('<div class="success-box">', unsafe_allow_html=True)
    st.markdown("<h3 style='color: white;'>Pronto para começar?</h3>", unsafe_allow_html=True)
    st.markdown("<p class='download-text'>O instalador do seu sistema VRS Elite está pronto para ser baixado no seu computador Windows.</p>", unsafe_allow_html=True)
    
    # Tentativa de Download Real
    try:
        with open("Gestao_VRS_Solucoes.exe", "rb") as file:
            st.download_button(
                label="📥 BAIXAR INSTALADOR AGORA",
                data=file,
                file_name="Gestao_VRS_Solucoes.exe",
                mime="application/octet-stream",
                use_container_width=True
            )
    except FileNotFoundError:
        st.error("⚠️ Arquivo 'Gestao_VRS_Solucoes.exe' não encontrado.")
        st.info("Vitor, coloque o arquivo do programa nesta pasta para o botão funcionar.")
    
    st.markdown("<p style='font-size: 10px; color: #444; margin-top: 15px;'>Versão 1.0.0 | Suporta Windows 7, 10 e 11</p>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# 5. BARRA DE NAVEGAÇÃO FINAL
botoes.dar_espaco(3)
botoes.barra_navegacao(pagina_anterior="home", pagina_proxima=None)

st.markdown("---")
st.markdown("<p style='text-align: center; color: #444; font-size: 12px;'>VR Soluções - Tecnologia em Gestão Automotiva © 2026</p>", unsafe_allow_html=True)