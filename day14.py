# Gerenciador de tarefas

import os
import json

# Função para carregar tarefas
def carregar_tarefas():
    if os.path.exists("tarefas.json"):
        with open("tarefas.json", "r") as arquivo:
            return json.load(arquivo)
    return[]

# Exibe todas as tarefas
def listar_tarefas(tarefas):
    print("Tarefas:")
    for tarefa in tarefas:
        status = "Concluida" if tarefa['Concluída'] else "Pendente"
        print(f"ID: {tarefa["id"]}, Título: {tarefa['titulo']}, Status:{status}")

# Escreve no arquivo e salva tarefas
def salvar_tarefas(tarefas):
    with open("tarefas.json", "w") as arquivo:
            json.dump(tarefas, arquivo, indent=4)

# Gerar id
def gerar_id(tarefas):
    if tarefas:
        return tarefas[-1]["id"] + 1 #Tarefa com id 3, a proxima será adicionado em 1, virando a tarefa 4

# Adicionar tarefas
def adicionar_tarefas(tarefas):
    print("Adicionar nova tarefa")
    titulo = input("Titulo: ")
    descricao = input("Descrição ")

    tarefa = {
        "id": gerar_id(tarefas),
        "titulo": titulo,
        "descricao": descricao,
        "status": False
    }

    tarefas.append(tarefa)
    salvar_tarefas(tarefas)
    print("Tarefa inserida com sucesso!")

# Concluir tarefas
def concluir_tarefas(tarefas):
    try:
        id_tarefa = int(input("Digite o id da tarefa para concluir: "))
        for tarefa in tarefas:
            if tarefa["id"] == id_tarefa:
                if tarefa["status"]:
                    print("A tarefa já está concluida.")
                else:
                    tarefa['status'] = True
                    salvar_tarefas(tarefas)
                    print("Tarefa concluída com sucesso")
                return
        print("Tarefa não encontrada")
    except ValueError:
        print("ID inválido.")

# Menu principal
def menu():
    print("=== Gerenciador de tarefas ===")
    print("1. Adicionar tarefas")
    print("2. Listar tarefas")
    print("3. Concluir tarefas")
    print("4. Remover tarefas")
    print("5. Sair")
    return input("Escolha uma opção: ")

# Loop das ações
def main():
    tarefas = carregar_tarefas()
    while True:
        opcao = menu()

        if opcao == "1":
            adicionar_tarefas(tarefas)
        elif opcao == "2":
            listar_tarefas(tarefas)
        elif opcao == "3":
            concluir_tarefas(tarefas)
        #elif opcao == "4":
         #   excluir_tarefas(tarefas)
        elif opcao == "5":
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida!")


if __name__ == '__main__':
    main()