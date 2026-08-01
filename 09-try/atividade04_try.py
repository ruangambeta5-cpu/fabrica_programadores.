# Autor: Ruan Lucas
# projeto: entendo tratamento de exceção IMC

try:
    peso = float(input("Digite o seu peso (kg): "))
    altura = float(input("Digite a sua altura (m): "))
    imc = peso / (altura ** 2)
    print(f"Seu IMC é: {imc:.2f}")
except ValueError:
    print("Erro: Digite valores numéricos válidos!")
except ZeroDivisionError:
    print("Erro: A altura não pode ser zero!")