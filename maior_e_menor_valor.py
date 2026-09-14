numeros = [18, 7, 32, 5, 21, 40, 12]
maior = numeros[0]
menor = numeros[0]

for n in numeros:
    if n > maior:
        maior = n
    if n < menor:
        menor = n

print(f"O maior valor é: {maior}")
print(f"O menor valor é: {menor}")