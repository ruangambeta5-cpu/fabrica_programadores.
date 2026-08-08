# autor: Ruan Lucas
# Projeto: Calculadora de IMC
# Criação das variáveis
nome= input("Digite seu nome: ")
peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))

# Cálculo do IMC
imc = peso / (altura ** 2)
print(f"{nome}, seu IMC é: {imc:.2f} ")

if imc < 18.5:
    print(f"{nome}, você está abaixo do peso.")
elif imc >= 25 and imc < 30:
    print(f"{nome}, você está com peso normal.")
elif imc >= 30 and imc < 35:
    print(f"{nome}, você está com sobrepeso, consulte um médico para avaliação.")
elif imc >= 35 and imc < 40:
    print(f"{nome}, você está com obesidade grau I, consulte um médico para avaliação.")
elif imc >= 40:
    print(f"{nome}, você está com obesidade grau II, é importante procurar um médico para avaliação.")
else:
    print(f"{nome}, você está com obesidade grave.")