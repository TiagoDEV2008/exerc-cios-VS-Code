numeros = [2, 4, 6, 8]
def maior_da_lista(lista):
    maior = lista[0]
    for numero in lista:
        if numero > maior:
            maior = numero
    return maior

print(f"O maior número na lista é: {maior_da_lista(numeros)}")