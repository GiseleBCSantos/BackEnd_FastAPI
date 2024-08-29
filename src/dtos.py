from pydantic import BaseModel

class RequisicaoLivro(BaseModel):
    titulo: str
    autor: str
    ano_publicacao: int
