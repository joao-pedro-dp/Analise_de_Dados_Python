# Análise de Animes - MyAnimeList

Este repositório contém uma aplicação interativa desenvolvida com Streamlit para analisar e visualizar dados de animes extraídos do MyAnimeList. Utilizando um conjunto de dados que abrange animes lançados de 1917 até 2024, a aplicação permite a exploração de várias informações interessantes sobre os animes, como avaliações, gêneros, estúdios de produção, número de episódios e tendências ao longo do tempo.

# Site Para Visualização do Dashboard

[Dashboard]([http://www.exemplo.com](https://primeirodashempythonjp.streamlit.app/))
                
# Funcionalidades

A aplicação responde às seguintes perguntas e exibe os resultados em gráficos interativos:

Anime mais bem avaliado: Exibe o anime com a maior avaliação de todos os tempos.

Quantidade de animes por ano: Mostra a quantidade de animes lançados por ano.

Gênero mais frequente: Indica qual gênero de anime é mais comum na base de dados.

Top 5 animes com maior número de episódios: Apresenta os cinco animes com o maior número de episódios.

Média de avaliação por gênero: Exibe a média de avaliação para cada gênero de anime.

Estúdios que mais produziram animes: Mostra os cinco estúdios de anime que mais produziram.

Relação entre avaliação e número de episódios: Compara a avaliação e o número de episódios dos animes.

Animes mais populares por década: Mostra a quantidade de animes lançados por década.

# Bibliotecas Utilizadas

Streamlit: Framework para construir a interface interativa.

Pandas: Biblioteca para manipulação e análise de dados.

Plotly: Biblioteca para a criação de gráficos interativos.

Kaggle Hub: Para download do dataset utilizado.


# Pré-requisitos
Antes de rodar o projeto, você precisa ter as dependências instaladas:

Você pode instalar essas dependências utilizando o pip:

        pip install streamlit pandas plotly kagglehub

# Como Usar

Baixar os dados: O conjunto de dados é baixado automaticamente através do KaggleHub. Não é necessário fazer o download manualmente, basta rodar a aplicação.
Executar a aplicação: Após instalar as dependências, execute o comando a seguir para iniciar o servidor do Streamlit:

        streamlit run Animes.py

Isso abrirá uma página interativa no seu navegador.

# Explicação do Código

Carregamento e Limpeza dos Dados: O código começa importando e limpando o conjunto de dados. Removeram-se colunas irrelevantes, e a coluna de ano de lançamento foi transformada para garantir que as análises sejam feitas de forma coerente.

Filtragem dos Dados: A interface permite filtrar os dados com base no ano de lançamento e na temporada. Isso facilita a análise de animes de períodos específicos.

Respostas às Perguntas: Diversos métodos foram usados para calcular as respostas para as perguntas mencionadas, como groupby, nlargest e value_counts. Esses cálculos geram as informações para os gráficos.

Gráficos Interativos: Cada pergunta tem um gráfico associado, que é gerado com a biblioteca Plotly. Esses gráficos são interativos, permitindo ao usuário explorar os dados de maneira intuitiva.

Exibição no Streamlit: O layout é organizado em colunas no Streamlit, onde gráficos e informações são apresentados.

# Exemplo de Tela

A interface do usuário é dividida da seguinte maneira:

Sidebar: Exibe informações do anime mais bem avaliado e o gênero mais frequente, além de filtros para selecionar o ano e a temporada.

Gráficos: A área principal exibe os gráficos interativos para cada uma das perguntas.

# Contribuindo

Se você encontrar algum problema ou quiser melhorar a aplicação, fique à vontade para fazer contribuições. Para isso, basta fazer um fork deste repositório e enviar um pull request.

# Licença

Este projeto está sob a licença MIT.
