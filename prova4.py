# Jogo de Adivinhação
# O usuário tenta adivinhar um número secreto com 3 tentativas

numero_secreto = 7
tentativas = 3

while tentativas > 0:
    palpite = int(input(f'Digite seu palpite (você tem {tentativas} tentativas restantes): '))
    
    if palpite == numero_secreto:
        print('Parabéns! Você acertou o número!')
        break
    else:
        tentativas -= 1
        print('Tente novamente!')

if tentativas == 0:
    print('Suas tentativas acabaram. O número era', numero_secreto) 