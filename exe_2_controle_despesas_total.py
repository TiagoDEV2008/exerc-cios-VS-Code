despesas = []
nomes = []

for numero in range(3):
    nome = input("Nome da despesa: ")
    valor = float(input("Valor da despesa: R$ "))
    nomes.append(nome)

    despesas.append(valor)

    print(f"{nome} registrada: R$ {valor:.2f}")

print(despesas)
print(nomes)

total = sum(despesas)

print(f"Total gasto: R$ {total:.2f}")

quantidade = len(despesas)
media = total / quantidade
maior_despesa = max(despesas)

print(f"Quantidade de despesas: {quantidade}")
print(f"Média das despesas: R$ {media:.2f}")
print(f"Maior despesa: R$ {maior_despesa:.2f}")

indice_maior = despesas.index(maior_despesa)
nome_maior = nomes[indice_maior]
print(f"Nome da maior despesa: {nome_maior}")