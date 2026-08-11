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

def pesquisar_transacoes(historico):

    while True:
        print("========== PESQUISAR TRANSAÇÕES ==========")
        print("""Você pode pesquisar por:
        
        - Tipo: Entrada ou Gasto
        - Valor: Digite o valor exato ou parte dele
        - Categoria: Para gastos, digite a categoria
        - Data: Digite a data no formato DD/MM/AAAA
        """)

        pesquisa = input("Digite o que deseja pesquisar: ")

        if pesquisa =="":
            print("Tente digitar algo.")
            continue
        break
        
    resultados = []
    for item in historico:
            if pesquisa.lower() in str(item).lower():
                resultados.append(item)
    if resultados:
            print("========== RESULTADOS DA PESQUISA ==========")
            for item in resultados:
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
    else:
            print("Nenhuma transação encontrada.")
    input("Pressione ENTER para voltar ao menu...")

def editar_transacao(saldo, historico):
    for indice, item in enumerate(historico):
        tipo = item[0]
        valor = item[1]

        if tipo == "entrada":
            data = item[2]

            print(f"""
        [{indice}] 🟢 ENTRADA
        Valor: R$ {valor:.2f}
        Data: {data}
        -------------------------------""")

        elif tipo == "gasto":
            categoria = item[2]
            data = item[3]

            print(f"""
        [{indice}] 🔴 GASTO
        Valor: R$ {valor:.2f}
        Categoria: {categoria}
        Data: {data}
        -------------------------------""")

    indice = int(input("Digite o número da transação que deseja editar: "))
    if 0 <= indice < len(historico):
        item = historico[indice]
        tipo = item[0]

        if tipo == "entrada":
            novo_valor = float(input("Digite o novo valor da entrada: "))

            diferenca = novo_valor - valor
            saldo += diferenca

            historico[indice] = ("entrada", novo_valor, item[2])
            print("Entrada atualizada com sucesso.")

        elif tipo == "gasto":
            novo_valor = float(input("Digite o novo valor do gasto: "))
            nova_categoria = input("Digite a nova categoria do gasto: ")
            diferenca = novo_valor - valor
            saldo += diferenca
            historico[indice] = ("gasto", novo_valor, nova_categoria, item[3])
            print("Gasto atualizado com sucesso.")
            

        else:
            print("Valor inválido. Tente um número existente.")

    return saldo, historico
            
def excluir_transacao(saldo, historico):
    for indice, item in enumerate(historico):
        tipo = item[0]
        valor = item[1]

        if tipo == "entrada":
            data = item[2]

            print(f"""
        [{indice}] 🟢 ENTRADA
        Valor: R$ {valor:.2f}
        Data: {data}
        -------------------------------""")

        elif tipo == "gasto":
            categoria = item[2]
            data = item[3]

            print(f"""
        [{indice}] 🔴 GASTO
        Valor: R$ {valor:.2f}
        Categoria: {categoria}
        Data: {data}
        -------------------------------""")

    while True:        
        try:
            indice = int(input("Digite o número da transação que deseja excluir: "))
            break

        except:
            print("Valor inválido. Digite um número.")

    if 0 <= indice < len(historico):
            item = historico[indice]
            tipo = item[0]   
        
            if tipo == "entrada":
                confirmacao = input("Tem certeza que deseja excluir esta entrada? (s/n): ")

                if confirmacao.lower() == "s":

                    saldo -= item[1]
                    historico.pop(indice)
                    print("Entrada excluída com sucesso.")

                else:
                    print("Exclusão cancelada.")
                    

            elif tipo == "gasto":
                confirmacao = input("Tem certeza que deseja excluir este gasto? (s/n): ")
                if confirmacao.lower() == "s":
                    saldo += item[1]
                    historico.pop(indice)
                    print("Gasto excluído com sucesso.")
                else:
                    print("Exclusão cancelada.")

    else:
            print("Valor inválido. Tente um número existente.")

    return saldo, historico