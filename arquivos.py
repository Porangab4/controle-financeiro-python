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
        try:
            with open("dados.json", "r") as arquivo:
                dados = json.load(arquivo)

            return dados["saldo"], dados["historico"]

        except (json.JSONDecodeError, KeyError):
            print("Erro ao carregar os dados. Inicializando com saldo 0 e histórico vazio.")
            return 0, []

    return 0, []