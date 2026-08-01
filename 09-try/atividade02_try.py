 # Autor: Ruan Lucas
# projeto: Entendo tratamento de exceção

try:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    soma = num1 + num2
    print(f"A soma é: {soma}")
except:
    print("Digite numero correto!")
