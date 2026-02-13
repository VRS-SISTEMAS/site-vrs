import streamlit as st
import anuncio
import pagamento

st.set_page_config(page_title="VRS Soluções", layout="wide")

# Limpa a memória para garantir que o site comece do zero
if "plano_selecionado" not in st.session_state:
    st.session_state.plano_selecionado = None

# Sidebar simples
st.sidebar.title("VRS Soluções")
if st.sidebar.button("Reiniciar Site"):
    st.session_state.plano_selecionado = None
    st.rerun()

# LÓGICA DE EXIBIÇÃO: Ou mostra o Anúncio, ou mostra o Formulário. NUNCA OS DOIS.
if st.session_state.plano_selecionado is None:
    anuncio.exibir_vitrine_vrs()
else:
    if st.button("⬅️ Voltar"):
        st.session_state.plano_selecionado = None
        st.rerun()
    
    # Formulário de Ativação (Só aparece após clicar no plano)
    c1, c2, c3 = st.columns([1, 2, 1])
    with c2:
        st.info(f"Plano Escolhido: {st.session_state.plano_selecionado}")
        with st.container(border=True):
            nome = st.text_input("NOME / RAZÃO SOCIAL:")
            id_pc = st.text_input("ID DA MÁQUINA:")
            if st.button("GERAR PAGAMENTO AGORA"):
                if nome and id_pc:
                    # Chamar sua lógica de Pix aqui
                    st.success("Processando...")
                else:
                    st.error("Preencha os dados!")