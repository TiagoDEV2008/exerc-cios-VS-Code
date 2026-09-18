numeros = [3, 8, 12, 5, 20, 1]

def contar_quantos_numeros(numeros):
    contador = 0

    for numero in numeros:
        if numero > 10:
            contador += 1

    return contador

resultado = contar_quantos_numeros(numeros)

print(f"A quantidade de números maiores que 10 é: {resultado}")