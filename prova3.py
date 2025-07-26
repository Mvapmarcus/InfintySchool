# Prova infinity (FOR): Soma de números pares
# Pede ao usuário 2 números e imprime a soma dos números pares
# Informa se não há números pares no intervalo caso não existam

soma = 0
numero_1 = int(input('Digite o primeiro número: '))
numero_2 = int(input('Digite o segundo número: '))

for i in range(min(numero_1, numero_2), max(numero_1, numero_2) + 1):
    if i % 2 == 0:  # Verifica se o número é par
        soma += i
if soma > 0:
    print(f'A soma dos números pares no intervalo é: {soma}')
else:
    print('Não há números pares no intervalo fornecido.')