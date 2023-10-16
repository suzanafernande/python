tupla1 = (1,2,3,4,5,6)
print(tupla1)

tupla2 = 6,5,4,3,2,1
print(tupla2)

tupla3 = (4) # nao é uma tupla

tupla4 = (4, ) # é uma tupla

# Podemos chegar uma tupla dinamicamente em range(inicio,fim,passo)
tupla = tuple(range(11))
print(tupla)

# Desempacotamento de tupla
tupla = 'caio', 'abreu'
nome, sobrenome = tupla
print(nome)
print(sobrenome)

# Como a tupla é imutavel ela nao tem metodos para adição ou remoção de elementos por ser imutavel
tupla = 1,2,3,4,5,6
print(sum(tupla))
print(max(tupla))
print(min(tupla))
print(len(tupla))

# Concatenação de tuplas 
print(tupla1+tupla2) # Tuplas são imutaveis mas podemos sobrescrever seus valores 

# Verificar se determinado elemento esta contido na tupla
print(3 in tupla)

# Interando sobre uma tupla
for n in tupla: 
    print(n)

for indice, valor in enumerate(tupla):
    print(indice,valor)

# Contando elementos dentro de uma tupla
tupla= 'a','b','c','d','e','a','b'
print(tupla.count('e'))

# Dicas na utilização de tuplas
# Devemos utilizar tuplas SEMPRE que nao precisarmos modificar os dados contidos em uma coleção
# Exemplo 1

meses = 'Janeiro', 'Fevereiro', 'Março', 'Abril','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro'
print(meses)

# Iterar com while
i= 0

while i <len(meses):
    print(meses[i])
    i += 1

print(meses.index('Março')) # Tem que ser exatamente igual a string

nova = meses
print(nova)