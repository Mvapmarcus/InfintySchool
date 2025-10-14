#Prova PYA02 - Exercício 2

# Lista de equipes e suas pontuações
equipes = [
    ('Equipe A', [10, 5, 9]),   
    ('Equipe B', [3, 7, 8]),   
    ('Equipe C', [5, 7, 7]),   
    ('Equipe D', [10, 8, 7])]

# Calculando a média das pontuações
medias = []
for equipe in equipes:
    nome, pontuacoes = equipe
    media = sum(pontuacoes) / len(pontuacoes)
    medias.append((nome, media))

# Ordenando as médias em ordem decrescente
medias.sort(key=lambda x: x[1], reverse=True)

# Criando a lista de classificação
classificacao = []
for equipe in medias:   
    classificacao.append(equipe)

# Exibindo a classificação final
for equipe in classificacao:
    print(f"Equipe: {equipe[0]}, Média: {equipe[1]:.2f}")

  

