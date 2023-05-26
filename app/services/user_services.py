from app.database import db


def find_user(user_id: str):
    """
    Busca usuário por id

    :param user_id: id do usuário
    :return: usuário
    """
    user = db["users"].find_one({"id": user_id}, {"_id": 0})
    return user
