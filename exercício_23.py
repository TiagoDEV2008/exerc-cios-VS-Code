notas = [8, 6, 9, 5, 7]
def media_final(notas):
    soma = 0
    for nota in notas:
        soma = nota + soma
    return soma / len(notas)

media = media_final(notas)

print(f"A média das notas é: {media}")