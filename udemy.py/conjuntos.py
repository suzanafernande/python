# Nao possuem valores duplicados
# Nao possuem valores ordenados
# Nao sao acessados via indice, ou seja, conjuntos nao sao indexados
# Sao referenciados com chaves {}
# Diferenças entre Conjunto/Set e Mapa/Dicionario
    # Um dicionario tem chave/valor
    # Um conjunto tem apenas valor


# Definindo um conjunto:
# Forma 1 
conj = set({1,2,3,4,5,5,6,6,7,8,2,10})
print(conj)

# Forma 2
conj = {1,2,3,4,5,5}
print(conj)
print(type(conj))

# Forma 3 
conj = {'Caio abreu'}
print(conj)
print(type(conj))

if 3 in conj:
    print('Tem o 3')
else:
    print('Nao tem o 3')

# Importante lebar que, alem de nao termos valores duplicados, nao temos ordem
lista = [99,23,1,100,200,200,300]
print(f'Lista:{lista}')

tupla=(99,23,1,100,200,200,300)
print(f'Tupla:{tupla}')

dicionario = {}.fromkeys(lista,'dict')
print(f'Dicionario:{dicionario}')

conj = {99,23,1,100,200,200,300}
print(f'Conjunto:{conj}')

# Podemos misturar dados
conj = {1,'b',True,34.22,44}
for valor in conj:
    print(valor)

# O conjunto ordena os valores
conj = {99,2,1,100,200,200,300}
print(f'Conjunto:{conj}')


# Adicionando elementos em um conjunto
conj.add(4)
print(conj)

# Remover elementos em um conjunto
# Forma 1
conj.remove(4) # Nenhum valor é retornado
print(conj)

# Forma 2
conj.discard(100) # Se nao encontrado nao acontece nada
print(conj)

# Copiando um conjunto para outro

# Forma 1 - Deep Copy
novo_conj = conj.copy()
novo_conj.add(4)
print(novo_conj)
print(conj)

# Forma 2 - Shallow Copy
novo_conj = conj
novo_conj.add(100000)
print(novo_conj)
print(conj)

# Podemos remover todos os itens de um conjunto
# conj.clear()
# print(conj)

estudantes_python = {'marcos','patricia','ellen','pedro','julia','gui'}
estudantes_java = {'fernando','gustavo','julia','pedro'}

# Veja que alguns alunos que estudam Python tambem estudam Java
# Precisamos gerar um conjunto com nomes de estudantes unicos

# Forma 1 - utilizando union
unicos1 = estudantes_python.union(estudantes_java)
print(unicos1)

# Forma 2 - utilizando o caractere pipe |
unicos2 = estudantes_java | estudantes_python
print(unicos2)

# Gerar um conjunto de aluno que estao em ambos os cursos
# Forma 1 Utilizando intersection
ambos1=estudantes_python.intersection(estudantes_java)
print(ambos1)

# Forma 2 Utilizando o &
ambos2 = estudantes_java & estudantes_python
print(ambos2)

# Gerar um conjunto de estudantes que nao estao no outro curso
so_python=estudantes_python.difference(estudantes_java)
print(so_python)

so_java = estudantes_java.difference(estudantes_python)
print(so_java)

# Soma,Valor maximo, Valor minimo, Tamanho, se todos os valores forem int ou reais

print(sum(conj))
print(max(conj))
print(min(conj))
print(len(conj))