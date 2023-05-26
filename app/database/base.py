from pymongo import MongoClient

from app.settings import settings


class Indices(type):
    """
    Cria index para todas as coleções que herdam essa classe
    """

    def __init__(cls, *args, **kwargs):
        if hasattr(cls, "indices"):
            cls.get_instancia().create_indexes(cls.indices)

        super().__init__(*args, **kwargs)


class BaseConexao:
    if settings.MONGO_SSL is True:
        conexao = MongoClient(
            settings.MONGO_URL,
            tls=True,
            tlsCAFile=settings.PATH_CERT,
            tlsAllowInvalidHostnames=True,
            retryWrites=False,
            directConnection=True,
        )
    else:
        conexao = MongoClient(settings.MONGO_URL)


class BaseDB(BaseConexao, metaclass=Indices):
    database = settings.DATABASE_ENVIRONMENT


db = BaseDB.conexao[BaseDB.database]
