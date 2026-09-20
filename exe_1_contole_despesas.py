despesas = []

for numero in range(3):
    nome = input("Nome da despesa: ")
    valor = float(input("Valor da despesa: R$ "))

    despesas.append(valor)

    print(f"{nome} registrada: R$ {valor:.2f}")

print(despesas)