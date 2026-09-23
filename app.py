import streamlit as st
from scrapegraphai.graphs import SmartScraperGraph

st.set_page_config(
    page_title="Web Scraping AI",
    page_icon="🕷️",
    layout="wide"
)

graph_config = {
    "llm": {
        "model": "ollama/llama3.2",
        "temperature": 0,
        "format": "json",
        "base_url": "http://localhost:11434",
    },
    "embeddings": {
        "model": "ollama/nomic-embed-text",
        "base_url": "http://localhost:11434",
    },
    "verbose": True,
}

st.markdown("""
<style>
.main {
    background-color: #f8f9fb;
}
.hero {
    padding: 100px 20px 70px 20px;
    text-align: center;
}
.hero h1 {
    font-size: 56px;
    font-weight: 700;
    margin-bottom: 15px;
}
.hero p {
    font-size: 20px;
    color: #666;
    max-width: 650px;
    margin: auto;
}
.card {
    padding: 25px;
    border-radius: 15px;
    background: white;
    border: 1px solid #e6e6e6;
    height: 100%;
}
.number {
    font-size: 14px;
    color: #888;
}
</style>
""", unsafe_allow_html=True)

if "page" not in st.session_state:
    st.session_state.page = "home"

if st.session_state.page == "home":

    st.markdown("""
    <div class="hero">
        <h1>Web Scraping AI 🕷️</h1>
        <p>Informe uma página, descreva o que você procura e deixe o agente extrair os dados para você.</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div class="card">
            <div class="number">01</div>
            <h4>Informe a URL</h4>
            <p>Cole o endereço da página que deseja analisar.</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="card">
            <div class="number">02</div>
            <h4>Descreva o objetivo</h4>
            <p>Diga em linguagem natural o que quer encontrar.</p>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div class="card">
            <div class="number">03</div>
            <h4>Receba o resultado</h4>
            <p>Os dados voltam estruturados em JSON.</p>
        </div>
        """, unsafe_allow_html=True)

    st.write("")
    _, center, _ = st.columns([1, 1, 1])
    with center:
        if st.button("Começar", type="primary", use_container_width=True):
            st.session_state.page = "scraper"
            st.rerun()

else:

    if st.button("← Voltar"):
        st.session_state.page = "home"
        st.rerun()

    st.title("Web Scraping AI 🕷️")
    st.caption("Informe uma página e diga ao agente o que você deseja encontrar.")

    url = st.text_input("URL", placeholder="https://exemplo.com")

    user_prompt = st.text_area(
        "O que você deseja encontrar?",
        placeholder="Ex: Encontre todos os produtos e seus respectivos preços.",
        height=120
    )

    if st.button("🔎 Executar agente", type="primary", use_container_width=True):

        if not url or not user_prompt:
            st.warning("Informe a URL e o que deseja encontrar.")

        else:
            try:
                with st.spinner("Analisando a página..."):
                    smart_scraper_graph = SmartScraperGraph(
                        prompt=user_prompt,
                        source=url,
                        config=graph_config
                    )
                    result = smart_scraper_graph.run()

                st.success("Análise concluída!")
                st.subheader("Resultado")
                st.json(result)

            except Exception as e:
                st.error(f"Erro ao executar o agente: {e}")