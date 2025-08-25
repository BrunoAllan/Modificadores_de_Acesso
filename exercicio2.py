import os
import sys

class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def ligar(self):
        print('Veículo ligado')

class Carro(Veiculo):
    def __init__(self, marca, modelo, num_portas):
        super().__init__(marca, modelo)
        self.num_portas = num_portas
        
    def ligar(self):
        print('Carro ligado')

class Moto(Veiculo):
    def __init__(self, marca, modelo, cilindradas):
        super().__init__(marca, modelo)
        self.cilindradas = cilindradas
        
    def ligar(self):
        print('Moto ligada')

def main():
    v1 = Veiculo('Infinity', 'A1')
    c1 = Carro('Infinity', 'A2', 4)
    m1 = Moto('Infinity', 'A3', 250)

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('--------------------------- Menu ----------------------------')
        print('1. Ligar Veículo | 2. Ligar Carro | 3. Ligar Moto | 0. Sair')
        try:
            opcao = int(input('Escolha uma opção: '))
        except ValueError:
            continue

        if opcao == 1:
            v1.ligar()
            input("Pressione Enter para continuar...")

        elif opcao == 2:
            c1.ligar()
            input("Pressione Enter para continuar...")

        elif opcao == 3:
            m1.ligar()
            input("Pressione Enter para continuar...")

        elif opcao == 0:
            print("Saindo do sistema...")
            sys.exit()

if __name__ == "__main__":
    main()
