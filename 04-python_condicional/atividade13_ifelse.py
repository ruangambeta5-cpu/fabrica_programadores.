# autor: Ruan Lucas
# Projeto: Desvio Condicional

# Criação das variáveis
nome = input('Digite seu nome: ')
pedidos = int(input('escolha seu pedido: 1 = cafe, 2 = cha, 3 = suco: '))
if pedidos == 1:
    print(f'{nome}, você escolheu café.')
elif pedidos == 2:
    print(f'{nome}, você escolheu chá.')
elif pedidos == 3:
    print(f'{nome}, você escolheu suco.')
else:
    print('Opção inválida')