soma = 0
maior_de_idade = 0
menor_de_idade = 0

idades = [15, 22, 17, 30, 12, 18, 25, 16]
maior = idades[0]
menor = idades[0]
for idade in idades:
    soma = soma + idade
    
    if idade > maior:
        maior = idade
    if idade < menor:
        menor = idade


for idade in idades:
    if idade >= 18:
        maior_de_idade = maior_de_idade + 1     
    else:
        menor_de_idade = menor_de_idade + 1
        

media = soma / len(idades)

print(f"Quantidade de pessoas maiores de idade: {maior_de_idade}")
print(f"Quantidade de pessoas menores de idade: {menor_de_idade}")
print(f"A soma das idades é: {soma}")
print(f"A maior idade é: {maior}")
print(f"A menor idade é: {menor}")
print(f"A média das idades é: {media}")
