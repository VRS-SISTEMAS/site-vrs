# =================================================================
# NOME DO SISTEMA: VR SOLUÇÕES Sistemas
# MARCA EXIBIDA: VRS Soluções (Pequeno no topo)
# MÓDULO: junior.py (Software do Cliente - 100 Veículos)
# =================================================================
import streamlit as st
import seguranca

# Nome pequeno no topo (VRS Soluções)
st.markdown("<p style='font-size: 10px; color: gray;'>VRS Soluções</p>", unsafe_allow_html=True)

# Verificação de acesso para o Plano Junior
if not seguranca.verificar_acesso():
    st.error("⚠️ SISTEMA BLOQUEADO - LICENÇA JÚNIOR NÃO ENCONTRADA")
    st.info("O Plano Júnior permite até 100 veículos e Relatórios Técnicos.")
    if st.button("Ver Opções de Pagamento"):
        st.session_state['pagina_ativa'] = 'pagamento'
        st.rerun()
    st.stop()

# --- ÁREA LIBERADA PARA O PLANO JÚNIOR ---
st.title("🚀 Painel de Gestão - Plano JÚNIOR")

st.sidebar.title("Menu Elite")
opcao = st.sidebar.radio("Navegação:", 
    ["Dashboard Frota", "Cadastrar Veículo", "Manutenção", "Relatórios Técnicos"]
)

# Configuração de limites do Plano Júnior
LIMITE_JUNIOR = 100
veiculos_cadastrados = 35 # Exemplo vindo do banco

if opcao == "Dashboard Frota":
    st.subheader("📊 Monitoramento de Frota (Até 100 veículos)")
    st.progress(veiculos_cadastrados / LIMITE_JUNIOR)
    st.write(f"Você está usando **{veiculos_cadastrados}%** da capacidade do seu plano.")

elif opcao == "Cadastrar Veículo":
    st.subheader("📝 Novo Cadastro")
    if veiculos_cadastrados >= LIMITE_JUNIOR:
        st.error(f"❌ Limite de {LIMITE_JUNIOR} veículos atingido!")
        st.warning("Precisa de mais? Migre para o **Plano Sênior** (Ilimitado).")
        if st.button("Falar com Suporte VRS"):
            st.session_state['pagina_ativa'] = 'senior'
            st.rerun()
    else:
        st.success(f"✅ Você ainda tem {LIMITE_JUNIOR - veiculos_cadastrados} vagas no sistema.")
        # Simulação de cadastro
        with st.form("cadastro_junior"):
            placa = st.text_input("Placa")
            tipo = st.selectbox("Categoria", ["Caminhão", "Carro", "Moto", "Empilhadeira", "Ônibus"])
            if st.form_submit_button("Registrar"):
                st.balloons()
                st.success(f"Veículo {placa} cadastrado!")

elif opcao == "Relatórios Técnicos":
    st.subheader("📄 Geração de Documentos Profissionais")
    st.write("Selecione o veículo para gerar o laudo em PDF:")
    st.selectbox("Selecionar Veículo", ["ABC-1234", "VRS-2026", "GTR-9999"])
    if st.button("Gerar PDF"):
        st.success("Gerando relatório com a marca VRS Soluções... ⏳")
        # Aqui chamaria o código do fpdf que usamos antes

elif opcao == "Manutenção":
    st.subheader("🔧 Controle de Oficina")
    st.write("Registro de Manutenções Corretivas e Preventivas.")
    # Lógica de manutenção