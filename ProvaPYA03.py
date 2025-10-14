# ProvaPYA03 - Exercício 3
# Sistema para gerenciar informações de alunos em uma escola.

alunos = []

while True:
    nome = input("Digite o nome do aluno: ")
    idade = int(input("Digite a idade do aluno: "))
    nota_matematica = float(input("Digite a nota de Matemática: "))
    nota_ciencias = float(input("Digite a nota de Ciências: "))
    nota_historia = float(input("Digite a nota de História: "))
    
    aluno = {
        'nome': nome,
        'idade': idade,
        'notas': (nota_matematica, nota_ciencias, nota_historia)
    }
    
    alunos.append(aluno)
    
    continuar = input("Deseja adicionar mais alunos? (S/N): ").strip().upper()
    if continuar != 'S':
        break
# Exibindo informações dos alunos e calculando médias
melhor_media = -1
for aluno in alunos:
    nome = aluno['nome']
    idade = aluno['idade']
    notas = aluno['notas']
    media = sum(notas) / len(notas)
    
    print(f"\nNome: {nome}")
    print(f"Idade: {idade}")
    print(f"Notas: Matemática: {notas[0]}, Ciências: {notas[1]}, História: {notas[2]}")
    print(f"Média das notas: {media:.2f}")
    
    if media > melhor_media:
        melhor_media = media
        melhor_aluno = nome 
print(f"\nAluno com melhor média: {melhor_aluno} com média {melhor_media:.2f}")