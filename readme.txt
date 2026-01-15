🧾 RPA Challenge – Invoice Automation (Python)
📌 Visão Geral

Este projeto implementa uma automação RPA em Python, desenvolvida para resolver o desafio proposto no site RPA Challenge OCR, cujo objetivo é:

Ler dados de uma tabela web

Realizar o download automático de faturas (PDF)

Extrair informações relevantes das faturas

Gerar um arquivo CSV no formato exato exigido

Submeter o CSV para validação no próprio site

A solução foi construída com foco em robustez, clareza de código e boas práticas de RPA, simulando um cenário real de automação corporativa.

🧠 Abordagem adotada

Essa abordagem reflete práticas comuns em projetos reais de RPA, especialmente quando não há uma API pública disponível para consumo direto.

Este mesmo desafio já foi resolvido anteriormente utilizando ferramentas RPA low-code (ex.: UiPath / Automation Anywhere).

Nesta implementação, a proposta foi reproduzir a mesma lógica de negócio em Python, com controle total do fluxo e maior flexibilidade técnica.

⚙️ Tecnologias utilizadas

Python 3

Selenium – automação do navegador

WebDriver Manager – gerenciamento automático do driver

pdfplumber – leitura e extração de texto de PDFs

python-dateutil – tratamento de datas

📂 Estrutura do projeto

A separação em módulos facilita:

Manutenção

Testes

Reutilização de componentes

🔄 Fluxo da automação

A automação abre o site do desafio

O botão Start é acionado para iniciar a contagem

Apenas a primeira linha da tabela é lida (conforme requisito)

A fatura correspondente é baixada automaticamente

O PDF é processado para extrair:

Número da fatura

Data da fatura

Nome da empresa

Valor total devido

É aplicada a regra de negócio:

Somente faturas vencidas ou com vencimento na data atual são consideradas

Um CSV é gerado exatamente no formato solicitado

O CSV é enviado via upload no próprio site

O processo é finalizado de forma limpa
