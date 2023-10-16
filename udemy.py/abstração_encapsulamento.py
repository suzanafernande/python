# POO - Abstração e Encapsulamento

# Encapsular -> cápsula

class Conta:
    contador = 400
    def __init__(self,titular,saldo,limite):
        self.__numero = Conta.contador
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    def extrato(self):
        print(f'Saldo de {self.__saldo} do titular {self.__titular} com limite de {self.__limite}')

    def depositar(self,valor):
        if valor >0:
            self.__saldo += valor
        else:
            print('O valor precisa ser positivo')

    def sacar(self, valor):
        if valor >0:
            if self.__saldo >= valor:
                self.__saldo -=valor
            else:
                print('Saldo insuficiente')
        else:
            print('O valor deve ser positivo')
    def transferir(self,valor,conta_destino):
        # 1- Remover o valor da conta de origem
        self.__saldo -=valor
        self.__saldo -= 10 # Taxa de transferencia paga por quem realizou a transferencia

        # 2 - Adicionar o valor na conta de destino
        conta_destino.__saldo += valor
# Testando
conta1 = Conta('susu',150.00,1500)
conta2 = Conta('Angelina',300,2000)
# print(conta1.numero)
# print(conta1.titular)
# print(conta1.saldo)
# print(conta1.limite)
# Jeito sem segurança, logo colocamos __ antes das variaveis

# conta1.numero =42
# conta1.titular = 'xuxa'
# conta1.saldo = 999999999999999999
# conta1.limite= 999999999999999999999999999
# print(conta1.__dict__)

# conta1.extrato()
# print(conta1._Conta__titular) # Name Mangling

# conta1._Conta__titular = 'Angelina'
# conta1.depositar(150)
# print(conta1.__dict__)
# conta1.depositar(-400)
# print(conta1.__dict__)

conta1.extrato()
conta2.extrato()

conta2.transferir(100,conta1) # Transferir de uma conta pra outra

conta1.extrato()
conta2.extrato()