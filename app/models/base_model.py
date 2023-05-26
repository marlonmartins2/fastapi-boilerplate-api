from pydantic import BaseModel


class Paginador(BaseModel):
    page: int
    offset: int


class BaseDataModel(BaseModel):
    created_at: str
    updated_at: str
