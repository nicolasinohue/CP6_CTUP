# Integrantes
# Nicolas Eiti Inohue - RM98057
# Marcel Prado Soddano - RM99841

class View:
    """Classe responsável por exibir informações ao usuário."""
    @staticmethod
    def mostrar_menu():
        '''Método estático para exibir o menu principal'''
        print("\n|MENU PRINCIPAL|")
        print("1 - Cadastrar loja")
        print("2 - Cadastrar produto")
        print("3 - Listar lojas e produtos")
        print("4 - Deletar loja")
        print("5 - Deletar produto de uma loja")
        print("6 - Encerrar")

    @staticmethod
    def opcao_invalida():
        '''Método estático para exibir uma mensagem quando uma opção inválida é inserida'''
        print("Opção inválida. Tente novamente.")

    @staticmethod
    def encerrar_programa():
        '''Método estático para exibir uma mensagem de encerramento do programa'''
        print("Encerrando o programa. Até mais!")

    @staticmethod
    def mostrar_lojas_produtos(lojas):
        '''Método estático para exibir a lista de lojas e produtos'''
        for loja in lojas:
            print(f"\nID: {loja.id} Loja: {loja.nome}")
            if loja.produtos:
                for produto in loja.produtos:
                    print(f"- Produto: {produto.nome}")
                    print(f"Descrição: {produto.descricao}")
                    print(f"Valor: R${produto.valor}")
            else:
                print("Nenhum produto cadastrado.")

    @staticmethod
    def mostrar_mensagem(mensagem):
        '''Método estático para exibir uma mensagem genérica'''
        print(mensagem)
