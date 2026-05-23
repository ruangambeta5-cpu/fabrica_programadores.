# autor: Ruan Lucas
# Projeto: Desvio Condicional

# Criação das variáveis
nome = input('Digite seu nome: ')
telefone = input('Digite seu telefone: ')
cidade = input('Digite sua cidade: ')
salario = float(input('Digite seu salário: '))
if salario >= 1000:
    print('Você possui uma renda boa')
elif salario >= 700:
    print('Você tem um salário razoável')
elif salario >= 500:
    print('Você possui uma renda baixa')
else:
    print('Você possui uma renda muito baixa')