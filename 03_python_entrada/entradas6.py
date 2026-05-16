# autor: Ruan Lucas
# Projeto: entrada pelo usuario

peso = float(input('Digite o peso: '))
altura = float(input('Digite a altura: '))
imc = peso / (altura * altura)

# exibir o resultado com variável
print(f'seu IMC é: {imc:.2f}')
