import streamlit as st
import os

def marca_topo():
    st.markdown("<p style='font-size: 10px; color: gray; margin-top: -40px;'>VRS Soluções</p>", unsafe_allow_html=True)

def dar_espaco(linhas=4):
    for _ in range(linhas):
        st.write("")

def barra_navegacao(pagina_anterior=None, pagina_proxima=None):
    st.write("---")
    col_voltar, col_meio, col_avancar = st.columns([1, 2, 1])
    with col_voltar:
        if pagina_anterior:
            # A key dinâmica evita que o botão trave
            if st.button("⬅️ VOLTAR", key=f"btn_voltar_{pagina_anterior}"):
                st.session_state['pagina_ativa'] = pagina_anterior
                st.rerun()
    with col_avancar:
        if pagina_proxima:
            if st.button("AVANÇAR ➡️", key=f"btn_avancar_{pagina_proxima}"):
                st.session_state['pagina_ativa'] = pagina_proxima
                st.rerun()

# --- NOVA FUNÇÃO INTEGRADA PARA A VR SOLUÇÕES ---
def download_instalador_vrs():
    """Gerencia a busca e o download do executável na página de checkout"""
    caminho_exe = "VR_Solucoes_Elite.exe"
    
    st.markdown("#### 📥 1. Baixe o Instalador")
    
    if os.path.exists(caminho_exe):
        with open(caminho_exe, "rb") as file:
            st.download_button(
                label="CLIQUE AQUI PARA BAIXAR (.EXE)",
                data=file,
                file_name="VR_Solucoes_Elite.exe",
                mime="application/octet-stream"
            )
    else:
        st.error("⚠️ O arquivo VR_Solucoes_Elite.exe não foi encontrado na pasta raiz.")