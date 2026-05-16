# autor: Ruan Lucas
# Projeto: Desvio Condicional

# Criação das variáveis
nome = input('Digite seu nome: ')
salario = float(input('Digite seu salário: '))
calculo = salario * 0.10
if calculo >= 100:
    print('entao voce tem dinheiro')
else:
    print('voce nao tem dinheiro')