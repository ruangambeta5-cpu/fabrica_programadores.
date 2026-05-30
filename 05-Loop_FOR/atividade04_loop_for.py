# autor: Ruan Lucas
# projeto: Loop For - variaveis de início e fim

numero = int(input("Digite a tabuada desejada: "))
numero_inicio = int(input("Digite o início da tabuada: "))
numero_fim = int(input("Digite o fim da tabuada: "))

# Loop For
for i in range (numero_inicio, numero_fim + 1):
    print(f'{numero} x {i} = {i * numero}')
   
