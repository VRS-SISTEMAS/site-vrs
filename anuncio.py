# ==============================================================================
# NOME DO SISTEMA: VRS SOLUÇÕES - SISTEMAS
# MÓDULO: Vitrine Publicitária e Checkout MP (anuncio.py)
# OBJETIVO: Renderizar planos, anúncios e processar pagamentos via Mercado Pago
# DESENVOLVEDOR: Iara & Vitor
# ==============================================================================
import streamlit as st
import mercadopago

# --- CONFIGURAÇÃO MERCADO PAGO VRS ---
# Mantenha o seu Access Token oficial para validar as transações
SDK_MP = mercadopago.SDK("SEU_ACCESS_TOKEN_AQUI")

def criar_preferencia_pagamento(plano, preco, email_cliente, nome_cliente):
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
        "payer": {
            "name": nome_cliente,
            "email": email_cliente
        },
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
    Renderiza a vitrine de planos com anúncios completos e checkout integrado.
    """
    # Estilos CSS de alto padrão para a vitrine (Padrão Elite VRS)
    st.markdown("""
        <style>
        .titulo-vrs { text-align: center; color: white; font-size: 3.8rem !important; font-weight: 900; letter-spacing: -1px; margin-bottom: 0px; }
        .subtitulo-vrs { text-align: center; color: #00FF7F; font-size: 1.2rem; font-weight: 300; letter-spacing: 3px; margin-bottom: 30px; text-transform: uppercase; }
        
        .container-nome-programa {
            background: rgba(0, 255, 127, 0.05);
            border: 1px solid rgba(0, 255, 127, 0.3);
            padding: 20px; border-radius: 15px; text-align: center; margin-bottom: 40px;
        }
        .nome-programa { color: #00FF7F; font-size: 2.2rem; font-weight: 800; margin: 0; text-shadow: 0 0 10px rgba(0, 255, 127, 0.5); }

        .card-plano {
            background: linear-gradient(180deg, #111111 0%, #0a0a0a 100%);
            border: 1px solid #222; padding: 30px; border-radius: 25px; 
            text-align: center; min-height: 480px; transition: 0.3s;
        }
        .card-plano:hover { border-color: #00FF7F; transform: translateY(-5px); }
        .card-popular { border: 2px solid #00FF7F !important; box-shadow: 0 0 20px rgba(0, 255, 127, 0.2); }
        
        .preco-vrs { color: #00FF7F; font-size: 2.5rem; font-weight: 800; margin: 10px 0; }
        .texto-suporte { color: #888; font-size: 1.1rem; margin-bottom: 20px; line-height: 1.2; }
        .lista-recursos { text-align: left; color: #ccc; font-size: 0.95rem; line-height: 2; margin-top: 20px; }
        .item-check { color: #00FF7F; font-weight: bold; margin-right: 10px; }

        .download-section {
            background: #1A1D2E; border: 1px dashed #00FF7F;
            padding: 25px; border-radius: 15px; text-align: center; margin-top: 40px;
        }
        
        .container-beneficios {
            background: #050505;
            padding: 40px; border-radius: 25px; margin-top: 60px;
            border: 1px solid #111; border-top: 4px solid #00FF7F;
        }
        .beneficio-item { color: #aaa; font-size: 1.1rem; margin-bottom: 15px; display: flex; align-items: center; }

        .secao-pagamento {
            background: #0a0a0a; border: 2px solid #00FF7F;
            padding: 30px; border-radius: 20px; margin-top: 50px;
        }
        </style>
    """, unsafe_allow_html=True)

    # Identificação da marca no topo
    st.markdown("<h1 class='titulo-vrs'>VRS SOLUÇÕES</h1>", unsafe_allow_html=True)
    st.markdown("<p class='subtitulo-vrs'>Evolução Digital em Gestão</p>", unsafe_allow_html=True)

    if 'etapa' not in st.session_state:
        st.session_state.etapa = "vitrine"

    # --- FLUXO DA VITRINE E ANÚNCIOS ---
    if st.session_state.etapa == "vitrine":
        st.markdown("""
            <div class='container-nome-programa'>
                <p style='color: #888; font-size: 0.9rem; margin-bottom: 5px;'>SOFTWARE EXCLUSIVO:</p>
                <h2 class='nome-programa'>GERENCIADOR PARA OFICINA</h2>
            </div>
        """, unsafe_allow_html=True)

        # Botão de Download Direto
        st.markdown("<div class='download-section'>", unsafe_allow_html=True)
        st.write("### 📥 Já possui uma licença ou quer testar?")
        url_download = "https://drive.google.com/file/d/1vUmS8hrQGZhR8mdR4PFtkDmZsEEX4jHM/view?usp=sharing" 
        st.link_button("🚀 BAIXAR INSTALADOR VRS ELITE", url_download, use_container_width=True)
        st.markdown("</div><br>", unsafe_allow_html=True)

        # Anúncios Restaurados (Padrão CEO)
        st.write("### 🛠️ Controle total da sua manutenção")
        st.info("Registros Simplificados e sem burocracia. Controle da sua manutenção sem deixar você na mão. Registro de histórico de manutenção que te leva ao perfeito controle, com estoque inteligente integrado à oficina e relatório de inventário geral.")

        # Colunas de Planos
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
                        <h4 style='color: {"#00FF7F" if p["popular"] else "white"};'>Plano {p["nome"]}</h4>
                        <div class='preco-vrs'>R$ {p["preco"]}</div>
                        <div class='texto-suporte'>Suporte para {p["suporte"]}</div>
                        <hr style='border-color: #222;'>
                        <div class='lista-recursos'>
                            <div><span class='item-check'>✔</span> Gestão de Peças & Estoque</div>
                            <div><span class='item-check'>✔</span> Relatórios Técnicos PDF</div>
                            <div><span class='item-check'>✔</span> Suporte VRS Chat</div>
                        </div>
                    </div>
                """, unsafe_allow_html=True)
                st.markdown("<br>", unsafe_allow_html=True)
                
                if st.button(f"COMPRAR {p['nome'].upper()} ⚡", key=p["key"], use_container_width=True):
                    st.session_state.plano_selecionado = p["nome"]
                    st.session_state.preco_selecionado = p["preco"]
                    st.session_state.etapa = "pagamento"
                    st.rerun()

    # --- FLUXO DE PAGAMENTO COM TODOS OS CAMPOS (RESTAURADO) ---
    elif st.session_state.etapa == "pagamento":
        st.markdown("<div class='secao-pagamento'>", unsafe_allow_html=True)
        st.subheader(f"💎 Finalizar Compra: Plano {st.session_state.plano_selecionado}")
        
        with st.form("form_vrs_cadastro_completo"):
            # CAMPOS FUNDAMENTAIS PARA A GESTÃO VRS
            nome_cliente = st.text_input("Nome Completo / Razão Social")
            doc_cliente = st.text_input("CPF ou CNPJ")
            whatsapp_cliente = st.text_input("WhatsApp (DDD + Número)")
            email_cliente = st.text_input("E-mail para recebimento da chave")
            id_maquina = st.text_input("ID do seu Sistema (8 dígitos)", max_chars=8)
            
            st.markdown("---")
            if st.form_submit_button("GERAR LINK DE PAGAMENTO 💳"):
                if nome_cliente and doc_cliente and whatsapp_cliente and email_cliente and len(id_maquina) == 8:
                    # Gera a preferência real no Mercado Pago
                    link_mp = criar_preferencia_pagamento(st.session_state.plano_selecionado, st.session_state.preco_selecionado, email_cliente, nome_cliente)
                    st.success(f"✅ Cadastro de {nome_cliente} realizado! Siga para o pagamento.")
                    st.link_button("🚀 PAGAR AGORA NO MERCADO PAGO", link_mp, use_container_width=True)
                else:
                    st.error("Por favor, preencha todos os campos obrigatórios (Nome, CPF/CNPJ, WhatsApp, E-mail e ID).")

        if st.button("⬅ Voltar para Planos"):
            st.session_state.etapa = "vitrine"
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

    # Benefícios (Rodapé)
    st.markdown("""
        <div class='container-beneficios'>
            <h2 style='color: white; margin-top: 0;'>🚀 Por que a VRS é a escolha da Elite?</h2>
            <div style='display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-top: 30px;'>
                <div class='beneficio-item'><span class='item-check'>✔</span> <b>Zero Papelada:</b> Digitalização total da sua oficina.</div>
                <div class='beneficio-item'><span class='item-check'>✔</span> <b>Histórico Instantâneo:</b> Tudo sobre o veículo em segundos.</div>
                <div class='beneficio-item'><span class='item-check'>✔</span> <b>Lucratividade:</b> Controle real de entradas e saídas.</div>
                <div class='beneficio-item'><span class='item-check'>✔</span> <b>Simplicidade:</b> Feito para quem foca no trabalho, não no PC.</div>
            </div>
        </div>
    """, unsafe_allow_html=True)