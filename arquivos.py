import json
import os

def salvar_dados(saldo, historico):
    
    dados = {
        "saldo": saldo,
        "historico": historico
    }

    with open("dados.json", "w") as arquivo:
        json.dump(dados, arquivo)

def carregar_dados():

    if os.path.exists("dados.json"):
        with open("dados.json", "r") as arquivo:
            dados =json.load(arquivo)

        return dados["saldo"], dados["historico"]

    return 0, []