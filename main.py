# Integrantes
# Nicolas Eiti Inohue - RM98057
# Marcel Prado Soddano - RM99841

from database import create_database
from repository import Repository
from views import View
from controller import Controller

def main():
    '''Função principal para funcionamento da aplicação'''
    engine = create_database()
    repository = Repository(engine)
    view = View()
    controller = Controller(repository, view)

    while True:
        view.mostrar_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            controller.cadastrar_loja()
        elif opcao == "2":
            controller.cadastrar_produto()
        elif opcao == "3":
            controller.listar_lojas_produtos()
        elif opcao == "4":
            controller.deletar_loja()
        elif opcao == "5":
            controller.deletar_produto()
        elif opcao == "6":
            view.encerrar_programa()
            break
        else:
            view.opcao_invalida()

if __name__ == "__main__":
    main()