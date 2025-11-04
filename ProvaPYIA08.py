# ProvaPYIA08 = Importando o módulo 'os' e listando arquivos e pastas no diretório atual

import os

def listar_arquivos_diretorio():
    """
    Importa o módulo 'os' e lista todos os arquivos e pastas no diretório atual.
    """
    try:
        conteudo_do_diretorio = os.listdir('.')
        
        print(f"Conteúdo do diretório atual ({os.getcwd()}):")
        print("-" * 30)

        for item in conteudo_do_diretorio:
            print(item)
            
        print("-" * 30)

    except FileNotFoundError:
        print("Erro: O diretório especificado não foi encontrado.")
    except PermissionError:
        print("Erro: Permissão negada para acessar o diretório.")
    
if __name__ == "__main__":
    listar_arquivos_diretorio()
    