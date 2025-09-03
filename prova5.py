# Media de notas de alunos
# pdeir ao usuario a quantidade de alunos, e pra cada aluno, pedir nome e 3 notas
# implementar uma condicional para saber se foram aprovados considerando a media 7
# exibir  o nome do aluno a media e se foi aprovado ou reprovado
# ao final exibir a media da turma inteira


media_turma = 0
for i in range(int(input("Digite a quantidade de alunos: "))):
    nome = input("Nome do aluno: ")
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    nota3 = float(input("Nota 3: "))
    
    media = (nota1 + nota2 + nota3) / 3
    media_turma += media
    
    if media >= 7:
        status = "Aprovado"
    else:
        status = "Reprovado"
    
    print(f"Aluno: {nome}, Média: {media:.2f}, Status: {status}")
print(f"Média da turma: {media_turma / (i + 1):.2f}")

