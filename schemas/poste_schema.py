from datetime import date, datetime
from typing import Optional

from pydantic import BaseModel, HttpUrl, validator


class PosteSchemaBase(BaseModel):
    id: Optional[int] = None
    proprietario: str
    tipo: str
    altura: int
    tracao: int
    rede: str
    latitude: float
    longitude: float
    aprovado: bool = False

    class Config:
        orm_mode = True


class PosteSchemaRead(PosteSchemaBase):
    usuario_id: int
    proprietario: Optional[str]
    tipo: Optional[str]
    altura: Optional[int]
    tracao: Optional[int]
    rede: Optional[str]
    latitude: Optional[float]
    longitude: Optional[float]
    aprovado: Optional[bool]
    casa: Optional[int]
    comercio: Optional[int]
    predio: Optional[str]
    equipamento: Optional[str]
    codigo_csi: Optional[str]
    ocupacao: Optional[str]
    imagem: Optional[HttpUrl]
    protocolo_aprovacao: Optional[str]
    descricao: Optional[str]
    data_creacao: Optional[date]
    data_atualizacao: Optional[date]
    data_aprovacao: Optional[date]


class PosteSchemaCreate(PosteSchemaBase):
    casa: Optional[int]
    comercio: Optional[int]
    predio: Optional[str]
    equipamento: Optional[str]
    codigo_csi: Optional[str]
    ocupacao: Optional[str]
    imagem: Optional[HttpUrl]
    data_creacao: Optional[date]
    data_aprovacao: Optional[date]
    protocolo_aprovacao: Optional[str] = None
    descricao: Optional[str]

    @validator("data_creacao", pre=True)
    def parse_createdate(cls, value):
        return datetime.strptime(
            value,
            "%d/%m/%Y"
        ).date()

    @validator("data_aprovacao", pre=True)
    def parse_approveddate(cls, value):
        return datetime.strptime(
            value,
            "%d/%m/%Y"
        ).date()


class PosteSchemaUp(PosteSchemaBase):
    proprietario: Optional[str]
    tipo: Optional[str]
    altura: Optional[int]
    tracao: Optional[int]
    rede: Optional[str]
    latitude: Optional[float]
    longitude: Optional[float]
    aprovado: Optional[bool]
    casa: Optional[int]
    comercio: Optional[int]
    predio: Optional[str]
    equipamento: Optional[str]
    codigo_csi: Optional[str]
    ocupacao: Optional[str]
    imagem: Optional[HttpUrl]
    data_atualizacao: Optional[date]
    data_aprovacao: Optional[date]
    protocolo_aprovacao: Optional[str]
    descricao: Optional[str]

    @validator("data_atualizacao", pre=True)
    def parse_updatedate(cls, value):
        return datetime.strptime(
            value,
            "%d/%m/%Y"
        ).date()

    @validator("data_aprovacao", pre=True)
    def parse_approveddate(cls, value):
        return datetime.strptime(
            value,
            "%d/%m/%Y"
        ).date()
