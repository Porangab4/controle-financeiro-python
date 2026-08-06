import json
import os
from datetime import datetime
from arquivos import salvar_dados
from financeiro import ver_saldo, adicionar_entrada, adicionar_gasto

saldo = 0
historico = []

def ver_historico():
    if len(historico) == 0:
        print("Não há histórico de transações.")
        return
    print("========== HISTÓRICO ==========")

    for item in historico:
        tipo = item[0]
        valor = item[1]

        if tipo == "entrada":
            data = item[2]

            print(f"""
        🟢 ENTRADA
        Valor: R$ {valor:.2f}
        Data: {data}
        -------------------------------""")

        elif tipo == "gasto":
            categoria = item[2]
            data = item[3]

            print(f"""
        🔴 GASTO
        Valor: R$ {valor:.2f}
        Categoria: {categoria}
        Data: {data}
        -------------------------------""")

def sair():
    print("Obrigado por usar o Controle Financeiro!")

def calcular_resumo():
    total_entradas = sum(item[1] for item in historico if item[0] == "entrada")
    total_gastos = sum(item[1] for item in historico if item[0] == "gasto")
    saldo_atual = total_entradas - total_gastos

    print("========== RESUMO ==========")
    print(f"Total de entradas: R$ {total_entradas:.2f}")
    print(f"Total de gastos: R$ {total_gastos:.2f}")
    print(f"Saldo atual: R$ {saldo_atual:.2f}")

def resumo_categorias():
    gastos_categoria = {}
    for item in historico:
        if item[0] == "gasto":
            valor = item[1]
            categoria = item[2]

            if categoria in gastos_categoria:
                gastos_categoria[categoria] += valor
            else:
                gastos_categoria[categoria] = valor

    print("========== GASTOS POR CATEGORIA ==========")

    for categoria, total in gastos_categoria.items():
        print(f"{categoria}: R$ {total:.2f}")

def carregar_dados():
    global saldo, historico

    if os.path.exists("dados.json"):
        with open("dados.json", "r") as arquivo:
            dados =json.load(arquivo)

        saldo = dados["saldo"]
        historico = dados["historico"]

carregar_dados()

while True:

    print("=========================")
    print("CONTROLE FINANCEIRO")
    print("=========================")

    print("1 - Adicionar entrada")
    print("2 - Adicionar gasto")
    print("3 - Ver saldo")
    print("4 - Ver histórico")
    print("5 - Calcular resumo")
    print("6 - Resumo por categoria")
    print("7 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        saldo, historico = adicionar_entrada(saldo, historico)

    elif opcao == "2":
        saldo, historico = adicionar_gasto(saldo, historico)

    elif opcao == "3": 
        ver_saldo(saldo)

    elif opcao == "4":
        ver_historico()

    elif opcao == "5":
        calcular_resumo()
        
    elif opcao == "6":
        resumo_categorias()

    elif opcao == "7":
        sair()
        break

    else:
        print("Opção inválida.")
        