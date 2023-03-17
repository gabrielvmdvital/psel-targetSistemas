faturamento_por_estados = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
    }

# calcula o valor total faturado para realizar o calculo da porcentagem de participação
total_faturado = sum(valor for key, valor in faturamento_por_estados.items())

# cria um novo dicionario contendo as informações da porcentagem de representação por estado
percentual_de_representacao = {key: valor/total_faturado for key, valor in faturamento_por_estados.items()}
print(percentual_de_representacao)

print(sum(percentual_de_representacao[key] for key in percentual_de_representacao.keys()))


