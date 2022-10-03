from datetime import datetime
from typing import List

from core.deps import get_current_user, get_session
from fastapi import APIRouter, Depends, HTTPException, Response, status
from models.poste_model import PosteModel
from models.usuario_model import UsuarioModel
from schemas.poste_schema import (PosteSchemaCreate, PosteSchemaRead,
                                  PosteSchemaUp)
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

router = APIRouter()


# POST Poste
@router.post('/', status_code=status.HTTP_201_CREATED, response_model=PosteSchemaRead)
async def post_poste(poste: PosteSchemaCreate, usuario_logado: UsuarioModel = Depends(get_current_user), db: AsyncSession = Depends(get_session)):
    """
    Criação de postes na base de dados
    """
    novo_poste: PosteModel = PosteModel(
        proprietario=poste.proprietario,
        tipo=poste.tipo,
        altura=poste.altura,
        tracao=poste.tracao,
        rede=poste.rede,
        casa=poste.casa,
        comercio=poste.comercio,
        predio=poste.predio,
        equipamento=poste.equipamento,
        codigo_csi=poste.codigo_csi,
        ocupacao=poste.ocupacao,
        imagem=poste.imagem,
        data_creacao=datetime.now(),
        aprovado=poste.aprovado,
        data_aprovacao=poste.data_aprovacao,
        latitude=poste.latitude,
        longitude=poste.longitude,
        descricao=poste.descricao,
        usuario_id=usuario_logado.id
    )

    db.add(novo_poste)
    await db.commit()

    return novo_poste


# GET Postes
@router.get('/', response_model=List[PosteSchemaRead])
async def get_postes(db: AsyncSession = Depends(get_session), usuario_logado: UsuarioModel = Depends(get_current_user)):
    async with db as session:
        query = select(PosteModel)
        result = await session.execute(query)
        postes: List[PosteModel] = result.scalars().unique().all()

        return postes


# GET Poste
@router.get('/{poste_id}', response_model=PosteSchemaRead, status_code=status.HTTP_200_OK)
async def get_poste(poste_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(PosteModel).filter(PosteModel.id == poste_id)
        result = await session.execute(query)
        poste: PosteModel = result.scalars().unique().one_or_none()

        if poste:
            return poste
        else:
            raise HTTPException(detail='Poste não encontrado',
                                status_code=status.HTTP_404_NOT_FOUND)


# PUT Poste
@router.put('/{poste_id}', response_model=PosteSchemaRead, status_code=status.HTTP_202_ACCEPTED)
async def put_poste(poste_id: int, poste: PosteSchemaUp, db: AsyncSession = Depends(get_session), usuario_logado: UsuarioModel = Depends(get_current_user)):
    async with db as session:
        query = select(PosteModel).filter(PosteModel.id == poste_id)
        result = await session.execute(query)
        poste_up: PosteModel = result.scalars().unique().one_or_none()

        if poste_up:
            poste_up.data_atualizacao = datetime.now()
            if poste.proprietario:
                poste_up.proprietario = poste.proprietario

            if poste.tipo:
                poste_up.tipo = poste.tipo

            if poste.altura:
                poste_up.altura = poste.altura

            if poste.tracao:
                poste_up.tracao = poste.tracao

            if poste.rede:
                poste_up.rede = poste.rede

            if poste.casa:
                poste_up.casa = poste.casa

            if poste.comercio:
                poste_up.comercio = poste.comercio

            if poste.predio:
                poste_up.predio = poste.predio

            if poste.equipamento:
                poste_up.equipamento = poste.equipamento

            if poste.codigo_csi:
                poste_up.codigo_csi = poste.codigo_csi

            if poste.ocupacao:
                poste_up.ocupacao = poste.ocupacao

            if poste.imagem:
                poste_up.imagem = poste.imagem

            if poste.aprovado:
                poste_up.aprovado = poste.aprovado

            if poste.data_aprovacao:
                poste_up.data_aprovacao = poste.data_aprovacao

            if poste.latitude:
                poste_up.latitude = poste.latitude

            if poste.longitude:
                poste_up.longitude = poste.longitude

            if poste.descricao:
                poste_up.descricao = poste.descricao

            if usuario_logado.id != poste_up.usuario_id:
                poste_up.usuario_id = usuario_logado.id

            await session.commit()

            return poste_up

        else:
            raise HTTPException(detail='Poste não encontrado',
                                status_code=status.HTTP_404_NOT_FOUND)


# DELETE Poste
@router.delete('/{poste_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_poste(poste_id: int, db: AsyncSession = Depends(get_session), usuario_logado: UsuarioModel = Depends(get_current_user)):
    async with db as session:
        query = select(PosteModel).filter(PosteModel.id == poste_id)
        result = await session.execute(query)
        poste_del: PosteModel = result.scalars().unique().one_or_none()

        if poste_del:
            await session.delete(poste_del)
            await session.commit()

            return Response(status_code=status.HTTP_204_NO_CONTENT)

        else:
            raise HTTPException(detail='Poste não encontrado',
                                status_code=status.HTTP_404_NOT_FOUND)
