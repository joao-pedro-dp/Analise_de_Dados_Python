# 🎌 Análise de Animes - MyAnimeList
Este repositório contém uma aplicação interativa desenvolvida com Streamlit para analisar e visualizar dados de animes extraídos do MyAnimeList. A aplicação utiliza um conjunto de dados abrangendo animes lançados de 1917 a 2024, permitindo a exploração de diversas informações, como avaliações, gêneros, estúdios de produção, número de episódios e tendências ao longo do tempo.

# 🌐 Visualização do Dashboard
🔗 Acesse o dashboard interativo clicando no link abaixo:

[Dashboard](https://primeirodashempythonjp.streamlit.app/)

## 📊 Funcionalidades
A aplicação responde a várias perguntas e apresenta os resultados em gráficos interativos:

✅ Anime mais bem avaliado: Exibe o anime com a maior avaliação de todos os tempos.

✅ Quantidade de animes por ano: Mostra a evolução do número de animes lançados anualmente.

✅ Gênero mais frequente: Identifica o gênero de anime mais comum no banco de dados.

✅ Top 5 animes com mais episódios: Apresenta os cinco animes com o maior número de episódios.

✅ Média de avaliação por gênero: Mostra a nota média de cada gênero.

✅ Estúdios que mais produziram animes: Lista os cinco estúdios mais produtivos.

✅ Relação entre avaliação e número de episódios: Analisa como a quantidade de episódios afeta a avaliação.

✅ Animes mais populares por década: Exibe a quantidade de animes lançados em cada década.

## 📦 Bibliotecas Utilizadas

Streamlit → Construção da interface interativa

Pandas → Manipulação e análise de dados

Plotly → Criação de gráficos interativos

Kaggle Hub → Download do dataset automaticamente

## ⚙️ Pré-requisitos

                pip install -r requirements.txt

## 🚀 Como Usar

1️⃣ Baixar os dados → O conjunto de dados é baixado automaticamente pelo Kaggle Hub.

2️⃣ Executar a aplicação → Após instalar as dependências, inicie o servidor Streamlit:


streamlit run Animes.py

🔹 Isso abrirá a aplicação automaticamente no seu navegador.

## 🛠️ Explicação do Código
📌 Carregamento e Limpeza dos Dados → Importação e pré-processamento dos dados, removendo colunas irrelevantes e ajustando o ano de lançamento para análises mais coerentes.

📌 Filtragem dos Dados → Interface permite filtrar os animes por ano e temporada, facilitando análises específicas.

📌 Cálculo das Métricas → Funções como groupby(), nlargest() e value_counts() processam os dados para responder às perguntas propostas.

📌 Gráficos Interativos → Criados com a biblioteca Plotly, permitindo uma experiência dinâmica e intuitiva.

📌 Exibição no Streamlit → O layout organiza os gráficos e informações em colunas para melhor visualização.

## 🤝 Contribuindo

Achou algum bug ou quer sugerir melhorias? Sinta-se à vontade para contribuir!

Faça um fork do repositório.

Implemente as melhorias.

Envie um Pull Request para revisão.

## ✨ Autor

Criado por João Pedro de Paula.
