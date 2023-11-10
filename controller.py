# Integrantes
# Nicolas Eiti Inohue - RM98057
# Marcel Prado Soddano - RM99841

from models import Loja

class Controller:
    '''Classe responsável por controlar a lógica de negócios do programa.'''
    def __init__(self, repository, view):
        '''Inicializa o controlador com instâncias do repositório e da visualização.'''
        self.repository = repository
        self.view = view

    def cadastrar_loja(self):
        try:
            print("==Cadastro de loja==")
            nome_loja = input("Insira o nome da loja: ")
            if not nome_loja:
                raise ValueError("O nome da loja não pode estar vazio.")
            self.repository.cadastrar_loja(nome_loja)
            self.view.mostrar_mensagem(f"Loja: {nome_loja}\nCadastrada com sucesso!")
        except ValueError as ve:
            print(f"Erro: {ve}")
        except Exception as e:
            print(f"Erro inesperado: {e}")

    def cadastrar_produto(self):
        '''Realiza o cadastro de um novo produto associado a uma loja no banco de dados.'''
        try:
            print("==Cadastro de produto==")
            try:
                id_loja = int(input("Insira o ID da loja para cadastrar o produto: "))
            except ValueError:
                self.view.mostrar_mensagem("O ID da loja deve ser um número inteiro válido.")
                return
            loja = self.repository.session.query(Loja).filter(Loja.id == id_loja).first()
            if not loja:
                self.view.mostrar_mensagem("Loja não existe.")
                return
            nome_produto = input("Insira o nome do produto: ")
            desc_produto = input("Insira a descrição do produto: ")
            try:
                valor = float(input("Insira o valor do produto: "))
            except ValueError:
                self.view.mostrar_mensagem("O valor do produto deve ser um número válido.")
                return
            self.repository.cadastrar_produto(id_loja, nome_produto, desc_produto, valor)
            self.view.mostrar_mensagem("Produto cadastrado com sucesso!")
        except Exception as e:
            self.view.mostrar_mensagem(f"Erro inesperado: {e}")


    def listar_lojas_produtos(self):
        ''' Lista todas as lojas e seus produtos no banco de dados.'''
        lojas = self.repository.listar_lojas_produtos()
        self.view.mostrar_lojas_produtos(lojas)

    def deletar_loja(self):
        '''Deleta uma loja existente no banco de dados.'''
        try:
            print("Lojas cadastradas: ")
            lojas = self.repository.listar_lojas_produtos()
            self.view.mostrar_lojas_produtos(lojas)
            while True:
                try:
                    id_loja = int(input("Insira o ID da loja que deseja deletar: "))
                    break
                except ValueError:
                    print("Por favor, insira um ID válido (número inteiro).")

            loja_a_deletar = next((loja for loja in lojas if loja.id == id_loja), None)
            if loja_a_deletar:
                self.repository.deletar_loja(id_loja)
                self.view.mostrar_mensagem(f"Loja ID: {id_loja}\nDeletada com sucesso!")
            else:
                raise ValueError(f"A loja com ID {id_loja} não existe.")
        except ValueError as ve:
            print(f"Erro: {ve}")
        except Exception as e:
            print(f"Erro inesperado: {e}")

    def deletar_produto(self):
        '''Deleta um produto de uma loja específica no banco de dados.'''
        try:
            print("Lojas e Produtos: ")
            lojas = self.repository.listar_lojas_produtos()
            self.view.mostrar_lojas_produtos(lojas)
            id_loja = int(input("Insira o ID da loja da qual deseja deletar um produto: "))
            loja = self.repository.session.query(Loja).get(id_loja)
            if loja:
                if loja.produtos:
                    for produto in loja.produtos:
                        print(f"ID: {produto.id} - Produto: {produto.nome}")
                    id_produto = int(input("Insira o ID do produto que deseja deletar: "))
                    if not any(produto.id == id_produto for produto in loja.produtos):
                        raise ValueError("ID do produto inválido.")
                    self.repository.deletar_produto(id_produto)
                    self.view.mostrar_mensagem(f"Produto ID {id_produto} deletado com sucesso!")
                else:
                    self.view.mostrar_mensagem("Nenhum produto cadastrado para esta loja.")
            else:
                self.view.mostrar_mensagem(f"Loja ID {id_loja} não encontrada.")
        except ValueError as ve:
           print(f"Erro: {ve}")
        except Exception as e:
            print(f"Erro inesperado: {e}")
