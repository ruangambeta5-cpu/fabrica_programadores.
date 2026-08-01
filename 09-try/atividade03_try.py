# Autor: Ruan Lucas
# projeto: entendo tratamento de exceção Calculadora

try:
    valor1 = int(input("Digite o primeiro valor: "))
    valor2 = int(input("Digite o segundo valor: "))
    soma  = valor1 + valor2
    subtracao = valor1 - valor2
    multiplicacao = valor1 * valor2
    divisao = valor1 / valor2
    print(f"O resultado é: {soma}")
    print(f"O resultado é: {subtracao}")
    print(f"O resultado é: {multiplicacao}")
    print(f"O resultado é: {divisao}")
except ValueError:
    print("Digite valores numéricos válidos!")
except ZeroDivisionError:
    print("Erro: Divisão por zero não é permitida!")