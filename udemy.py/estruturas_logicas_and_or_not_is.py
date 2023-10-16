Estruturas lógicas: and (e), or (ou), not (não), is (e)

Operadores unários:
- not;
Operadores binários
- and, or, is

Regras de funcionamento

Para and ambos os valores precisam ser True
Para or um ou outro valor precisa True
Para not o valor do booleano invertido 

exemplo

resposta=int( input('Qual sua idade: ') )

if resposta>=18 and resposta <=65:
    print('Você é obrigado a votar!')
else:
    print('Você não é obrigado a votar')

exemplo

print('1. Idoso')
print('2. Gestante')
print('3. Cadeirante')
print('4. Nenhum destes')
resposta=int( input('Você é: ') )

if (resposta==1) or (resposta==2) or (resposta==3) :
    print('Você tem direito a fila prioritária')
else:
    print('Você não tem direito a nada. Vá pra fila e fique quieto')

exemplo

banda = input('Qual melhor banda do mundo? ')

if not banda=='rush':
    print('Herege!')
else:
    print('Correto, é o Rush!')
