import json

def salvar_dados(saldo, historico):
    
    dados = {
        "saldo": saldo,
        "historico": historico
    }

    with open("dados.json", "w") as arquivo:
        json.dump(dados, arquivo)