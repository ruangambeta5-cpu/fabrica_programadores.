# Autor: Ruan Lucas
# projeto: Entendo tratamento de exceção 
print("----Conversão de temperatura---")

try:
    celsius = float(input("Digite a temperatura em Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"A temperatura em Fahrenheit é: {fahrenheit:.2f}")
except ValueError:
    print("Erro: Digite um valor numérico válido!")
