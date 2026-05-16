# autor: Ruan Lucas
# Projeto: Desvio Condicional

# Criação das variáveis
nome = input('Digite seu nome: ')
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura ** 2)
if imc < 18.5:
    print('Abaixo do peso')
else:
    print('Peso normal')

