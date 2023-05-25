from app.models.base_model import Paginador


def skip_limit(page: int, offset: int):
    """
    Wrapper para cria paginador

    Args:
        page (int): Numero da pagina
        offset (int): Limite de intem da pagina

    Returns:
        Paginador: Modelo do paginador
    """

    paginador = Paginador(page=page, offset=offset)

    return paginador
