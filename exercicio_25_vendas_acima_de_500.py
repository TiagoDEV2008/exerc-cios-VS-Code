vendas = [250, 800, 120, 1500, 600, 90, 1100]
def analisar_vendas(vendas):
    quantidades_vendas_500 = 0
    for venda in vendas:
        if venda > 500:
            quantidades_vendas_500 += 1
    return quantidades_vendas_500

print(f"A quantidade de vendas acima de 500 é: {analisar_vendas(vendas)}") 