notas = [8.5, 6.0, 7.5, 4.0, 9.0, 5.5] 
soma = sum(notas)
# SUM tem a função de somar todos os elementos da lista, nesse caso, a soma das notas. 

media = soma / len(notas) 
# A função LEN tem a função de contar quantos elementos tem na lista, nesse caso, a quantidade de notas.

print(f"A média das notas é: {media}") 
for nota in notas:     
    if nota >= 7.0:        
         print(f"{nota} - aprovado.")     
else:         
         print(f"{nota} - reprovado.")