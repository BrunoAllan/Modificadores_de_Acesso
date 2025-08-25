import os
import sys

class ContaBancaria:
    def __init__(self, titular, saldo, numero_conta):

        self.titular = titular

        self.__saldo = saldo

        self.numero_conta = numero_conta

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        if (self.__saldo >= valor):
            self.__saldo -= valor
        else:
            print ('Saldo insuficiente')

    def consultar_saldo(self):
        print(self.__saldo)

    def get_saldo(self):
        return self.__saldo
    
    def set_saldo(self, SaldoAtualizado):
        self.__saldo = SaldoAtualizado

    def exibir_extrato(self):
        print(self.titular)
        print(self.numero_conta)


c1 = ContaBancaria('Bruno', 900, 909)

def main():
    c1 = ContaBancaria('Bruno', 0, 100)
    while True:
        os.system('cls')
        print('---------------------------Menu----------------------------')
        print('1.Depositar|2.Sacar|3.ConsultarSaldo|4.ExibirExtrato|5.Get|6.Set|0.Sair')
        opcao = int(input('Escolha uma Opção:'))
        if opcao == 1:
            valor = float(input('Valor a depositar:'))
            c1.depositar(valor)
            input()
        
        elif opcao == 2:
            valor = float(input('Valor a sacar:'))
            c1.sacar(valor)
            input()

        elif opcao == 3:
            c1.consultar_saldo()
            input()

        elif opcao == 4:
            c1.exibir_extrato()
            input()
        
        elif opcao == 5:
            c1.get_saldo()
            input()

        elif opcao == 6:
            SaldoAtualizado = float(input('Valor a sacar:'))
            c1.set_saldo(SaldoAtualizado)
            input()

        elif opcao == 0:
            print("Saindo do sistema...")
            sys.exit()
           

        pass

if __name__ == "__main__":
    main()
