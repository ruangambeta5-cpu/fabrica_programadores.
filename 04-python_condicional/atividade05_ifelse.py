# autor: Ruan Lucas
# Projeto: Desvio Condicional

# Criação das variáveis
nome = input('Digite seu nome: ')
nota = float(input('Digite sua nota: '))
if nota >= 6:
    print('Aprovado')
elif nota >= 4:
    print('Recuperação')
else:
    print('Reprovado')