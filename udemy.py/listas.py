# array em pythin é dinamico []
lista1 = [1,2,2,2,2,3,4,5,6,7,8,9,3]
lista2 = ['suzana','caio','mali','tania','pedro','joao']
lista3 =[]
lista4 = list(range(11))
lista5 = list('Suzana Fernandes')

# Usar lista com if
num = 10
if num in lista1:
    print(f'Achei o {num} na lista')
else:
    print(f'Nao achei o {num} na lista')

# Ordernar a lista
lista1.sort()
print(lista1)

# contar numero de ocorrencias em uma lista
print(lista1.count(2))
print(lista5.count('a'))

# Adicionar elementos em listas
# Só podemos adicionar um elemnto por vez
print(lista1)
lista1.append(42)
print(lista1)

# Adicionando mais de um elemento
lista1.append([8,3,1])
lista1.append(lista2)
print(lista1)

if [8,3,1] in lista1:
    print('Encontrei a lista')
else:
    print('Nao encontrei a lista')

# Coloca cada elemento na lista como valor adicional 
lista1.extend([123,44,67])
print(lista1)

# Adicionar a partir de um indice
lista1.insert(2,'Novo elemento')
print(lista1)

# Soma de lista
lista6 = lista1 +lista2
# print(lista6)

# Inverter a lista
# uma forma é fazendo -> lista1(::-1)
lista1.reverse()
print(lista1)

# Copiar uma lista
lista6 = lista2.copy()
print(lista6)

# Removendo o ultimo elemento da lista e retorna o numero removido
lista2.pop()
print(lista2)

# Removendo pelo indice, os elementos a direita sao movidos para a esquerda
lista2.pop(2)
print(lista2)

# Remover todos os elementos
# lista2.clear()
print(lista2)

# Repetir elementos em uma lista
nova = [1,2,3]
print(nova)
nova *= 3
print(nova)

# Converter uma string para uma lista
nome = 'Suzana Fernandes Soares'
nome =nome.split()
print(nome)

nome2 = 'Suzana,Fernandes,Soares'
nome2 =nome2.split(',')
print(nome2)

# Convertendo uma lista em uma string 
print(' '.join(nome2))

print('$'.join(nome2))

# Podemos adicionar qualquer elemento nas listas

# Iterando sob listas
# Exemplo 1
print('----------------------------')
numeros = [1,2,3,4,5,6,7,8,9,10]
for elemento in lista2:
    print(elemento)

soma = 0
for elemento in numeros:
    print(elemento)
    soma += elemento
print(soma)

# Exemplo 2 utilizando while
carrinho =[]
produto =''

# while produto != 'sair':
#     print("Adicio um produto na lista ou digite 'sair' para sair:")
#     produto= input()
#     if produto != 'sair':
#         carrinho.append(produto)

# for produto in carrinho:
#     print(produto)

# Utilizando variaveis em listas
print(numeros)
print(numeros[-1]) # Vai pegar o ultimo elemento da lista

cores = ['verde','amarelo','vermelho']
for cor in cores:
    print(cor)

print('----------------')

indice = 0 
while indice < len(cores):
    print(cores[indice])
    indice += 1

print('----------------')

# Gerar indice em um for
for indice, cor in enumerate(cores):
    print(indice,cor)

# Outros metodos nao tao importantes

# Encontrar um indice de um elemento na lista
# Retorna o primeiro elemento encontrado
print(numeros)
print(numeros.index(5))

# Ira procurar a partir do indice citado index(valor_que_busca,indice_inicial)
print(numeros.index(5,1))

# Procure o numero 8 entre os indices 6,8
print(numeros.index(8,6,8))

# Revisão de slicing com o parametro inicio [indice_inicial:indice_final:vai de 'x' em 'x']
print(numeros[1:8:2])
print(numeros[::-1])

print('-------------------')

print(sum(numeros)) #soma da lista
print(max(numeros)) #maior valor da lista
print(min(numeros)) #menor valor da lista
print(len(numeros)) #tamanho da lista 

# Transformando em tupla
tupla = tuple(numeros)
print(tupla)
print(type(tupla))

# Copia de listas (Shallow copy e Deep copy)
# Forma 1
nova = numeros.copy() # é diferente de nova = numeros pois nao ira receber uma copia da lista e sim a copia do campo de memoria da lista(numeros)
print(nova)
nova.append(4)

print(numeros)
print(nova)