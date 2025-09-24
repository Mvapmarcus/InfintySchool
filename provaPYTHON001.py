# Programa para registrar produtos comprados e fornecer um resumo da compra

compras = []

while True:
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: R$ "))
    compras.append({'nome': nome, 'preco': preco})
    
    continuar = input("Deseja adicionar mais produtos? (S/N): ").strip().upper()
    if continuar != 'S':
        break

# A) Total gasto na compra
total = sum(produto['preco'] for produto in compras)

# B) Quantidade de produtos que custam mais de R$1000
mais_de_1000 = sum(1 for produto in compras if produto['preco'] > 1000)

# C) Nome do produto mais barato
produto_mais_barato = min(compras, key=lambda x: x['preco'])['nome']

print("\nResumo da compra:")
print(f"Total gasto: R$ {total:.2f}")
print(f"Quantidade de produtos acima de R$1000: {mais_de_1000}")
print(f"Produto mais barato: {produto_mais_barato}")
