notas = [8, 5, 9, 6, 7, 10, 4]
def analisar_notas(notas):
    quantidades_aprovadas = 0
    for nota in notas:
        if nota >= 9:
            quantidades_aprovadas += 1
    return quantidades_aprovadas

print(f"A quantidade de alunos aprovados é: {analisar_notas(notas)}")

