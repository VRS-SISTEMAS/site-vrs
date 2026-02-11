# =================================================================
# NOME DO SISTEMA: VR SOLUÇÕES Sistemas
# MÓDULO: escritorio.py (Central de Comando com Histórico)
# DESCRIÇÃO: Painel Administrativo para controle de vendas e chaves
# =================================================================
import streamlit as st
import seguranca # Importa a lógica de criptografia das chaves
import os
import json

def carregar_visitas():
    """Lê o contador de acessos do arquivo de texto"""
    if os.path.exists("visitas.txt"):
        with open("visitas.txt", "r") as f: return f.read()
    return "0"

def carregar_vendas():
    """Lê o histórico de vendas que o site salvou no formato JSON"""
    if os.path.exists("vendas_vrs.json"):
        with open("vendas_vrs.json", "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except:
                return []
    return []

def exibir_painel_vitor():
    """Função principal que desenha o Painel Administrativo do Vitor"""
    
    # Estilização exclusiva do título VRS no painel
    st.markdown("""<style>@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@700;900&display=swap'); .vrs-admin-title { font-family: 'Orbitron', sans-serif; background: linear-gradient(180deg, #FFFFFF 0%, #A9A9A9 50%, #4F4F4F 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-size: 50px; font-weight: 900; }</style>""", unsafe_allow_html=True)

    # --- SISTEMA DE LOGIN ---
    if not st.session_state.get('autenticado', False):
        st.markdown("<div class='vrs-admin-title'>VRS</div>", unsafe_allow_html=True)
        st.subheader("ACESSO RESTRITO - VR SOLUÇÕES")
        senha = st.text_input("CHAVE MESTRA:", type="password")
        
        if st.button("DESBLOQUEAR"):
            if senha == "Vitor123":
                st.session_state['autenticado'] = True
                st.rerun()
            else:
                st.error("ACESSO NEGADO: Chave Mestra Incorreta!")
                
    else:
        # --- PAINEL JÁ AUTENTICADO ---
        st.markdown("<div class='vrs-admin-title'>VRS</div>", unsafe_allow_html=True)
        
        with st.sidebar:
            st.markdown("### 🖥️ COMANDO")
            # Menu de navegação lateral
            opcao = st.radio("MENU:", ["📊 Dashboard", "💰 Vendas Reais", "🔑 Gerador Mestre"])
            
            st.write("---")
            if st.button("SAIR DO SISTEMA"): 
                st.session_state['autenticado'] = False
                st.rerun()

        # 1. ABA DASHBOARD: Visão geral de tráfego e vendas
        if opcao == "📊 Dashboard":
            vendas = carregar_vendas()
            visitas = carregar_visitas()
            
            c1, c2 = st.columns(2)
            c1.metric("VISITAS REAIS", visitas) # Exibe o dado coletado pelo site
            c2.metric("VENDAS TOTAIS", len(vendas))

        # 2. ABA VENDAS: Lista detalhada de quem comprou e pagou
        elif opcao == "💰 Vendas Reais":
            st.markdown("### 💰 Histórico de Vendas do Site")
            vendas = carregar_vendas()
            if vendas:
                # Exibe a tabela completa de clientes
                st.dataframe(vendas, use_container_width=True)
            else:
                st.info("Nenhuma venda registrada até o momento.")

        # 3. ABA GERADOR: Criação manual de licenças para brindes ou testes
        elif opcao == "🔑 Gerador Mestre":
            st.markdown("### 🔑 Gerador para Presentes (Sem Custo)")
            
            id_cli = st.text_input("ID DO HARDWARE (Obtido no App do cliente):")
            plano = st.selectbox("TIPO DE LICENÇA:", ["BÁSICO", "JÚNIOR 🚀", "SÊNIOR 💎"])
            
            if st.button("🔥 GERAR CHAVE AGORA"):
                if id_cli.strip():
                    try:
                        # Chama a função de segurança para criptografar o ID
                        # Garante que o ID esteja limpo e em letras maiúsculas
                        id_limpo = id_cli.strip().upper()
                        
                        # Gera a chave usando a lógica do módulo seguranca.py
                        chave = seguranca.gerar_chave_vrs(id_limpo, plano)
                        
                        st.success(f"Chave gerada com sucesso para o plano {plano}!")
                        st.code(chave) # Exibe a chave em uma caixa fácil de copiar
                    except Exception as e:
                        st.error(f"Erro ao gerar: {e}. Verifique se o arquivo seguranca.py está na pasta.")
                else:
                    st.warning("⚠️ Você precisa colar o ID do Hardware do cliente primeiro!")