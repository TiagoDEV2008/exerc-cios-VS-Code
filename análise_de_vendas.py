vendas = [1102, 3500, 900, 5000, 2700, 6000, 4100, 2000]
maior_venda = vendas[0]
menor_venda = vendas[0]
for venda in vendas:
    if venda > maior_venda:
        maior_venda = venda
    if venda < menor_venda:
        menor_venda = venda
soma = 0
for venda in vendas:
    soma = soma + venda
media = soma / len(vendas)

acima_da_media = 0
for venda in vendas:
    if venda > media:
        acima_da_media = acima_da_media + 1
abaixo_ou_igual_a_media = len(vendas) - acima_da_media

maior_ou_igual_a_300 = 0
for venda in vendas:
    if venda >= 300:
        maior_ou_igual_a_300 = maior_ou_igual_a_300 + 1


print(f"o total de vendas é: {soma}")
print(f"A maior venda é: {maior_venda}")
print(f"A menor venda é: {menor_venda}")
print(f"A média das vendas é: {media}")
print(f"O número de vendas acima da média é: {acima_da_media}")
print(f"O número de vendas abaixo ou igual à média é: {abaixo_ou_igual_a_media}")
print(f"A quantidade de vendas maior ou igual a 300 é de: {maior_ou_igual_a_300}")