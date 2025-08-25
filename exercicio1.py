import os
import sys

# Classe que representa uma conta bancária
class ContaBancaria:
    def __init__(self, titular, saldo, numero_conta):
        # Nome do titular da conta
        self.titular = titular
        # Atributo privado (não acessível diretamente fora da classe)
        self.__saldo = saldo
        # Número da conta
        self.numero_conta = numero_conta

    # Método para adicionar valor ao saldo
    def depositar(self, valor):
        self.__saldo += valor

    # Método para retirar valor do saldo, se houver fundos suficientes
    def sacar(self, valor):
        if (self.__saldo >= valor):
            self.__saldo -= valor
        else:
            print('Saldo insuficiente')

    # Método para exibir o saldo diretamente
    def consultar_saldo(self):
        print(self.__saldo)

    # Método getter para retornar o saldo
    def get_saldo(self):
        return self.__saldo
    
    # Método setter para atualizar o saldo manualmente
    def set_saldo(self, SaldoAtualizado):
        self.__saldo = SaldoAtualizado

    # Método para exibir informações básicas da conta
    def exibir_extrato(self):
        print(self.titular)
        print(self.numero_conta)


# Criação de uma conta bancária inicial (fora do main, não usada depois)
c1 = ContaBancaria('Bruno', 900, 909)

def main():
    # Conta criada dentro do main, usada pelo menu
    c1 = ContaBancaria('Bruno', 0, 100)

    # Loop principal do menu
    while True:
        # Limpa a tela (no Windows)
        os.system('cls')

        # Exibe o menu
        print('--------------------------- Menu ----------------------------')
        print('1.Depositar | 2.Sacar | 3.Consultar Saldo | 4.Exibir Extrato | 5.Get | 6.Set | 0.Sair')

        # Recebe a opção escolhida
        opcao = int(input('Escolha uma Opção:'))

        # Depositar
        if opcao == 1:
            valor = float(input('Valor a depositar:'))
            c1.depositar(valor)
            input()

        # Sacar
        elif opcao == 2:
            valor = float(input('Valor a sacar:'))
            c1.sacar(valor)
            input()

        # Consultar saldo (print direto no método)
        elif opcao == 3:
            c1.consultar_saldo()
            input()

        # Exibir extrato (titular + conta)
        elif opcao == 4:
            c1.exibir_extrato()
            input()

        # Usando getter (retorna saldo, mas não imprime aqui → não aparece na tela)
        elif opcao == 5:
            c1.get_saldo()
            input()

        # Usando setter (atualiza o saldo manualmente)
        elif opcao == 6:
            SaldoAtualizado = float(input('Novo valor para o saldo:'))
            c1.set_saldo(SaldoAtualizado)
            input()

        # Sair do programa
        elif opcao == 0:
            print("Saindo do sistema...")
            sys.exit()

        pass

# Ponto de entrada do programa
if __name__ == "__main__":
    main()
