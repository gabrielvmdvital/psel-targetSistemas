import json

with open(r"dados.json") as file:
    dados = json.load(file)

def min_faturamento(dados: dict) -> str:
    min_value = min(dados, key=lambda x: x["valor"])
    return f"O dia {min_value['dia']} teve o menor faturamento que foi de R$ {min_value['valor']}"

def max_faturamento(dados: dict) -> str:
    min_value = max(dados, key=lambda x: x["valor"])
    return f"O dia {min_value['dia']} teve o maior faturamento que foi de R$ {min_value['valor']}"

def num_faturamento_acima_da_media(dados: dict) -> str:
    list_valor = [x['valor'] for x in dados]
    media = round(sum(list_valor)/len(list_valor), 2) # arredondando a média
    num_faturamento = sum(1 for faturamento_diario in list_valor if faturamento_diario > media)

    return f"O número de dias do mês que o valor do faturamento diário foi superior à média mensal de {media} é de {num_faturamento}"


if __name__ == '__main__':
    print(min_faturamento(dados))
    print(max_faturamento(dados))
    print(num_faturamento_acima_da_media(dados))
    