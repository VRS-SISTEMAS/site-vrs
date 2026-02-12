# =================================================================
# NOME DO SISTEMA: VR SOLUÇÕES Sistemas
# MÓDULO: botoes.py (Funções Visuais e Downloads)
# =================================================================
import streamlit as st

def download_instalador_vrs():
    """
    Cria o botão de download do instalador do sistema VRS Soluções.
    """
    # URL do seu instalador (Google Drive, Dropbox, etc.)
    # Se você ainda não tem o link, pode deixar esse link de exemplo
    url_download = "https://seu-link-de-download-aqui.com/instalador_vrs.exe"
    
    st.markdown(f"""
        <a href="{url_download}" target="_blank" style="text-decoration: none;">
            <button style="
                width: 100%;
                height: 50px;
                background-color: #262626;
                color: #00c853;
                border: 1px solid #00c853;
                border-radius: 10px;
                font-weight: bold;
                cursor: pointer;
                margin-bottom: 20px;
            ">
                📥 BAIXAR INSTALADOR VRS SOLUÇÕES
            </button>
        </a>
    """, unsafe_allow_html=True)

# Nota: Verifique se o nome da função acima é exatamente 'download_instalador_vrs'