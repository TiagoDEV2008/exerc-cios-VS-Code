real = float(input("quanto você tem na carteira: R$"))
dolar = real / 5.20
print("com R${} VOCÊ PODE COMPRAR US${:.2f}".format(real, dolar))

euro = real / 6.20
print("com R${} VOCÊ PODE COMPRAR €${:.2f}".format(real, euro))

input("Pressione Enter para sair...")