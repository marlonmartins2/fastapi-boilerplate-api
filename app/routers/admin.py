from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

from app.services import find_user

router = APIRouter(prefix="/admin", tags=["Admin"])


@router.get("/get_user/{user_id}", description="Busca usuário por id")
def get_user(user_id: str):
    """
    Busca usuário por id

    :param user_id: id do usuário
    :return: usuário
    """
    user = find_user(user_id)
    if not user:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={
                "message": "Usuário não encontrado",
                "user_id": user_id,
            },
        )
    elif not user.get("is_admin"):
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "message": "Usuário não é admin",
                "user_id": user_id,
            },
        )

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=user,
    )
