despesas = []
nomes = []

while True:
    print("\n1 - Adicionar despesa")
    print("2 - Ver resumo")
    print("3 - Listar despesas")
    print("4 - despesa acima da média")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome da despesa: ")
        valor = float(input("Valor da despesa: R$ "))

        nomes.append(nome)
        despesas.append(valor)

        print(f"{nome} registrada: R$ {valor:.2f}")

    elif opcao == "2":
        if len(despesas) == 0:
            print("Nenhuma despesa cadastrada.")
        else:
            total = sum(despesas)
            quantidade = len(despesas)
            media = total / quantidade
            maior_despesa = max(despesas)

            indice_maior = despesas.index(maior_despesa)
            nome_maior = nomes[indice_maior]

            print(f"Total gasto: R$ {total:.2f}")
            print(f"Quantidade de despesas: {quantidade}")
            print(f"Média: R$ {media:.2f}")
            print(f"Maior despesa: {nome_maior} - R$ {maior_despesa:.2f}")

    elif opcao == "3":
        if len(despesas) == 0:
            print("Nenhuma despesa cadastrada.")
        else:
            print("Despesas cadastradas:")
            for i in range(len(despesas)):
                print(f"- {nomes[i]}: R$ {despesas[i]:.2f}")

    elif opcao == "4":

        if len(despesas) == 0:
            print("Nenhuma despesa cadastrada.")
        else:
            total = sum(despesas)
            quantidade = len(despesas)
            media = total / quantidade

            print("Despesas acima da média:")
            for i in range(len(despesas)):
                if despesas[i] > media:
                    print(f"- {nomes[i]}: R$ {despesas[i]:.2f}")
    elif opcao == "5":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida.")