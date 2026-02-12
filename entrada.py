import streamlit as st
import botoes

st.set_page_config(layout="wide", page_title="VR Soluções - Ativação Elite")
botoes.aplicar_estetica_vrs()

st.markdown("<h1 style='text-align:center; font-family:Orbitron;'>VRS SOLUÇÕES</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#00e5ff;'>GESTÃO DE FROTAS E MANUTENÇÃO</p>", unsafe_allow_html=True)

# Estrutura baseada no que funcionava (image_ed460c.png)
st.markdown("### 👤 Passo 1: Seus Dados")
col1, col2 = st.columns(2)
with col1:
    nome = st.text_input("Nome Completo ou Razão Social:")
    tipo_doc = st.radio("Documento Principal:", ["CPF", "CNPJ"], horizontal=True)
with col2:
    doc = st.text_input(f"Digite seu {tipo_doc}:")
    whatsapp = st.text_input("WhatsApp com DDD:")

st.markdown("### 🚀 Passo 2: Escolha seu Plano")
# Valores corrigidos: 50, 100 e 500 veículos (image_e33320.png)
plano_escolhido = st.radio(
    "Selecione o limite de frota desejado:",
    ["BÁSICO (50 Veículos) - R$ 99,99", 
     "JÚNIOR (100 Veículos) - R$ 139,99", 
     "SÊNIOR (500 Veículos) - R$ 299,99"],
    horizontal=True
)

st.markdown("### 🔑 Passo 3: Identificação do PC")
id_maquina = st.text_input("ID da Máquina (exibido no instalador):", placeholder="Ex: B32163D3")

st.markdown("### 💰 Passo 4: Pagamento")
forma_pagto = st.radio("Forma de pagamento:", ["Pix (Ativação Automática ⚡)", "Cartão / Boleto"], horizontal=True)

st.write("---")

# Botão de ação que não dá erro fatal
if st.button("FINALIZAR E GERAR PAGAMENTO ✅", use_container_width=True):
    if nome and doc and id_maquina:
        # Aqui chamamos o link oficial que você já tem
        link_mp = "https://www.mercadopago.com.br/checkout/v1/payment/redirect/?preference-id=1840049752-16a7f804-585a-4e8c-9411-96860d5f850b"
        st.success(f"Tudo pronto, {nome.split()[0]}! Clique abaixo para concluir.")
        st.markdown(f'<a href="{link_mp}" target="_blank" style="text-decoration:none;"><div style="background-color:#00FF7F; color:#050a0e; padding:15px; text-align:center; border-radius:10px; font-weight:bold; font-size:20px;">PAGAR AGORA</div></a>', unsafe_allow_html=True)
    else:
        st.error("⚠️ Por favor, preencha todos os campos para continuar.")