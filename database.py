# Integrantes
# Nicolas Eiti Inohue - RM98057
# Marcel Prado Soddano - RM99841

from sqlalchemy import create_engine

from models import Base

def create_database():
    '''Cria e inicializa o banco de dados. Retorna um objeto de conexão com o banco de dados.'''
    engine = create_engine('oracle+oracledb://rm98057:250899@oracle.fiap.com.br/?service_name=orcl')
    Base.metadata.create_all(engine)
    return engine