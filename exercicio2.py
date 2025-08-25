import os
import sys

# Classe base que representa um veículo genérico
class Veiculo:
    def __init__(self, marca, modelo):
        # Atributos comuns a qualquer veículo
        self.marca = marca
        self.modelo = modelo

    # Método comum a todos os veículos
    def ligar(self):
        print('Veículo ligado')

# Classe derivada que representa um carro
class Carro(Veiculo):
    def __init__(self, marca, modelo, num_portas):
        # Chama o construtor da classe mãe (Veiculo)
        super().__init__(marca, modelo)
        # Atributo específico do carro
        self.num_portas = num_portas
        
    # Sobrescreve o método ligar
    def ligar(self):
        print('Carro ligado')

# Classe derivada que representa uma moto
class Moto(Veiculo):
    def __init__(self, marca, modelo, cilindradas):
        # Chama o construtor da classe mãe (Veiculo)
        super().__init__(marca, modelo)
        # Atributo específico da moto
        self.cilindradas = cilindradas
        
    # Sobrescreve o método ligar
    def ligar(self):
        print('Moto ligada')

# Função principal que controla o fluxo do programa
def main():
    # Criação de objetos das classes
    v1 = Veiculo('Infinity', 'A1')
    c1 = Carro('Infinity', 'A2', 4)
    m1 = Moto('Infinity', 'A3', 250)

    # Loop infinito do menu
    while True:
        # Limpa a tela (compatível com Windows e Linux)
        os.system('cls' if os.name == 'nt' else 'clear')
        
        # Exibição do menu
        print('--------------------------- Menu ----------------------------')
        print('1. Ligar Veículo | 2. Ligar Carro | 3. Ligar Moto | 0. Sair')

        # Captura da opção escolhida pelo usuário
        try:
            opcao = int(input('Escolha uma opção: '))
        except ValueError:
            # Caso o usuário digite algo inválido, volta ao menu
            continue

        # Executa ações de acordo com a opção escolhida
        if opcao == 1:
            v1.ligar()  # Liga veículo genérico
            input("Pressione Enter para continuar...")

        elif opcao == 2:
            c1.ligar()  # Liga carro
            input("Pressione Enter para continuar...")

        elif opcao == 3:
            m1.ligar()  # Liga moto
            input("Pressione Enter para continuar...")

        elif opcao == 0:
            print("Saindo do sistema...")
            sys.exit()  # Encerra o programa

# Ponto de entrada do programa
if __name__ == "__main__":
    main()
