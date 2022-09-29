from typing import Optional

from pydantic import BaseModel, HttpUrl


class PosteSchema(BaseModel):
    id: Optional[int] = None
    proprietario: str
    tipo: str
    altura: int
    tracao: int
    rede: str
    casa: Optional[int]
    comercio: Optional[int]
    predio: Optional[str]
    equipamento: Optional[str]
    codigo_csi: Optional[str]
    ocupacao: Optional[str]
    imagem: Optional[str]
    data_creacao: str
    data_atualizacao: Optional[str]
    aprovado: bool
    data_aprovacao: Optional[str]
    protocolo_aprovacao: Optional[str]
    latitude: float
    longitude: float
    descricao: Optional[str]
    usuario_id: Optional[int]

    class Config:
        orm_mode = True
