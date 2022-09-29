from typing import List, Optional

from pydantic import BaseModel, EmailStr

from schemas.poste_schema import PosteSchema


class UsuarioSchemaBase(BaseModel):
    id: Optional[int] = None
    nome: str
    sobrenome: str
    email: EmailStr
    eh_admin: bool = False

    class Config:
        orm_mode = True


class UsuarioSchemaCreate(UsuarioSchemaBase):
    senha: str


class UsuarioSchemaPostes(UsuarioSchemaBase):
    postes: Optional[List[PosteSchema]]


class UsuarioSchemaUp(UsuarioSchemaBase):
    nome: Optional[str]
    sobrenome: Optional[str]
    email: Optional[EmailStr]
    senha: Optional[str]
    eh_admin: Optional[bool]
