estoque = [243, 0, 71, 3, 6, 0, 771, 35, 26, 1]
maior_quantidade = estoque[0]
menor_quantidade = estoque[0]  

for quantidade in estoque:
    if quantidade > maior_quantidade:
        maior_quantidade = quantidade
    if quantidade < menor_quantidade:
        menor_quantidade = quantidade

soma_estoque = 0
for quantidade in estoque:
    soma_estoque += quantidade

media_estoque = soma_estoque / len(estoque)

acima_da_media = 0
estoque_baixo = 0
entre_5_e_20 = 0
estoque_zerado = 0
for quantidade in estoque:
    if quantidade > media_estoque:
        acima_da_media += 1

    if 5 <= quantidade <= 20:
        entre_5_e_20 += 1

    if quantidade < 5:
        estoque_baixo += 1

    if quantidade == 0:
        estoque_zerado += 1
    

print(f"O total de itens em estoque é: {soma_estoque}")
print(f"A maior quantidade em estoque é: {maior_quantidade}")
print(f"A menor quantidade em estoque é: {menor_quantidade}")
print(f"A média das quantidades em estoque é: {media_estoque}")
print(f"O número de itens com quantidade acima da média é: {acima_da_media}")
print(f"O número de itens com quantidade igual a zero é: {estoque_zerado}")
print(f"O número de itens com quantidade abaixo de 5 é: {estoque_baixo}")
print(f"O número de itens com quantidade entre 5 e 20 é: {entre_5_e_20}")