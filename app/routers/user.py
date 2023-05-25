# *-* Coding: UTF-8 *-*

from fastapi import APIRouter


router = APIRouter(prefix="/user", tags=["User"])


@router.get("/")
def home():
    return {"message": "Hello World"}