# autor: Ruan Lucas
# Projeto: Desvio Condicional

# Criação das variáveis
nome= input("Digite seu nome: ")
peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))

# Cálculo do IMC
imc = peso / (altura ** 2)

if imc < 18.5:
    print('Abaixo do peso')
elif imc >= 18.5:
    print('Peso normal')
elif imc >= 25:
    print('Sobrepeso')  
elif imc >= 30:
    print('Obesidade grau I')
elif imc >= 35:
    print('Obesidade grau II')
else:
    print('Obesidade grau III')


