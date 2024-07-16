# Função para cadastrar um novo aluno
import os

# Inicialização de uma lista para armazenar os dados dos alunos
alunos = []

def cadastrar_aluno():
    """
    Função para cadastrar um novo aluno.
    Solicita ao usuário que insira os detalhes do aluno e adiciona-o à lista de alunos.
    """
    nome = input("Digite o nome do aluno: ")
    idade = int(input("Digite a idade do aluno: "))
    data_nascimento = input("Digite a data de nascimento do aluno (DD/MM/AAAA): ")
    matricula = input("Digite a matrícula do aluno: ")

    aluno = {
        'nome': nome,
        'idade': idade,
        'data_nascimento': data_nascimento,
        'matricula': matricula
    }
    alunos.append(aluno)
    print(f"Aluno {nome} cadastrado com sucesso!\n")

def consultar_alunos():
    """
    Função para consultar os alunos cadastrados.
    Percorre a lista de alunos e imprime os detalhes de cada um.
    """
    if not alunos:
        print("Nenhum aluno cadastrado.\n")
    else:
        for aluno in alunos:
            print(f"Nome: {aluno['nome']}, Idade: {aluno['idade']}, Data de Nascimento: {aluno['data_nascimento']}, Matrícula: {aluno['matricula']}")
        print("")

def excluir_aluno():
    """
    Função para excluir um aluno.
    Solicita ao usuário que insira a matrícula do aluno a ser excluído e remove-o da lista.
    """
    matricula = input("Digite a matrícula do aluno a ser excluído: ")
    for aluno in alunos:
        if aluno['matricula'] == matricula:
            alunos.remove(aluno)
            print(f"Aluno com matrícula {matricula} excluído com sucesso!\n")
            return
    print(f"Aluno com matrícula {matricula} não encontrado.\n")

def menu():
    """
    Função que implementa o menu principal do programa.
    Permite ao usuário navegar entre as opções de cadastrar, consultar e excluir alunos.
    """
    while True:
        print("1. Cadastrar Aluno")
        print("2. Consultar Alunos")
        print("3. Excluir Aluno")
        print("4. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            cadastrar_aluno()
        elif escolha == '2':
            consultar_alunos()
        elif escolha == '3':
            excluir_aluno()
        elif escolha == '4':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida, tente novamente.\n")

if __name__ == "__main__":
    menu()