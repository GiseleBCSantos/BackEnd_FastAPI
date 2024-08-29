from fastapi import APIRouter, status, HTTPException
from models import Livro
from dtos import RequisicaoLivro
from sqlmodel import Session, select
from database import get_engine

router = APIRouter()

@router.post('/', 
             response_model=Livro, 
             status_code=status.HTTP_201_CREATED)
def livro_create(requisicao: RequisicaoLivro):
    novo_livro = Livro(titulo=requisicao.titulo, 
                       autor=requisicao.autor,
                       ano_publicacao=requisicao.ano_publicacao)
    
    with Session(get_engine()) as session:
        session.add(novo_livro)
        session.commit()
        session.refresh(novo_livro)

    return novo_livro