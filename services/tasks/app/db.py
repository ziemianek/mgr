from sqlmodel import create_engine, SQLModel, Session, select
from typing import Final


DATABASE_URL: Final[str] = "sqlite:///./test.db"  # TODO: change to the actual database URL
ENGINE = create_engine(DATABASE_URL, echo=True)  # TODO: add Final[Engine] type


def init_db():
    SQLModel.metadata.create_all(ENGINE)


def get_session():
    with Session(ENGINE) as session:
        yield session
