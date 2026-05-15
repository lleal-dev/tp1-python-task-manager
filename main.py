# Importando bibliotecas necessárias #
from datetime import datetime

# Lista de funções para o gerenciador de tarefas #
# Menu Principal #
def menu_tarefas():
    """
    Exibe o menu de opções para o usuário. Inicia um loop para receber uma entrada do usuário e executar a função correspondente.

        Opções:
        1. Adicionar Tarefa: Chama a função adicionar_tarefa() para adicionar uma nova tarefa à lista.
        2. Listar Tarefas: Chama a função listar_tarefas() para exibir todas as tarefas atuais.
        3. Marcar Tarefa como Concluída: Exibe a lista de tarefas e solicita ao usuário o número da tarefa a ser marcada como concluída, chamando a função marcar_concluida().
        4. Excluir Tarefa: Exibe a lista de tarefas e solicita ao usuário o número da tarefa a ser excluída, chamando a função excluir_tarefa().
        5. Sair: Encerra o programa. 

        O loop continua enquanto o usuário inserir uma opção inválida ou saia na opção 5.     
    """

    print("\nGerenciador de Tarefas")
    print("1. Adicionar Tarefa")
    print("2. Listar Tarefas")
    print("3. Marcar Tarefa como Concluída")
    print("4. Excluir Tarefa")
    print("5. Sair")

    while True:
        opcao = int(input("\nEscolha uma opção: "))

        if opcao == 1:
            listar_tarefas()
            print("\nAdicionar nova tarefa")
            adicionar_tarefa()
        elif opcao == 2:
            listar_tarefas()
        elif opcao == 3:
            marcar_concluida()
        elif opcao == 4:
            excluir_tarefa()
        elif opcao == 5:
            print("\nSaindo do gerenciador de tarefas. Até logo!")
            break
        else:
            print("\nOpção inválida. Por favor, escolha uma opção válida.")

# Adicionar Tarefa #
def adicionar_tarefa():
    """
    Adiciona uma nova tarefa à lista de tarefas. 

    Titulo: O título da tarefa a ser adicionada.
    Criação: A data de criação da tarefa, definida como a data atual.
    Descrição: A descrição da tarefa a ser adicionada.
    Status: O status da tarefa a ser adicionada (Pendente/Concluída).
    Prazo: O prazo da tarefa a ser adicionada (dd/mm/aaaa).
    Urgência: A urgência da tarefa a ser adicionada (Baixa/Média/Alta).

    Retorna um dict com as informações da tarefa adicionada.       
    """

    titulo = input("Digite o título da tarefa: ")
    descricao = input("Digite a descrição da tarefa: ")
    status = input("Digite o status da tarefa (Pendente/Concluída): ")
    prazo = input("Digite o prazo da tarefa (dd/mm/aaaa): ")
    urgencia = input("Digite a urgência da tarefa (Baixa/Média/Alta): ")

    tarefa = {
        "titulo": titulo,
        "criacao": datetime.now().strftime("%d/%m/%Y"),
        "descricao": descricao,
        "status": status,
        "prazo": prazo,
        "urgencia": urgencia

    }
    tarefas.append(tarefa)
    print("\nTarefa adicionada com sucesso!")

# Listar Tarefas #
def listar_tarefas():
    """
    Caso não haja tarefas, informa que não há tarefas encontradas. Caso haja, exibe a lista de tarefas com seus títulos, descrições e prazos.

    Para melhor visualização, cada tarefa recebe um índice numérico, começando do 1, utilizamos um for para percorrer a lista de tarefas e exibir cada tarefa com seu índice, título, descrição e prazo.
    """

    if not tarefas:
        print("Nenhuma tarefa encontrada.")
        return

    print("\nLista de Tarefas:")
    for indice, tarefa in enumerate(tarefas, start=1):
        print(f"\n{indice}. {tarefa['titulo']}")
        print(f"   Descrição: {tarefa['descricao']}")
        print(f"   Criada em: {tarefa['criacao']}")
        print(f"   Status:    {tarefa['status']}")
        print(f"   Prazo:     {tarefa['prazo']}")
        print(f"   Urgência:  {tarefa['urgencia']}")

# Marcar Tarefa como Concluída #
def marcar_concluida():
    """
    Marca uma tarefa como concluída, removendo-a da lista.

    Exibe a lista de tarefas e solicita ao usuário o número
    da tarefa. Repete a solicitação enquanto o número for inválido.

    """
    if not tarefas:
        print("Nenhuma tarefa encontrada.")
        return
    listar_tarefas()
    while True:
        concluida = int(input("\nDigite o número da tarefa a ser concluída: "))
        if 1 <= concluida <= len(tarefas):
            break
        else:
            print(f"Digite um número entre 1 e {len(tarefas)}.")
    tarefa_concluida = tarefas.pop(concluida - 1)
    print(f"\nTarefa '{tarefa_concluida['titulo']}' concluída e removida da lista!")

# Excluir Tarefa #
def excluir_tarefa():
    """
    Exclui uma tarefa da lista.

    Exibe a lista de tarefas e solicita ao usuário o número da tarefa a ser excluída. Repete a solicitação enquanto o número for inválido.
    """

    if not tarefas:
        print("Nenhuma tarefa encontrada.")
        return
    listar_tarefas()
    while True:
        excluida = int(input("\nDigite o número da tarefa a ser excluída: "))
        if 1 <= excluida <= len(tarefas):
            break
        else:
            print(f"Digite um número entre 1 e {len(tarefas)}.")
    tarefa_excluida = tarefas.pop(excluida - 1)
    print(f"\nTarefa '{tarefa_excluida['titulo']}' excluída da lista!")

# Executar o programa #
tarefas = []
menu_tarefas()