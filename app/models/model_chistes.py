from typing import Optional

from sqlmodel import Field, SQLModel


class ChisteBase(SQLModel):
    chiste: str = Field(index=True, unique=True)
    pokemon: str


class Chiste(ChisteBase, table=True):
    number: Optional[int] = Field(default=None, primary_key=True)


class ChisteCrear(ChisteBase):
    number: int


class ChisteLeer(ChisteBase):
    number: int


class ChisteActualizar(ChisteBase):
    chiste: Optional[str] = None
    pokemon: Optional[str] = None
