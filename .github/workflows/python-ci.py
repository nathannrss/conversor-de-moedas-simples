# continuous integration conversor de moedas simples
name: CI Conversor De Moedas Simples
on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main
  

jobs:
  executar-testes:
    runs-on: ubuntu-latest

    steps:
      - name: Executar testes com Pytest
        uses: actions/checkout@v4

      - name: Configurar Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      - name: Instalar pacotes e dependências
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
          pip install flake8 pytest requests

      - name: Analisar código Flake8
        run: flake8 .

      - name: Executar testes com Pytest
        run: pytest tests/