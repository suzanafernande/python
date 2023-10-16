#Entrada de dados
print("Qual seu nome?")
nome = input () #input -> entrada 

#Exemplo de print atual
print(f'Seja bem-vindo(a) {nome}')

print('Qual é a sua idade?')
idade = input ()

print(f'A {nome} tem {idade} anos')

# int(idade) -> cast 
Cast é a 'conversão' de um tipo de dado para outro.

print(f'A {nome} nasceu em {2018 - int(idade)}')

OBS: Ao converter um float para int perdemos a precisão