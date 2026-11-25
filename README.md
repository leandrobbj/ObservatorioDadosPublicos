# Observatório de Dados Públicos

## Objetivo
O **Observatório de Dados Públicos** é uma aplicação desenvolvida em Python no âmbito da Atividade Prática Integradora da **UFCD 10806: Linguagens de Scripting e Linha de Comandos** (Módulo 5: Recolha e Automatização de Dados com Python, Curso de Análise de Dados). O programa recolhe informação pública de duas fontes de demonstração, uma API e uma página Web, apresenta os resultados na consola e guarda-os em ficheiros CSV.

## Requisitos
* Windows 10/11
* Python 3
* Bibliotecas: `requests` e `beautifulsoup4`
* Ligação à Internet

## Instruções de Execução

1 - Abra o **Git Bash** e execute o seguinte comando para clonar o projeto:
```bash
git clone https://github.com/leandrobbj/ObservatorioDadosPublicos.git
```

2 - Entre na pasta do projeto:
```bash
cd ObservatorioDadosPublicos
```


3 - Execute o script da API (gera `utilizadores.csv`):
```bash
python api_utilizadores.py
```

4 - Execute o script de Web Scraping (gera `citacoes.csv`):
```bash
python scraping_citacoes.py
```

## Fontes de dados
* **API:** [JSONPlaceholder](https://jsonplaceholder.typicode.com/users) (dados fictícios de utilizadores, em formato JSON)
* **Página Web:** [Quotes to Scrape](https://quotes.toscrape.com/) (página para exercícios de Web Scraping)

Não são utilizados dados pessoais, credenciais ou páginas que exijam autenticação.