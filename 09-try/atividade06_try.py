# Autor: Ruan Lucas
# projeto: Entendo tratamento de exceção conversão de moeda

try:
    reais = float(input("Digite o valor em reais: "))
    dolar = reais / 5.08
    print(f"O valor em dólares é: {dolar:.2f}")
except ValueError:
    print("Erro: Digite um valor numérico válido!")
