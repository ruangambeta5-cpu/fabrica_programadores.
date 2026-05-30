# Autor: Ruan Lucas
# Projeto: Loop while

numero = int(input("Digite a tabuada desejada: "))
inicio = int(input("Digite o início da tabuada: "))
fim = int(input("Digite o fim da tabuada: "))
i = inicio

while i <= fim:
    print(f'{numero} x {i} = {i * numero}')
    i = i + 1
