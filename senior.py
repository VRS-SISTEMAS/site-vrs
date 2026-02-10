# =================================================================
# NOME DO SISTEMA: VR SOLUÇÕES Sistemas
# MARCA EXIBIDA: VRS Soluções (Pequeno no topo)
# MÓDULO: senior.py (Plano ELITE - Ilimitado)
# =================================================================
import streamlit as st
import seguranca

# Nome pequeno no topo como você pediu
st.markdown("<p style='font-size: 10px; color: gray;'>VRS Soluções</p>", unsafe_allow_html=True)

# Verificação de segurança para o Plano Máximo
if not seguranca.verificar_acesso():
    st.error("⚠️ SISTEMA BLOQUEADO - LICENÇA SÊNIOR NÃO ENCONTRADA")
    st.info("O Plano Sênior oferece gestão ilimitada e suporte VIP.")
    if st.button("Adquirir Plano Sênior"):
        st.session_state['pagina_ativa'] = 'pagamento'
        st.rerun()
    st.stop()

# --- ÁREA ELITE LIBERADA ---
st.title("💎 VRS ELITE - Gestão Ilimitada")

# Barra lateral com todos os recursos liberados
st.sidebar.success("✅ Licença Senior Ativa")
st.sidebar.title("Menu Completo")
opcao = st.sidebar.selectbox("Navegar por Módulos:", [
    "Painel de Frotas Geral", 
    "Controle de Oficina", 
    "Histórico de Manutenção",
    "Gestão de Estoque/Peças",
    "Relatórios Técnicos (PDF)",
    "Relatórios Financeiros",
    "Configurações da Unidade"
])

# No Sênior não tem trava de quantidade!
st.info("🚀 Você possui o Plano Ilimitado. Cadastre quantos veículos e peças forem necessários.")

if opcao == "Painel de Frotas Geral":
    st.subheader("🚛 Monitoramento Global da Frota")
    # Simulação de Dashboard pesado
    col1, col2, col3 = st.columns(3)
    col1.metric("Veículos Ativos", "145", "+12%")
    col2.metric("Em Manutenção", "8", "-2")
    col3.metric("Disponíveis", "137", "95%")
    
    st.write("### Lista de Veículos")
    st.table({
        "ID": [1, 2, 3],
        "Placa": ["VRS-2026", "XYZ-1234", "ABC-8888"],
        "Tipo": ["Caminhão Scania", "Empilhadeira", "Ônibus"],
        "Status": ["Disponível", "Oficina", "Disponível"]
    })

elif opcao == "Gestão de Estoque/Peças":
    st.subheader("📦 Inventário e Peças")
    # Módulo que o Junior e Básico não acessam com tanta facilidade
    st.write("Controle a entrada e saída de materiais da sua oficina.")
    if st.button("Lançar Nova Entrada de Estoque"):
        st.success("Módulo de estoque aberto!")

elif opcao == "Relatórios Técnicos (PDF)":
    st.subheader("📄 Centro de Relatórios")
    st.write("Gere laudos técnicos detalhados com a logomarca da sua empresa.")
    st.button("Exportar Histórico Completo em PDF")

# --- MENSAGEM DE SUPORTE VIP ---
st.sidebar.markdown("---")
st.sidebar.write("📞 **Suporte VIP VRS Soluções**")
st.sidebar.write("Tempo de resposta: < 1 hora")