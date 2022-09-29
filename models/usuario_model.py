from core.configs import settings
from sqlalchemy import (Boolean, Column, DateTime, Float, ForeignKey, Integer,
                        String)
from sqlalchemy.orm import relationship


class UsuarioModel(settings.DBBaseModel):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(256), nullable=True)
    sobrenome = Column(String(256), nullable=True)
    email = Column(String(256), index=True, nullable=False, unique=True)
    senha = Column(String(256), nullable=False)
    eh_admin = Column(Boolean, default=False)
    postes = relationship(
        "PosteModel",
        cascade="all,delete-orphan",
        back_populates="criador",
        uselist=True,
        lazy="joined"
    )
