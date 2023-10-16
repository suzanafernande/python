# Lendo arquivos CSV
# CSV - Comma Separeted Values - Valores Separados por Vírgula

# Separador por virgula
# 1,2,3,4,5,6
# "geek", "university","python","ciencia",'dados'

# Separador por ponto e virgula
# "geek"; "university";"python";"ciencia";'dados'

# Separador por espaço
# 1 2 3 4 5 6
# "geek"  "university" "python" "ciencia" 'dados'

# Possivel de se trabalhar, mas não é o ideal (trabalhoso)

# with open('manipulando_JSON_CSV/lutadores.csv',encoding="utf8") as arquivo:
#     dado = arquivo.read()
#     # print(type(dado))
#     dado = dado.split(',')[2:]
#     print(dado)

# A linguagem Python possui duas formas diferente para ler dados em arquivos CSV:
# - reader -> Permite que iteremos sobre as linhas do arquivo CSV como listas;
# - DictReader -> Permitee que iteremos sobre as linhas do arquivo CSV como OrderedDicts;

# Reader
from csv import reader,DictReader

with open('manipulando_JSON_CSV/lutadores.csv',encoding="utf8") as arquivo:
    leitor_csv = reader(arquivo)
    next(leitor_csv) # Pula o cabeçalho 
    for linha in leitor_csv:
        # Cada linha é uma lista
        print(f'{linha[0]} nasceu no(a)(s) {linha[1]} e mede {linha[2]} centimetros')

print('--------------------------------------------------------------------------')
# DictReader

with open('manipulando_JSON_CSV/lutadores.csv',encoding="utf8") as arquivo:
    leitor_csv = DictReader(arquivo)
    # E se precissa utilizar outro separador que nao fosse a virgula 
    # leitor_csv = DictReader(arquivo,delimiter ='Serve para delimitar e como sera feito a separação no arquivo tendo como a virgula o padrão') 
    for linha in leitor_csv:
        # Cada linha é um OrderedDict
        print(f"{linha['Nome']} nasceu no(a)(s) {linha['País']} e mede {linha['Altura (em cm)']} centimetros ")