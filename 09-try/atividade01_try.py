 # Autor: Ruan Lucas
# projeto: Entendo tratamento de exceção

num1 = input("Digite um número: ")
num2 = input("Digite outro número: ")

try:
    num1 = int(num1)
    num2 = int(num2)
    print(f"A soma é: {num1 + num2}")
except:
    print("Digite um número!")
