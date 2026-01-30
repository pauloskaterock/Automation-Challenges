# Coletor tempo – Python

Este projeto foi desenvolvido como parte de um **teste técnico**, com o objetivo de demonstrar a coleta de dados de um website por **web scraping** e por **API pública**, utilizando Python e salvando os resultados em arquivos CSV.

O tema escolhido foi **dados climáticos**, por ser um domínio simples, claro e facilmente comparável entre as duas abordagens.

---

##  Objetivo

- Coletar dados climáticos de São Paulo utilizando:
  - **Web Scraping**
  - **API pública**
- Estruturar e salvar os dados em arquivos CSV
- Aplicar boas práticas de código, simplicidade, tratamento de erros e clareza

---

##  Tecnologias Utilizadas

- Python 3.13.1
- requests
- beautifulsoup4

---

##  Estrutura do Projeto

btimeBot/
├── readme.txt            # explicação projeto
├── requirements.txt      # Dependências do projeto
├── teste.txt             # Case tecnico desafio
├── weather_scraping.py   # Coleta de dados via web scraping
├── weather_api.py        # Coleta de dados via API pública


## Execucao btimeBot

- python weather_scraping.py
- python weather_api.py

- saida esperada

- Cada script gera um arquivo CSV com os campos:

city
temperature
condition
source
