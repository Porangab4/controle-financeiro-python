from datetime import datetime
from arquivos import salvar_dados

def pedir_valor(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            if valor < 0:
                print("O valor não pode ser negativo. Tente novamente.")
            else:
                return valor
        except ValueError:
            print("Valor inválido. Digite um número válido.")

def ver_saldo(saldo):
    print(f"Seu saldo atual é: R$ {saldo:.2f}")


def adicionar_entrada(saldo, historico):

    valor = pedir_valor("Digite o valor da entrada: ")

    data = datetime.now().strftime("%d/%m/%Y")

    saldo += valor

    historico.append(("entrada", valor, data))

    print(f"Entrada de R$ {valor:.2f} adicionada com sucesso.")

    salvar_dados(saldo, historico)

    return saldo, historico

def adicionar_gasto(saldo, historico):

    valor = pedir_valor("Digite o valor do gasto: ")

    while True:
        print("Categorias disponíveis:")
        print("1 - Alimentação")
        print("2 - Transporte")
        print("3 - Lazer")
        print("4 - Saúde")
        print("5 - Educação")
        print("6 - Outros")
        categoria_opcao = input("Escolha uma categoria (1-6): ")

        if categoria_opcao == "1":
            categoria = "Alimentação"
            break
        elif categoria_opcao == "2":
            categoria = "Transporte"
            break
        elif categoria_opcao == "3":
            categoria = "Lazer"
            break
        elif categoria_opcao == "4":
            categoria = "Saúde"
            break
        elif categoria_opcao == "5":
            categoria = "Educação"
            break
        elif categoria_opcao == "6":
            categoria = "Outros"
            break
        else:
            print("Opção inválida. Tente novamente.")

    if saldo >= valor:
        saldo = saldo - valor

        data = datetime.now().strftime("%d/%m/%Y")
        
        historico.append(("gasto", valor, categoria, data))
        print(f"Gasto de R$ {valor:.2f} adicionado com sucesso.")

        salvar_dados(saldo, historico)
    else:
        print("Saldo insuficiente para o gasto.")

    return saldo, historico
