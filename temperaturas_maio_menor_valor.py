temperaturas = [22, 19, 25, 31, 18, 27, 24]
maior = temperaturas[0]
menor = temperaturas[0] 

for t in temperaturas:
    if t > maior:
        maior = t
    if t < menor:
        menor = t

print(f"A maior temperatura é: {maior}")
print(f"A menor temperatura é: {menor}")