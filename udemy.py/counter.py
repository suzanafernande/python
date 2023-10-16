from typing import Counter
lista =[1,1,1,1,1,1,1,3,4,4,4,4,4,4,4,5,5,5,5,6,6,6,6,6,7,7,7,7,7]

# Utilizando counter
res = Counter(lista)
print(type(res))
print(res)
# Para cada elemento da listar, o Counter criou uma chave e colocou como valor a quantidade de ocorrencias de cada elemento

print(Counter('Suzana Fernandes'))

print('----------------------------------')

texto = 'Senac Senac está oferecendo muitos cursos gratuitos na modalidade EAD, nas áreas de gestão, informática, games, idiomas e muito mais'
palavras = texto.split()
print(palavras)

print('----------------------------------')

res = Counter(palavras)
print(res)

print('----------------------------------')

# Encontrando as 5 palavras com mais ocorrencia no texto
print(res.most_common(5))