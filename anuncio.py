# ==============================================================================
# NOME DO SISTEMA: VRS SOLUÇÕES - SISTEMAS
# MÓDULO: Vitrine Publicitária e Checkout MP (anuncio.py)
# OBJETIVO: Renderizar planos e processar pagamentos REAIS via Mercado Pago
# DESENVOLVEDOR: Iara & Vitor
# ==============================================================================
import streamlit as st
import mercadopago # Certifique-se de que o 'pip install mercadopago' foi feito

# --- CONFIGURAÇÃO MERCADO PAGO VRS ---
# Seu Access Token oficial que já estava integrado
SDK_MP = mercadopago.SDK("SEU_ACCESS_TOKEN_AQUI")

def criar_preferencia_pagamento(plano, preco, email_cliente):
    """
    Gera o link de pagamento oficial do Mercado Pago para o plano escolhido.
    """
    dados_preferencia = {
        "items": [
            {
                "title": f"VRS ELITE - Plano {plano}",
                "quantity": 1,
                "unit_price": float(preco),
            }
        ],
        "payer": {"email": email_cliente},
        "back_urls": {
            "success": "https://vrs-solucoes.streamlit.app",
            "failure": "https://vrs-solucoes.streamlit.app",
            "pending": "https://vrs-solucoes.streamlit.app"
        },
        "auto_return": "approved",
    }
    
    resultado = SDK_MP.preference().create(dados_preferencia)
    return resultado["response"]["init_point"]

def exibir_vitrine_vrs():
    """
    Vitrine de vendas e checkout integrado com Mercado Pago.
    """
    # Estilos CSS de alto padrão (Padrão Elite VRS)
    st.markdown("""
        <style>
        .titulo-vrs { text-align: center; color: white; font-size: 3.8rem !important; font-weight: 900; letter-spacing: -1px; margin-bottom: 0px; }
        .subtitulo-vrs { text-align: center; color: #00FF7F; font-size: 1.2rem; font-weight: 300; letter-spacing: 3px; margin-bottom: 30px; text-transform: uppercase; }
        .card-plano { background: linear-gradient(180deg, #111111 0%, #0a0a0a 100%); border: 1px solid #222; padding: 30px; border-radius: 25px; text-align: center; min-height: 480px; transition: 0.3s; }
        .card-popular { border: 2px solid #00FF7F !important; box-shadow: 0 0 20px rgba(0, 255, 127, 0.2); }
        .preco-vrs { color: #00FF7F; font-size: 2.5rem; font-weight: 800; margin: 10px 0; }
        .secao-pagamento { background: #0a0a0a; border: 2px solid #00FF7F; padding: 30px; border-radius: 20px; margin-top: 50px; }
        </style>
    """, unsafe_allow_html=True)

    if 'etapa' not in st.session_state:
        st.session_state.etapa = "vitrine"

    # --- TELA 1: VITRINE ---
    if st.session_state.etapa == "vitrine":
        st.markdown("<h1 class='titulo-vrs'>VRS SOLUÇÕES</h1>", unsafe_allow_html=True)
        st.markdown("<p class='subtitulo-vrs'>Evolução Digital em Gestão</p>", unsafe_allow_html=True)

        col1, col2, col3 = st.columns(3)
        planos = [
            {"nome": "Básico", "preco": 99.99, "suporte": "50 Veículos", "key": "b_vrs", "col": col1, "popular": False},
            {"nome": "Júnior", "preco": 149.99, "suporte": "100 Veículos", "key": "j_vrs", "col": col2, "popular": True},
            {"nome": "Sênior", "preco": 299.99, "suporte": "500 Veículos", "key": "s_vrs", "col": col3, "popular": False}
        ]

        for p in planos:
            with p["col"]:
                classe_extra = "card-popular" if p["popular"] else ""
                st.markdown(f"""
                    <div class='card-plano {classe_extra}'>
                        <h4 style='color: white;'>Plano {p["nome"]}</h4>
                        <div class='preco-vrs'>R$ {p['preco']}</div>
                        <div style='color: #888;'>Suporte para {p["suporte"]}</div>
                    </div>
                """, unsafe_allow_html=True)
                
                if st.button(f"COMPRAR {p['nome'].upper()} ⚡", key=p["key"], use_container_width=True):
                    st.session_state.plano_selecionado = p["nome"]
                    st.session_state.preco_selecionado = p["preco"]
                    st.session_state.etapa = "pagamento"
                    st.rerun()

    # --- TELA 2: PAGAMENTO MERCADO PAGO ---
    elif st.session_state.etapa == "pagamento":
        st.markdown("<div class='secao-pagamento'>", unsafe_allow_html=True)
        st.subheader(f"💎 Finalizar Compra: {st.session_state.plano_selecionado}")
        
        with st.form("form_vrs_mp"):
            nome = st.text_input("Nome Completo")
            email = st.text_input("E-mail para Licença")
            id_maquina = st.text_input("ID do Sistema (8 dígitos)", max_chars=8)
            
            if st.form_submit_button("GERAR LINK DE PAGAMENTO 💳"):
                if nome and email and len(id_maquina) == 8:
                    # Gera o link real do Mercado Pago
                    link_mp = criar_preferencia_pagamento(st.session_state.plano_selecionado, st.session_state.preco_selecionado, email)
                    st.success("✅ Link gerado com sucesso!")
                    st.link_button("🚀 PAGAR AGORA COM PIX/CARTÃO", link_mp, use_container_width=True)
                else:
                    st.error("Por favor, preencha todos os dados corretamente.")

        if st.button("⬅ Voltar"):
            st.session_state.etapa = "vitrine"
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)