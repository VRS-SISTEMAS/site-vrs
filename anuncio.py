# ==============================================================================
# NOME DO SISTEMA: VRS SOLUÇÕES - SISTEMAS
# MÓDULO: Vitrine Publicitária (anuncio.py)
# OBJETIVO: Renderizar planos e fornecer link de download oficial
# DESENVOLVEDOR: Iara & Vitor
# ==============================================================================
import streamlit as st

def exibir_vitrine_vrs():
    """
    Renderiza a vitrine de planos com interface premium e link de download.
    """
    # Estilos CSS de alto padrão para a vitrine (Mantendo seu padrão Elite)
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

        .container-beneficios {
            background: #050505;
            padding: 40px; border-radius: 25px; margin-top: 60px;
            border: 1px solid #111; border-top: 4px solid #00FF7F;
        }
        .beneficio-item { color: #aaa; font-size: 1.1rem; margin-bottom: 15px; display: flex; align-items: center; }
        
        /* Estilo para a seção de download */
        .download-section {
            background: #1A1D2E; border: 1px dashed #00FF7F;
            padding: 25px; border-radius: 15px; text-align: center; margin-top: 40px;
        }
        </style>
    """, unsafe_allow_html=True)

    # Identificação da marca no topo [cite: 2026-02-07]
    st.markdown("<h1 class='titulo-vrs'>VRS SOLUÇÕES</h1>", unsafe_allow_html=True)
    st.markdown("<p class='subtitulo-vrs'>Evolução Digital em Gestão</p>", unsafe_allow_html=True)

    st.markdown("""
        <div class='container-nome-programa'>
            <p style='color: #888; font-size: 0.9rem; margin-bottom: 5px;'>SOFTWARE EXCLUSIVO:</p>
            <h2 class='nome-programa'>GERENCIADOR PARA OFICINA</h2>
        </div>
    """, unsafe_allow_html=True)

    # --- NOVO: BOTÃO DE DOWNLOAD DIRETO ---
    st.markdown("<div class='download-section'>", unsafe_allow_html=True)
    st.write("### 📥 Já possui uma licença ou quer testar?")
    # LINK DO GOOGLE DRIVE QUE VOCÊ GEROU
    url_download = "COLE_AQUI_O_LINK_DO_GOOGLE_DRIVE" 
    st.link_button("🚀 BAIXAR INSTALADOR VRS ELITE", url_download, use_container_width=True)
    st.markdown("</div><br>", unsafe_allow_html=True)

    # Definição das colunas para os cards
    col1, col2, col3 = st.columns(3)

    # Configuração dos planos disponíveis [cite: 2026-02-16]
    planos = [
        {"nome": "Básico", "preco": "99.99", "suporte": "50 Veículos", "key": "b_vrs", "col": col1, "popular": False},
        {"nome": "Júnior", "preco": "149.99", "suporte": "100 Veículos", "key": "j_vrs", "col": col2, "popular": True},
        {"nome": "Sênior", "preco": "299.99", "suporte": "500 Veículos", "key": "s_vrs", "col": col3, "popular": False}
    ]

    for p in planos:
        with p["col"]:
            classe_extra = "card-popular" if p["popular"] else ""
            st.markdown(f"""
                <div class='card-plano {classe_extra}'>
                    <h4 style='color: {"#00FF7F" if p["popular"] else "white"}; margin-bottom: 0;'>Plano {p["nome"]}</h4>
                    <div class='preco-vrs'>R$ {p["preco"]}</div>
                    <div class='texto-suporte'>Com suporte para {p["suporte"]}</div>
                    <hr style='border-color: #222;'>
                    <div class='lista-recursos'>
                        <div><span class='item-check'>✔</span> Gestão de Peças & Estoque</div>
                        <div><span class='item-check'>✔</span> Relatórios Técnicos PDF</div>
                        <div><span class='item-check'>✔</span> Suporte VRS Chat</div>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            st.markdown("<br>", unsafe_allow_html=True)
            
            # Ação do botão: Inicia o processo de ativação [cite: 2026-02-16]
            if st.button(f"COMPRAR {p['nome'].upper()} 💎", key=p["key"], use_container_width=True):
                st.session_state.plano_selecionado = p["nome"]
                st.session_state.etapa = "checkout" # Direciona para o pagamento
                st.rerun()

    # Seção informativa de benefícios
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