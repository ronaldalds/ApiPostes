
from core.configs import settings
from sqlalchemy import (Boolean, Column, Date, Float, ForeignKey, Integer,
                        String)

# from sqlalchemy.orm import relationship


class PosteModel(settings.DBBaseModel):
    __tablename__ = 'postes'

    id = Column(Integer, primary_key=True, autoincrement=True)
    proprietario = Column(String(256), nullable=True)
    tipo = Column(String(256), nullable=True)
    altura = Column(Integer, nullable=True)
    tracao = Column(Integer, nullable=True)
    rede = Column(String(256), nullable=True)
    casa = Column(Integer, nullable=True)
    comercio = Column(Integer, nullable=True)
    predio = Column(String(256), nullable=True)
    equipamento = Column(String(256), nullable=True)
    codigo_csi = Column(String(256), nullable=True)
    ocupacao = Column(String(256), nullable=True)
    imagem = Column(String(256), nullable=True)
    data_creacao = Column(Date, nullable=False)
    data_atualizacao = Column(Date, nullable=True)
    aprovado = Column(Boolean, default=False)
    data_aprovacao = Column(Date, nullable=True)
    protocolo_aprovacao = Column(String(256), nullable=True)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    descricao = Column(String(256), nullable=True)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'))
    # criador = relationship(
    #     "UsuarioModel", back_populates='postes', lazy='joined')
