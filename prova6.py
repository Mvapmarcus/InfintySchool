# Questão 5: Programa de login com limite de tentativas

# Definindo as credenciais corretas
usuario_correto = "admin"
senha_correta = "1234"

# Inicializando o contador de tentativas
tentativas = 3

# Loop principal do programa de login
while tentativas > 0:
    # Solicitando o nome de usuário e a senha ao usuário
    usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")

    # Verificando as credenciais
    if usuario == usuario_correto and senha == senha_correta:
        print("Bem-vindo ao sistema, admin!")
        break  # Sai do loop se as credenciais forem corretas
    else:
        tentativas -= 1
        if tentativas > 0:
            print(f"Credenciais incorretas. Você tem {tentativas} tentativas restantes.")
        else:
            for _ in range(3):
                print("Acesso bloqueado")