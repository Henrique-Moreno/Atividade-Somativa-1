# =======================================
# Sistema de Gerenciamento Acadêmico
# Nome: [Henrique Alexandre De Souza Moreno]
# Curso: [Tecnologia em Análise e Desenvolvimento de Sistemas]
# =======================================

# Lista para armazenar os nomes dos estudantes
estudantes = []

# Função para exibir o menu principal
def menu_principal():
    print("***** MENU PRINCIPAL *****")
    print("(1) Estudantes")
    print("(2) Professores")
    print("(3) Disciplinas")
    print("(4) Turmas")
    print("(5) Matrículas")
    print("(9) Sair")
    print("***************************")

# Função para exibir o menu de operações dos estudantes
def menu_estudantes():
    print("***** [ESTUDANTES] MENU DE OPERAÇÕES *****")
    print("(1) Incluir.")
    print("(2) Listar.")
    print("(3) Atualizar.")
    print("(4) Excluir.")
    print("(9) Voltar ao menu principal.")
    print("******************************************")

# Função para incluir estudantes
def incluir_estudante():
    print("===== INCLUSÃO =====")
    nome = input("Informe o nome do estudante: ")
    estudantes.append(nome)
    print("Estudante adicionado com sucesso!")
    input("Pressione ENTER para continuar.")

# Função para listar estudantes
def listar_estudantes():
    print("===== LISTAGEM =====")
    if not estudantes:
        print("Não há estudantes cadastrados.")
    else:
        for estudante in estudantes:
            print(f"- {estudante}")
    input("Pressione ENTER para continuar.")

# Função principal do sistema
def sistema():
    while True:
        menu_principal()
        opcao = input("Informe a ação desejada: ")

        if opcao == "1":  
            while True:
                menu_estudantes()
                acao = input("Informe a ação desejada: ")

                if acao == "1":  
                    incluir_estudante()
                elif acao == "2":  
                    listar_estudantes()
                elif acao in ["3", "4"]:  
                    print("EM DESENVOLVIMENTO")
                    input("Pressione ENTER para continuar.")
                elif acao == "9":  
                    break
                else:
                    print("Opção inválida. Tente novamente.")

        elif opcao in ["2", "3", "4", "5"]:  
            print("EM DESENVOLVIMENTO")
            input("Pressione ENTER para continuar.")
        elif opcao == "9":  
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Iniciar o sistema
if __name__ == "__main__":
    sistema()
