# =================================================================
# NOME DO SISTEMA: VR SOLUÇÕES Sistemas
# MÓDULO: Vitrine e Ecossistema (anuncio.py)
# =================================================================
import streamlit as st

def exibir_vitrine_vrs():
    # Estilização para organizar o layout e limpar o fundo
    st.markdown("""
        <style>
        .bloco-vrs {
            background-color: #1e1e1e;
            padding: 15px;
            border-radius: 10px;
            border-left: 5px solid #00c853;
            margin-bottom: 15px;
            min-height: 100px;
        }
        .titulo-secao { color: #00c853; font-weight: bold; font-size: 1.2rem; margin-bottom: 5px; }
        .texto-corpo { color: #ddd; font-size: 0.95rem; }
        </style>
    """, unsafe_allow_html=True)

    # Título Principal Centralizado
    st.markdown("<h1 style='text-align: center; color: #00c853; font-size: 3rem;'>VRS SOLUÇÕES</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; letter-spacing: 2px;'>O FUTURO DA GESTÃO AUTOMOTIVA</p>", unsafe_allow_html=True)
    st.divider()

    # Divisão em 2 colunas para parar de encavalar
    col_esquerda, col_direita = st.columns([1.2, 1])

    with col_esquerda:
        st.markdown("### 🖥️ CONHEÇA SEU NOVO ECOSSISTEMA")
        
        st.markdown("""
            <div class='bloco-vrs'>
                <div class='titulo-secao'>📊 PAINEL DE FROTAS</div>
                <div class='texto-corpo'>Visão completa da sua operação em tempo real com indicadores Elite de desempenho e status.</div>
            </div>
            
            <div class='bloco-vrs'>
                <div class='titulo-secao'>🛠️ MANUTENÇÃO / HISTÓRICO</div>
                <div class='texto-corpo'>Controle técnico total: Ordens de Serviço detalhadas e histórico completo por veículo da frota.</div>
            </div>
            
            <div class='bloco-vrs'>
                <div class='titulo-secao'>📦 CADASTRO DE PEÇAS</div>
                <div class='texto-corpo'>Gestão de estoque inteligente integrada para garantir que os itens essenciais nunca faltem.</div>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("---")
        st.link_button("📥 BAIXAR INSTALADOR AGORA", "https://vrsolucoes.com.br/download", use_container_width=True)

    with col_direita:
        with st.container(border=True):
            st.markdown("<h3 style='text-align: center;'>💎 ATIVAÇÃO DE LICENÇA</h3>", unsafe_allow_html=True)
            
            plano = st.selectbox("Selecione o limite de frota:", 
                                ["Básico (50 Veículos) - R$ 99,99", 
                                 "Júnior (100 Veículos) - R$ 149,99", 
                                 "Sênior (500 Veículos) - R$ 299,99"])
            
            tipo_cad = st.radio("Tipo de Cadastro:", ["CPF", "CNPJ"], horizontal=True)
            
            nome = st.text_input("NOME COMPLETO OU RAZÃO SOCIAL:")
            doc = st.text_input(f"DIGITE O {tipo_cad}:")
            email = st.text_input("E-MAIL PARA ENVIO DA CHAVE:")
            machine_id = st.text_input("ID DA MÁQUINA (VEJA NO INSTALADOR):")
            
            st.divider()
            
            if st.button("GERAR PIX PARA ATIVAÇÃO", use_container_width=True, type="primary"):
                if nome and email and doc and machine_id:
                    # Salva os dados na sessão para o index.py processar
                    st.session_state.plano_selecionado = plano
                    st.session_state.dados_usuario = {
                        "nome": nome,
                        "email": email,
                        "doc": doc,
                        "id_maquina": machine_id
                    }
                    st.rerun()
                else:
                    st.error("⚠️ Por favor, preencha todos os campos!")