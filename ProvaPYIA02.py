# Programa para armazenar informações de contatos em um dicionário

agenda = {}

nome = input("Digite o nome do contato: ")
telefone = input("Digite o telefone do contato: ")  
email = input("Digite o email do contato: ")

agenda[nome] = {'telefone': telefone, 'email': email}

for chave, valor in agenda.items():
    print(f"Contato: {chave}")
    for info, detalhe in valor.items():
        print(f"  {info.capitalize()}: {detalhe}")