# Integrantes
# Nicolas Eiti Inohue - RM98057
# Marcel Prado Soddano - RM99841

from sqlalchemy.orm import sessionmaker
from models import Loja, Produto

class Repository:
    def __init__(self, engine):
        '''Inicializa uma sessão de banco de dados usando o SQLAlchemy'''
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def cadastrar_loja(self, nome):
        '''Cria uma nova instância de Loja com o nome fornecido, adiciona a nova loja à sessão e confirma as alterações no banco de dados'''
        nova_loja = Loja(nome=nome)
        self.session.add(nova_loja)
        self.session.commit()

    def cadastrar_produto(self, id_loja, nome, descricao, valor):
        '''Cria uma nova instância de Produto associada à loja fornecida, adiciona o novo produto à sessão e confirma as alterações no banco de dados'''
        novo_produto = Produto(id_loja=id_loja, nome=nome, descricao=descricao, valor=valor)
        self.session.add(novo_produto)
        self.session.commit()

    def listar_lojas_produtos(self):
        '''Retorna todas as instâncias da classe Loja presentes no banco de dados'''
        return self.session.query(Loja).all()

    def deletar_loja(self, id_loja):
        '''Obtém a instância da loja com o ID fornecido, se a loja existir, remove-a da sessão e confirma as alterações no banco de dados'''
        loja = self.session.get(Loja, id_loja)
        if loja:
            self.session.delete(loja)
            self.session.commit()

    def deletar_produto(self, id_produto):
        '''Obtém a instância do produto com o ID fornecido, se o produto existir, remove-o da sessão e confirma as alterações no banco de dados'''
        produto = self.session.get(Produto, id_produto)
        if produto:
            self.session.delete(produto)
            self.session.commit()