temperaturas = [22, 31, 18, 35, 27, 40, 25]

def contar_temperaturas(temperaturas):
    contador = 0
    for temperatura in temperaturas:
        if temperatura >30:
            contador = contador +1
    return contador

resultado = contar_temperaturas(temperaturas)

print(f"a quantidade de tempreaturas acima de 30 são {resultado}" )
    