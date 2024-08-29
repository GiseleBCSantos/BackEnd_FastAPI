from sqlmodel import SQLModel, Field
from sqlalchemy import table

class Livro(SQLModel, table=True):
    id: int | None = Field(primary_key=True, default=None)
    titulo: str
    autor: str
    ano_publicacao: int
    isbs: int | None = Field(default=None)