# Lista global para armazenar todas as tarefas
tarefas = []

def adicionar_tarefa(nome, descricao, prioridade, categoria):
    """Adiciona uma nova tarefa à lista de tarefas."""
    nova_tarefa = {
        'nome': nome,
        'descricao': descricao,
        'prioridade': prioridade,
        'categoria': categoria,
        'concluída': False  # Padrão: tarefa não concluída
    }
    tarefas.append(nova_tarefa)
    print(f"Tarefa '{nome}' adicionada com sucesso!")

def listar_tarefas():
    """Exibe todas as tarefas no formato de lista."""
    if not tarefas:
        print("Nenhuma tarefa encontrada.")
        return

    print("\n--- Lista de Tarefas ---")
    for i, tarefa in enumerate(tarefas):
        status = "✅ Concluída" if tarefa['concluída'] else "❌ Pendente"
        print(f"{i + 1}. Nome: {tarefa['nome']} | Prioridade: {tarefa['prioridade']} | Categoria: {tarefa['categoria']} | Status: {status}")
    print("------------------------")

def marcar_como_concluida(indice_tarefa):
    """Marca uma tarefa específica como concluída com base no índice."""
    try:
        # Ajusta o índice baseado em 0
        tarefa = tarefas[indice_tarefa - 1]
        if not tarefa['concluída']:
            tarefa['concluída'] = True
            print(f"Tarefa '{tarefa['nome']}' marcada como concluída.")
        else:
            print(f"Tarefa '{tarefa['nome']}' já está concluída.")
    except IndexError:
        print("Índice de tarefa inválido.")
    except ValueError:
        print("Entrada inválida. Digite um número.")

def exibir_por_criterio(criterio, valor):
    """Exibe tarefas filtradas por prioridade ou categoria."""
    resultados = [tarefa for tarefa in tarefas if tarefa[criterio].lower() == valor.lower()]
    
    if not resultados:
        print(f"Nenhuma tarefa encontrada com {criterio} '{valor}'.")
        return

    print(f"\n--- Tarefas com {criterio} '{valor}' ---")
    for tarefa in resultados:
        status = "✅ Concluída" if tarefa['concluída'] else "❌ Pendente"
        print(f"Nome: {tarefa['nome']} | Descrição: {tarefa['descricao']} | Status: {status}")
    print("------------------------------------------")

def menu_comandos():
    """Exibe o menu de comandos e lida com a interação do usuário."""
    while True:
        print("\n=== Menu de Gerenciamento de Tarefas ===")
        print("1. Adicionar tarefa")
        print("2. Listar todas as tarefas")
        print("3. Marcar tarefa como concluída")
        print("4. Exibir por prioridade")
        print("5. Exibir por categoria")
        print("6. Sair")
        print("========================================")

        escolha = input("Digite o número da opção desejada: ")

        if escolha == '1':
            nome = input("Digite o nome da tarefa: ")
            descricao = input("Digite a descrição: ")
            prioridade = input("Digite a prioridade (ex: alta, media, baixa): ")
            categoria = input("Digite a categoria (ex: trabalho, pessoal, estudos): ")
            adicionar_tarefa(nome, descricao, prioridade, categoria)
        elif escolha == '2':
            listar_tarefas()
        elif escolha == '3':
            listar_tarefas()
            if tarefas:
                indice = input("Digite o número da tarefa a ser marcada como concluída: ")
                marcar_como_concluida(int(indice))
        elif escolha == '4':
            prioridade = input("Digite a prioridade para filtrar: ")
            exibir_por_criterio('prioridade', prioridade)
        elif escolha == '5':
            categoria = input("Digite a categoria para filtrar: ")
            exibir_por_criterio('categoria', categoria)
        elif escolha == '6':
            print("Saindo do programa. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Inicia o menu de comandos
if __name__ == "__main__":
    menu_comandos()