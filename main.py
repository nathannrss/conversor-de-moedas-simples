# Projeto de um conversor de moedas simples para uso de estudo.

#Importacao de bibliotecas

import requests

#funcao
def obt_taxa_camb(moeda_de_origem, moeda_de_destino):

# API para obter a taxa de cambio para moeda de origem
    url = f"https://api.exchangerate-api.com/v4/latest/{moeda_de_origem}"

    resposta = requests.get(url)  # Corrigido request.get(url) para requests.get(url)

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

if __name__ == "__main__":  # Corrigido "__name__" para "__main__"
    print("Conversor de Moedas")

#painel usuario

#melhorando o painel.
    nome = str(input("Olá como vai? Digite seu nome aqui!"))
    print(f'Olá {nome} é um prazer lhe ajudar com a sua conversão de moeda')

    while True:  # Mantem o loop ate que a conversao seja bem-sucedida
        moeda_de_origem = input("Digite a moeda de origem(Ex: BRL, USD, EUR)").upper()
        moeda_de_destino = input("Digite a moeda de Destino(Ex: BRL, USD, EUR)").upper()
        valor = float(input("Digite o Valor aqui"))

        try:
            result = conver_moeda(valor, moeda_de_origem, moeda_de_destino)
            print(f"{valor} {moeda_de_origem} igual à {result} {moeda_de_destino}")  # Corrigido "iqual" para "igual"
            break  # Se a conversao for bem-sucedida, sai do loop
        except Exception as e:
            print(f"Erro: {e}. Por favor, tente novamente.")  # Exibe o erro e volta ao inicio do loop
