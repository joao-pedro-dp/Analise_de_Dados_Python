''' Perguntas a Serem Respondidas:

1 - Qual é o anime mais bem avaliado na base de dados?
2 - Quantos animes foram lançados em cada ano?
3 - Qual o gênero de anime mais frequente na base de dados?
4 - Quais são os 5 animes com maior número de episódios?
5 - Qual é a média de avaliação para cada gênero de anime?
6 - Quais estúdios produziram mais animes?
7 - Existe uma relação entre a avaliação e o número de episódios dos animes?
8 - Quais são os animes mais populares de cada década?
'''

import kagglehub
import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(layout="wide")  

# Baixando os dados e carregando os dados
dataset_path = kagglehub.dataset_download("crazygump/myanimelist-scrappind-a-decade-of-anime")
file_path = dataset_path + "/MAL-all-from-winter1917-to-fall2024.csv"
df = pd.read_csv(file_path, sep=",", encoding="utf-8-sig")

# Limpando e formatando os dados
df = df.drop(['MAL_id', 'release-date', 'demographics', 'themes', 'members'], axis=1)
df["studio"] = df["studio"].str.replace(r"[\[\]']", "", regex=True)
df["genres"] = df["genres"].str.replace(r"[\[\]']", "", regex=True)
df["release-year"] = pd.to_datetime(df["release-year"], format="%Y", errors="coerce")
df["release-year"] = df["release-year"].dt.year
df = df.sort_values("release-year")
df["decade"] = (df["release-year"] // 10) * 10

# Titulo do dashboard na sidebar
fig_title = f"""
    <div style="width: 100%; height: 120px; background-color:#0E1117;border-radius: 30px; padding: 10px; display: flex; flex-direction: column; justify-content: center; align-items: center; margin-bottom: 40px;">
        <h1 style="font-family: serif; text-align: center; font-size: 25px; color: white;">Análise de Animes - MyAnimeList</h1>
    </div>
"""
st.sidebar.markdown(fig_title, unsafe_allow_html=True)

# Adicionando filtros de ano e temporada
year_options = ["Todos"] + sorted(df['release-year'].dropna().unique().tolist())
year = st.sidebar.selectbox("Ano", year_options)
season_options = ["Todos"] + sorted(df['release-season'].dropna().unique().tolist())
season = st.sidebar.selectbox("Temporada", season_options)

# Aplicando filtros na página
df_filtered = df.copy()
if year != "Todos":
    df_filtered = df_filtered[df_filtered['release-year'] == year]
if season != "Todos":
    df_filtered = df_filtered[df_filtered['release-season'] == season]

# Conjunto de regras e tratamento da base de dados para responder as perguntas e colocar nos gráficos

# Anime mais bem avaliado para o markdown
max_score = df["score"].max()
max_anime = df[df["score"] == max_score]["title"].values[0]

# Quantidade de animes por ano
df_ano = df_filtered.copy()
df_ano = df_ano.drop_duplicates(subset=['title'])
df_grouped = df_ano.groupby("release-year")["title"].count().reset_index()

# Genêro com maior frequencia
df_genre = df_filtered["genres"].str.split(", ").explode().value_counts()
max_genre = df_genre.max()
max_name = df_genre[df_genre == max_genre].index[0]

# Selecionando os 5 animes com maior número de episódios
df_unique = df_filtered.drop_duplicates(subset='title')
df_top5_ep = df_unique.nlargest(5, 'episodes')[['episodes', 'title']]
df_top5_ep = df_top5_ep.sort_values(by="episodes", ascending=True)

# Média de nota por gênero
df_exploded = df_filtered.copy()
df_exploded['genres'] = df_exploded['genres'].str.split(', ')  
df_exploded = df_exploded.explode('genres')  
df_exploded = df_exploded[df_exploded['genres'].notna()]
df_mean = df_exploded.groupby('genres')['score'].mean().reset_index()
df_mean_sorted = df_mean.sort_values(by='score', ascending=False)

# 5 estúdios que mais produziram animes
df_estudio = df_filtered.copy()
df_estudio['studio'] = df_estudio['studio'].str.split(', ')
df_estudio = df_estudio.explode('studio')
df_estudio = df_estudio[df_estudio['studio'].notna()]
df_estudio = df_estudio[df_estudio['studio'].str.strip() != ""]
df_estudio = df_estudio[df_estudio['studio'].str.lower() != "unknown"]
df_estudio_unique = df_estudio.drop_duplicates(subset=['title', 'studio'])
df_top5_std = df_estudio_unique.groupby("studio")["title"].count().reset_index()
df_top5_std = df_top5_std.sort_values(by="title", ascending=False).head(5)

# Anime com maior nota vs anime com mais episódios
df_compara = df_filtered[['title', 'score', 'episodes']]
df_compara = df_compara.drop_duplicates(subset=['title'])
df_compara1 = df_compara.sort_values(by='episodes', ascending=False).head(1)
df_compara2 = df_compara.sort_values(by='score', ascending=False).head(1)
junta = pd.concat([df_compara1, df_compara2], ignore_index=True)

# Quantidade de animes por década
df_decada = df_filtered.copy()
df_decada = df_decada.drop_duplicates(subset=['title'])
df_decada = df_filtered.groupby("decade")["title"].count().reset_index()

# Criando colunas para o layout
col3, col4, col5 = st.columns(3)
col6, col7, col8 = st.columns(3)

# Markdown exibindo o anime com maior nota na sidebar
fig_score1 = f"""
    <div style="width: 100%; height: 120px; border-radius: 30px; background-color:#0E1117; padding: 20px; display: flex; flex-direction: column; justify-content: center; align-items: center; margin-bottom: 40px; margin-top: 250px;">
        <h1 style="font-family: serif; text-align: center; font-size: 20px; color: white;">Anime com Maior Nota:</h1>
        <h2 style="font-family: serif; text-align: center; font-size: 20px; color: white;">{max_anime} - {max_score}</h2>
    </div>
"""
st.sidebar.markdown(fig_score1, unsafe_allow_html=True)

# Markdown exibindo o genêro com maior frequencia na sidebar
fig_score2 = f"""
    <div style="width: 100%; height: 120px; border-radius: 30px; background-color:#0E1117; padding: 20px; display: flex; flex-direction: column; justify-content: center; align-items: center;">
        <h1 style="font-family: serif; text-align: center; font-size: 20px; color: white;">Gênero com Maior Frequencia:</h1>
        <h2 style="font-family: serif; text-align: center; font-size: 20px; color: white;">{max_genre} - {max_name}</h2>
    </div>
"""
st.sidebar.markdown(fig_score2, unsafe_allow_html=True)

# Gráfico da Quantidade de Animes por Ano
fig_anime_ano = px.bar(df_grouped, x="release-year", y="title", title="Quantidade de Animes por Ano", color_discrete_sequence=["#00FFFF"])

# Personalização do gráfico 
fig_anime_ano.update_layout(plot_bgcolor="#262730", title_font=dict(size=18, color="white", family="serif", weight="bold"), title_x=0.25, xaxis_title="Ano de Lançamento", yaxis_title="Número de Animes", xaxis=dict(showgrid=False, tickangle=-45, tickfont=dict(color="white")), yaxis=dict(showgrid=True, gridcolor="white", tickfont=dict(color="white")))

# Exibindo o gráfico no Streamlit
col3.plotly_chart(fig_anime_ano, use_container_width=True)

# Gráfico top 5 quantidade de episódios
fig_ep = px.bar(df_top5_ep, x="episodes", y="title", title="Top 5 Animes com Mais Episódios", orientation="h", color_discrete_sequence=["#00FFFF"])

# Personalização do gráfico 
fig_ep.update_layout(plot_bgcolor="#262730", title_font=dict(size=18, color="white", family="serif", weight="bold"), title_x=0.25, xaxis_title="Quantidade de Episodios", yaxis_title="", xaxis=dict(showgrid=True, gridcolor="white", tickangle=-45, tickfont=dict(color="white")), yaxis=dict(showgrid=False, gridcolor="white", tickfont=dict(color="white")))

# Exibindo o gráfico no Streamlit
col4.plotly_chart(fig_ep, use_container_width=True)

# Gráfico de média de avaliação por gênero
fig_genre_score = px.bar(df_mean_sorted, x="genres", y="score", title="Média de Nota por Gênero", color_discrete_sequence=["#00FFFF"])

# Personalização do gráfico 
fig_genre_score.update_layout(plot_bgcolor="#262730", title_font=dict(size=18, color="white", family="serif", weight="bold"), title_x=0.25, xaxis_title="", yaxis_title="", xaxis=dict(showgrid=False, gridcolor="white", tickangle=-45, tickfont=dict(color="white")), yaxis=dict(showgrid=True, gridcolor="white", tickfont=dict(color="white")))

# Exibindo o gráfico no Streamlit
col5.plotly_chart(fig_genre_score, use_container_width=True)

# Gráfico estudios que mais produziram 
fig_std = px.bar(df_top5_std, x="studio", y="title", title="Estúdios que Mais Produziram", color_discrete_sequence=["#00FFFF"])

# Personalização do gráfico 
fig_std.update_layout(plot_bgcolor="#262730", title_font=dict(size=18, color="white", family="serif", weight="bold"), title_x=0.25, xaxis_title="", yaxis_title="Quantidade de Animes", xaxis=dict(showgrid=False, gridcolor="white", tickangle=-45, tickfont=dict(color="white")), yaxis=dict(showgrid=True, gridcolor="white", tickfont=dict(color="white")))

# Exibindo o gráfico no Streamlit
col6.plotly_chart(fig_std)

# Gráfico de comparação entre nota com episódios 
fig_std = px.bar(junta, x="score", y='title',title="Relação Entre Episodios e Nota", text="episodes", color_discrete_sequence=["#00FFFF"])

# Personalização do texto
fig_std.update_traces(textfont=dict(color="black"))

# Personalização do gráfico 
fig_std.update_layout(plot_bgcolor="#262730", title_font=dict(size=18, color="white", family="serif", weight="bold"), title_x=0.25, xaxis_title="Nota", yaxis_title="", xaxis=dict(showgrid=True, gridcolor="white", tickangle=-45, tickfont=dict(color="white")), yaxis=dict(showgrid=False, gridcolor="white", tickfont=dict(color="white")))

# Exibindo o gráfico no Streamlit
col7.plotly_chart(fig_std)

# Gráfico de animes lançados por decada
fig_anime_decada = px.bar(df_decada, x="decade", y="title", title="Quantidade de Animes por Década", color_discrete_sequence=["#00FFFF"])

# Personalização do gráfico 
fig_anime_decada.update_layout(plot_bgcolor="#262730", title_font=dict(size=18, color="white", family="serif", weight="bold"), title_x=0.25, xaxis_title="", yaxis_title="Quantidade de Animes", xaxis=dict(showgrid=False, gridcolor="white", tickangle=-45, tickfont=dict(color="white")), yaxis=dict(showgrid=True, gridcolor="white", tickfont=dict(color="white")))

# Exibindo o gráfico no Streamlit
col8.plotly_chart(fig_anime_decada, use_container_width=True)

