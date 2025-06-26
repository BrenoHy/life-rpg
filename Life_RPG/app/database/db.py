import json

# Função para salvar os dados em um arquivo .json
def salvar_dados(nome_arquivo, dados):
    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)

# Função para carregar os dados salvos
def carregar_dados(nome_arquivo):
    try:
        with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return None
