# Integrantes
# Nicolas Eiti Inohue - RM98057
# Marcel Prado Soddano - RM99841

from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, Sequence, String, Float, ForeignKey
import sqlalchemy

Base = sqlalchemy.orm.declarative_base()

class Loja(Base):
    '''Definição da classe Loja, que mapeia a tabela 'lojas' no banco de dados'''
    __tablename__ = 'lojas'
    id = Column(Integer, Sequence('sequencia_id'), primary_key=True)
    nome = Column(String(150), nullable=False)
    produtos = relationship('Produto', back_populates='loja', cascade='all, delete-orphan')

class Produto(Base):
    '''Definição da classe Produto, que mapeia a tabela 'produtos' no banco de dados'''
    __tablename__ = 'produtos'
    id = Column(Integer, Sequence('sequencia_id'), primary_key=True)
    id_loja = Column(Integer, ForeignKey('lojas.id'), nullable=False)
    nome = Column(String(150), nullable=False)
    descricao = Column(String(1000), nullable=False)
    valor = Column(Float, nullable=False)
    loja = relationship('Loja', back_populates='produtos')