def contar_positivos(numeros):
    quantidade = 0

    for numero in numeros:
        if numero > 0:
            quantidade += 1

    return quantidade
numeros = [10, -2, 0, 7, -5, 3]

print(contar_positivos(numeros))