# =================================================================
# NOME DO SISTEMA: VR SOLUÇÕES Sistemas
# MARCA EXIBIDA: VRS Soluções (Pequeno no topo)
# MÓDULO: basico.py (Software do Cliente - 30 Veículos)
# =================================================================
import streamlit as st
import seguranca

# Nome pequeno no topo como você pediu (VRS Soluções)
st.markdown("<p style='font-size: 10px; color: gray;'>VRS Soluções</p>", unsafe_allow_html=True)

# Verificação de segurança integrada
if not seguranca.verificar_acesso():
    st.error("⚠️ SISTEMA BLOQUEADO - LICENÇA BÁSICA NÃO ENCONTRADA")
    st.write("Seu ID: **PC-VITOR-01**") # Exemplo de ID
    st.info("Adquira sua licença de R$ 60,00 no site para liberar.")
    
    # Botão para facilitar a vida do cliente
    if st.button("Ir para Pagamento"):
        st.session_state['pagina_ativa'] = 'pagamento'
        st.rerun()
    st.stop()

# --- ÁREA LIBERADA PARA O PLANO BÁSICO ---
st.title("📊 Painel de Gestão - Plano Básico")
st.sidebar.title("Menu Elite")
opcao = st.sidebar.radio("Ir para:", ["Dashboard de Frota", "Cadastrar Veículo", "Relatórios Simples"])

# Configuração de limites do Plano Básico
LIMITE = 30
# Aqui futuramente faremos a contagem real no banco de dados vrs_solucoes.db
veiculos_cadastrados = 10 

if opcao == "Cadastrar Veículo":
    st.subheader("📝 Cadastro de Novos Veículos")
    if veiculos_cadastrados >= LIMITE:
        st.error(f"❌ Limite de {LIMITE} veículos atingido!")
        st.warning("Para cadastrar mais, você precisa do **Plano Júnior** (Até 100 veículos).")
        if st.button("Fazer Upgrade Agora"):
            st.session_state['pagina_ativa'] = 'junior'
            st.rerun()
    else:
        st.success(f"✅ Espaço disponível: Você ainda pode cadastrar {LIMITE - veiculos_cadastrados} veículos.")
        # Aqui entra o formulário de cadastro que já criamos
        with st.form("form_cadastro_basico"):
            placa = st.text_input("Placa do Veículo")
            modelo = st.selectbox("Tipo", ["Caminhão", "Carro", "Moto", "Empilhadeira"])
            enviar = st.form_submit_button("Salvar no Sistema")
            if enviar:
                st.write(f"Veículo {placa} registrado com sucesso!")

elif opcao == "Dashboard de Frota":
    st.subheader("📑 Monitoramento da Frota")
    st.info(f"Ocupação do Plano: {veiculos_cadastrados}/{LIMITE} veículos.")
    # Aqui exibiríamos a tabela vinda do banco_dados.py