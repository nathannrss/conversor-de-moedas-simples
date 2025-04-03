#Projeto de um conversor de moedas simples para uso de estudo.

#Importação de biblioteca.
import requests

#Função para obter a taxa de cambio.
def taxa_camb(moeda_orig, moeda_dest):

#URL da API para obter a taxa de cambio para a moeda de origem.
    url = f"https://api.exchangerate-api.com/v4/latest/{moeda_orig}"
    resposta = requests.get(url)  

    if resposta.status_code != 200:
        raise Exception("Erro ao buscar taxa de câmbio.")
    
    return resposta.json()["rates"].get(moeda_dest, None)  

#função para conversao de moeda.
def conver_moeda(valor, moeda_orig, moeda_dest):
    taxa = taxa_camb(moeda_orig, moeda_dest)

    if taxa is None:
        raise ValueError("Moeda de destino inválida.")

    return round(valor * taxa, 2)


if __name__ == "__main__":  
    #mensagem inicial do programa.
    print("Conversor de Moedas")

    #painel do usuario.
    nome = input("Olá, como vai? Digite seu nome aqui: ").strip()
    
    print(f"Olá, {nome}, é um prazer lhe ajudar com a sua conversão de moeda!")

#loop até que a conversao seja bem sucedida.
    while True: 
        moeda_orig = input("Digite a moeda de origem (Ex: BRL, USD, EUR): ").strip().upper()

#solicita a moeda de destino.
        moeda_dest = input("Digite a moeda de destino (Ex: BRL, USD, EUR): ").strip().upper()

        try:
#solicita o valor a ser convertido.
            valor = float(input("Digite o valor aqui: "))

#converte o valor usando a taxa de cambio obtida.
            result = conver_moeda(valor, moeda_orig, moeda_dest)

#exibe o resultado da conversao
            print(f"{valor} {moeda_orig} é igual a {result} {moeda_dest}") 

        except ValueError:
#exibe mensagem de erro caso o usuario insira um valor invalido.
            print("Erro: Valor inválido. Certifique-se de digitar um número.")  
            continue

        except Exception as e:
#exibe o erro retornado pela função e reinicia o processo.
            print(f"Erro: {e}. Por favor, tente novamente.")  
            continue  

#pergunta ao usuario se deseja continuar ou sair.
        while True:
            resposta = input(f"Olá, {nome}, deseja fazer uma nova conversão? (S/N): ").strip().upper()

#encerra o programa caso o usuario escolha "N"
            if resposta == "N":
                print(f"Obrigado por usar o conversor, {nome}! Até mais!")
                exit()  

#reinicia o processo caso o usuario escolha "S"
            elif resposta == "S":
                break  

#exibe erro caso a entrada não seja válida
            else:
                print("Opção inválida! Digite 'S' para continuar ou 'N' para sair.")
