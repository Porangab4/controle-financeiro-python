def ver_historico(historico):
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

def calcular_resumo(historico):
    total_entradas = sum(item[1] for item in historico if item[0] == "entrada")
    total_gastos = sum(item[1] for item in historico if item[0] == "gasto")
    saldo_atual = total_entradas - total_gastos

    print("========== RESUMO ==========")
    print(f"Total de entradas: R$ {total_entradas:.2f}")
    print(f"Total de gastos: R$ {total_gastos:.2f}")
    print(f"Saldo atual: R$ {saldo_atual:.2f}")

def resumo_categorias(historico):
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