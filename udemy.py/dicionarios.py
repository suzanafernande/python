# Criação de dicionario

# Forma 1 {'chave': o que esta na chave}
paises = {'BR':'Brasil','EUA':'Estados Unidos','PY':'Paraguai'}
print(paises)

# Forma 2
paises = dict(BR='Brasil',EUA='Estados Unidos',PY='Paraguai')
print(paises)

# Acessando elementos

# Forma 1 - Acessando via chave da mesma forma que lista/tupla
print(paises['BR'])
print(paises['EUA'])

# Forma 2 - Acessando via get
print(paises.get('PY'))
print(paises.get('ru','Não encontrado')) # Quando utilizado get se não for achado no dicionario ele retornara none ou o que digitado apos a busca
pais = paises.get('PY','Não encontrado')
print(f'Encontrei o pais {pais}')

# Forma 3
print('BR' in paises)
print('RU' in paises)
print('Estados Unidos' in paises)

# Podemos utilizar qualquer tipo de dado(int, float, string, boolean), como tambem listas,tuplas e chaves de dicionario
# Tuplas por exemplo são bastante interessantes de serem utilizadas como chave de dicionarios, pois as mesmas são imutaveis
localidades ={
    (35.6895, 39.6917): 'Escritorio em Tokio',
    (45.6895, 79.6917): 'Escritorio em NY',
    (25.6895, 19.6917): 'Escritorio em SP'
}
print(localidades)

# Adicionar elementos em um dicionario
receita = {'Jan':100, 'Fev':120,'Mar':300}
print(receita)

# Forma 1 - mais comum
receita['abr'] = 300
print(receita)

# Forma 2 
novo_dado = {'mai':500}
receita.update(novo_dado) # receita.update({'mai':500})
print(receita)

# Atualizando dados em um dicionario

# Forma 1
receita['mai']= 550
print(receita)

# Forma 2
receita.update({'mai':600})
print(receita)
# Atualizar e adicionar elementos é a mesma forma 
# Nao podemos aceitar chaves repetidos

# Remover dados de um dicionario

# Forma 1 
receita.pop('Mar')
print(receita)

# Forma 2
del receita['Fev'] # Se a chave nao existir, sera gerado um KeyError e nao retorna o valor quando removido diferente de pop
print(receita) 

# Exemplo
carrinho = []
produto1 ={'nome':'Playstation 4','quantidade':1,'preco':2300.00}
produto2 ={'nome':'God of war 4','quantidade':1,'preco':300.00}
carrinho.append(produto1)
carrinho.append(produto2)
print(carrinho)

# Copiando um dicionario para outro

# Forma 1 Deep copy
novo = receita.copy()
print(novo)
novo['d']=4
print(receita)
print(novo)

# Forma 2 Shallow copy(onde vai mudar o original tambem)
novo = receita
novo['d']=4
print(receita)
print(novo)

# Forma nao usual de criação de dicionario

outro = {}.fromkeys('a',2)
print(outro)

usuario = {}.fromkeys(['nome','pontos','email','profile'],'desconhecido')
print(usuario)

# O metodo fromkeys recebe dois parametros: um interavel e um valor, atribuindo a cada interavel o valor descrito

veja = {}.fromkeys('teste','valor')
print(veja)
veja = {}.fromkeys(range(1,11),'valor')
print(veja)