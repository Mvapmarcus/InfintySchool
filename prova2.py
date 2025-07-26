#Prova Infinity (IF,else, Elif): Verifica se um número é positivo, negativo ou zero
# Pede ao usuário um número e informa se é positivo, negativo ou zero

numero = float(input("Digite um número: "))

if numero > 0:
    print(f'O número é positivo.')   
elif numero < 0:
    print(f'O número é negativo.')   
else:
    print(f'O número é zero.')
    