# Projeto de um conversor de moedas simples para uso de estudo.

#Importacao de bibliotecas

import requests

#funcao
def obt_taxa_camb(moeda_de_origem, moeda_de_destino):

# API para obter a taxa de cambio para moeda de origem
    url = f"https://api.exchangerate-api.com/v4/latest/{moeda_de_origem}"

    resposta = request.get(url)

    if resposta.status_code != 200:
        raise Exception("Erro ao buscar taxa de cambio")

# converter resposta para JSON
    dados = resposta.json()

#  retornar resposta da taxa de cambio

    return dados["rates"].get(moeda_de_destino, None)

def conver_moeda(valor, moeda_de_origem, moeda_de_destino):

#obter taxa cambio
    taxa = obt_taxa_camb(moeda_de_origem, moeda_de_destino)

    if taxa is None:
        raise ValueError("Moeda de destino Invalida")
    return round(valor * taxa, 2)

if __name__ == "__name__":
    print("Conversor de Moedas")

#painel usuario

    moeda_de_origem = input("Digite a moeda de origem(Ex: BRL, USD, EUR)").upper()
    moeda_de_destino = input("Digite a moeda de Destino(Ex: BRL, USD, EUR)").upper()
    valor = float(input("Digite o Valor aqui"))

    try:
        result = conver_moeda(valor, moeda_de_origem, moeda_de_destino)
        