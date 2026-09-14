soma = 0 
quantidade = 0 

numeros = [5, 8, 12, 3, 20, 7, 14, 9] 
for numero in numeros:
    if numero % 2 == 0:
        soma = soma + numero
        quantidade = quantidade + 1

print(f"A soma dos números pares é: {soma}")
print(f"A quantidade de números pares é: {quantidade}")