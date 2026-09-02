def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: Divisão por zero!"
    return a / b

def calculadora():
    while True:
        print("\n--- CALCULADORA EM PYTHON ---")
        print("1. Somar")
        print("2. Subtrair")
        print("3. Multiplicar")
        print("4. Dividir")
        
        # Exibe a linha em branco e o texto exatamente como você pediu
        opcao = input("\nDigite uma opção: ")
            
        if opcao in ['1', '2', '3', '4']:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            
            if opcao == '1':
                print(f"\nResultado: {somar(num1, num2)}")
            elif opcao == '2':
                print(f"\nResultado: {subtrair(num1, num2)}")
            elif opcao == '3':
                print(f"\nResultado: {multiplicar(num1, num2)}")
            elif opcao == '4':
                print(f"\nResultado: {dividir(num1, num2)}")
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    calculadora()
