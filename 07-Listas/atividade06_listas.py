# Autor: Ruan Lucas
# Projeto: Listas em Python
 #          0         1       2        3            4         5       
nomes = [ "Pele", "Maradona", "Messi", "Ronaldo" ] # neymar  #pedro (Mbappe)
print(*nomes)

 # adionado um nome na lista
 # para retirar as aspas e os colchetes, use *
nomes.append("pedro")
print(*nomes)

# adicionando um nome em uma posicao especifica
nomes.insert(4, "neymar")
print(*nomes)

# modificar uma pessoa da lista
nomes[5] = "Mbappe"
print(*nomes)

# removendo um nome na lista
del nomes[2]
print(*nomes)

# removendo um nome por texto
# buscar o nome e apagar  primeiro que aparecer
nomes.remove("Maradona")
print(*nomes)

# Usando o pop para mostrar o nome removido
# 0     1        2     3    
# pele ronaldo neymar mbappe 
removido = nomes.pop(1)
print(f'Após o pop foi removido o nome: {removido}',nomes)

# limpar a lista
nomes.clear()
print(f'Após o clear a lista é: {nomes}')