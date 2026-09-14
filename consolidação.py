soma = 0
reprovados = 0
aprovados = 0

notas = [7.5, 4.0, 8.5, 6.0, 9.0, 5.5, 10.0]
for nota in notas:
    soma = soma + nota

    if nota >= 7:
        aprovados = aprovados + 1
    else:
        reprovados = reprovados + 1

media = soma / len(notas)

print(f"A soma das notas é: {soma}")
print(f"A quantidade de alunos aprovados é: {aprovados}")
print(f"A quantidade de alunos reprovados é: {reprovados}")
print(f"A média das notas é: {media}")