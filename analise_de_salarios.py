salarios = [100, 200, 300, 400, 500]
maior_salario = salarios[0]
menor_salario = salarios[0]
for salario in salarios:
    if salario > maior_salario:
        maior_salario = salario
    if salario < menor_salario:
        menor_salario = salario

soma = 0
for salario in salarios:
    soma = soma + salario
media = soma / len(salarios)

acima_da_media = 0
for salario in salarios:
    if salario > media:
        acima_da_media = acima_da_media + 1




print(f"O maior salário é: {maior_salario}")
print(f"o menor salário é: {menor_salario}")
print(f"A soma dos salários é: {soma}") 
print(f"A média dos salários é: {media}")
print(f"O número de salários acima da média é: {acima_da_media}")
print(f"O número de salários abaixo ou igual à média é: {len(salarios) - acima_da_media}")