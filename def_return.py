def multiplicar(a , b):
    return a * b

result1 = multiplicar(2, 5)
result2 = multiplicar(3, 7)
result3 = multiplicar(4, 6)

print(f"O resultado da multiplicação é: {result1}")
print(f"O resultado da multiplicação é: {result2}")
print(f"O resultado da multiplicação é: {result3}")


#----------------------------------------------------------------------#


def verificar_idade(idade):
    if idade >= 18:
        return "Maior de idade"
    else:
        return "Menor de idade"

idade1 = 20
idade2 = 15
idade3 = 18

situação1 = verificar_idade(idade1)
situação2 = verificar_idade(idade2)
situação3 = verificar_idade(idade3)

print(f"A pessoa com {idade1} anos é: {situação1}")
print(f"A pessoa com {idade2} anos é: {situação2}")
print(f"A pessoa com {idade3} anos é: {situação3}")
