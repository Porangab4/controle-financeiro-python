from arquivos import carregar_dados
from financeiro import ver_saldo, adicionar_entrada, adicionar_gasto
from relatorios import pesquisar_transacoes, ver_historico, calcular_resumo, resumo_categorias, editar_transacao, excluir_transacao


def mostrar_menu():
    print("=========================")
    print("CONTROLE FINANCEIRO")
    print("=========================")
    print("1 - Adicionar entrada")
    print("2 - Adicionar gasto")
    print("3 - Ver saldo")
    print("4 - Ver histórico")
    print("5 - Calcular resumo")
    print("6 - Resumo por categoria")
    print("7 - Pesquisar transações")
    print("8 - Excluir transação")
    print("9 - Editar transação")
    print("10 - Sair")


def sair():
    print("Obrigado por usar o Controle Financeiro!")


saldo, historico = carregar_dados()

while True:
    mostrar_menu()

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        saldo, historico = adicionar_entrada(saldo, historico)

    elif opcao == "2":
        saldo, historico = adicionar_gasto(saldo, historico)

    elif opcao == "3":
        ver_saldo(saldo)

    elif opcao == "4":
        ver_historico(historico)

    elif opcao == "5":
        calcular_resumo(historico)

    elif opcao == "6":
        resumo_categorias(historico)

    elif opcao == "7":
        pesquisar_transacoes(historico)

    elif opcao == "8":
        saldo, historico = excluir_transacao(saldo, historico)

    elif opcao == "9":
        saldo, historico = editar_transacao(saldo, historico)

    elif opcao == "10":
        sair()
        break

    else:
        print("Opção inválida.")