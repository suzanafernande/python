receita = {'jan':100,'fev':250,'mar':400}

# Interar sobre dicionario
for chave in receita:
    print(chave)
    print(receita[chave])

# Acessando as chaves
print(receita.keys())

# Acessando os valores
print(receita.values())

for valor in receita.values():
    print(valor)

# Desempacotamento do dicionario

for chave, valor in receita.items():
    print(f'chave = {chave} e valor={valor}')

# Se os valores forem todos int ou reais
print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita))