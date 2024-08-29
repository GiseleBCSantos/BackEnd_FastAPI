from sqlmodel import SQLModel, create_engine

def get_engine():
    return create_engine('sqlite:///livros.db')


def sync_database(engine):
    SQLModel.metadata.create_all(engine)