# 🕷️ Web Scraping com IA

Projeto base para raspagem de dados de páginas web utilizando um modelo de inteligência artificial local, com uma interface interativa desenvolvida em Streamlit.

## 🚀 Sobre o projeto

A aplicação permite informar uma URL e descrever quais informações devem ser extraídas da página. A raspagem é realizada utilizando inteligência artificial local através do Ollama e do ScrapeGraphAI.

O objetivo é explorar o uso de modelos de IA para automatizar processos de coleta e extração de informações na web.

## 🛠️ Tecnologias

* 🐍 Python
* 🎈 Streamlit
* 🤖 Ollama
* 🧠 Llama 3.2
* 🔎 ScrapeGraphAI
* 📊 Nomic Embed Text

## 📋 Requisitos

Antes de executar o projeto, é necessário ter instalado:

* Python
* Ollama

Também é necessário baixar os modelos utilizados:

```bash
ollama pull llama3.2
ollama pull nomic-embed-text
```

## ⚙️ Instalação

Clone o repositório:

```bash
git clone https://github.com/analusz/webScrapingAi.git
cd webScrapingAi
```

Crie o ambiente virtual:

```bash
python -m venv .venv
```

Ative o ambiente virtual no Windows:

```powershell
.venv\Scripts\Activate.ps1
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

## ▶️ Executando

Com o ambiente virtual ativado, execute:

```bash
streamlit run app.py
```

A aplicação será aberta no navegador.

## 💡 Como utilizar

1. Informe a URL da página que deseja analisar.
2. Descreva quais informações deseja extrair.
3. Clique em **Scrape**.
4. A IA processará a página e retornará os dados solicitados.

## 📁 Estrutura do projeto

```text
Scraping com ia/
├── .venv/
├── .gitignore
├── app.py
├── README.md
└── requirements.txt
```

> A pasta `.venv` é utilizada apenas localmente e não é enviada para o GitHub.

## 📌 Próximos passos

* Melhorar a interface da aplicação
* Adicionar diferentes formatos de saída
* Permitir exportação dos dados coletados
* Melhorar o tratamento de erros
* Explorar diferentes modelos de IA locais

---

Desenvolvido com 🐍 Python, 🤖 IA e ☕ curiosidade.
