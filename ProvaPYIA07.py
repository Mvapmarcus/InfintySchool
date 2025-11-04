# Prova 07 - Função para somar o numero de dois DADOS aleatiórios

import random

def somar_dados():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    soma = dado1 + dado2
    return soma , dado1, dado2

def menu_comandos():
    while True:
        print("\n=== Menu de Soma de Dados ===")
        print("1. Somar dois dados")
        print("2. Sair")
        escolha = input("Digite o número da opção desejada: ")

        if escolha == '1':
            resultado, dado1, dado2 = somar_dados()
            print(f"A soma dos dois dados é: {resultado} .Dados: {dado1} e {dado2}")
        elif escolha == '2':
            break
        else:
            print("Opção inválida. Tente novamente.")
if __name__ == "__main__":
    menu_comandos()