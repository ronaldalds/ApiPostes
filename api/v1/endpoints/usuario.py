from typing import Any, List, Optional

from core.auth import autenticar, criar_token_acesso
from core.deps import get_current_user, get_session
from core.security import gerar_hash_senha

from fastapi import APIRouter, Depends, HTTPException, Response, status
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm

from models.usuario_model import UsuarioModel

from schemas.usuario_schema import (UsuarioSchemaBase, UsuarioSchemaCreate,
                                    UsuarioSchemaPostes, UsuarioSchemaUp)

from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

router = APIRouter()


# GET Logado
@router.get('/logado', response_model=UsuarioSchemaPostes)
def get_logado(usuario_logado: UsuarioModel = Depends(get_current_user)):
    return usuario_logado


# POST / Signup
@router.post('/signup', status_code=status.HTTP_201_CREATED, response_model=UsuarioSchemaBase, summary='Criação de usuários')
async def post_usuario(usuario: UsuarioSchemaCreate, db: AsyncSession = Depends(get_session)):
    novo_usuario: UsuarioModel = UsuarioModel(
        nome=usuario.nome,
        sobrenome=usuario.sobrenome,
        email=usuario.email,
        senha=gerar_hash_senha(usuario.senha)
    )

    async with db as session:
        try:
            session.add(novo_usuario)
            await session.commit()

            return novo_usuario
        except IntegrityError:
            raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,
                                detail='Já existe email cadastrado'
                                )


# GET usuarios
@router.get('/', response_model=List[UsuarioSchemaBase], status_code=status.HTTP_200_OK)
async def get_usuarios(db: AsyncSession = Depends(get_session), usuario_logado: UsuarioModel = Depends(get_current_user)):
    async with db as session:
        query = select(UsuarioModel)
        result = await session.execute(query)
        usuarios: List[UsuarioSchemaBase] = result.scalars().unique().all()

        return usuarios


# GET usuario
@router.get('/{usuario_id}', response_model=UsuarioSchemaPostes, status_code=status.HTTP_200_OK)
async def get_usuario(usuario_id: int, db: AsyncSession = Depends(get_session), usuario_logado: UsuarioModel = Depends(get_current_user)):
    async with db as session:
        query = select(UsuarioModel).filter(usuario_id == UsuarioModel.id)
        result = await session.execute(query)
        usuario: UsuarioSchemaPostes = result.scalars().unique().one_or_none()

        if usuario:
            return usuario
        else:
            raise HTTPException(detail='Usuário não encontrado.',
                                status_code=status.HTTP_404_NOT_FOUND)


# PUT usuario
@router.put('/{usuario_id}', response_model=UsuarioSchemaPostes, status_code=status.HTTP_202_ACCEPTED)
async def put_usuario(usuario_id: int, usuario: UsuarioSchemaUp, db: AsyncSession = Depends(get_session), usuario_logado: UsuarioModel = Depends(get_current_user)):
    async with db as session:
        query = select(UsuarioModel).filter(usuario_id == UsuarioModel.id)
        result = await session.execute(query)
        usuario_up: UsuarioSchemaPostes = result.scalars().unique().one_or_none()

        if usuario_up:
            if usuario.nome:
                usuario_up.nome = usuario.nome

            if usuario.sobrenome:
                usuario_up.sobrenome = usuario.sobrenome

            if usuario.email:
                usuario_up.email = usuario.email

            if usuario.senha:
                usuario_up.senha = gerar_hash_senha(usuario.senha)

            if usuario.eh_admin:
                usuario_up.eh_admin = usuario.eh_admin

            await session.commit()

            return usuario_up

        else:
            raise HTTPException(detail='Usuário não encontrado.',
                                status_code=status.HTTP_404_NOT_FOUND)


# DELETE usurio
@router.delete('/{usuario_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_usuario(usuario_id: int, db: AsyncSession = Depends(get_session), usuario_logado: UsuarioModel = Depends(get_current_user)):
    async with db as session:
        query = select(UsuarioModel).filter(usuario_id == UsuarioModel.id)
        result = await session.execute(query)
        usuario_del: UsuarioSchemaPostes = result.scalars().unique().one_or_none()

        if usuario_del:
            await session.delete(usuario_del)
            await session.commit()

            return Response(status_code=status.HTTP_204_NO_CONTENT)

        else:
            raise HTTPException(detail='Usuário não encontrado.',
                                status_code=status.HTTP_404_NOT_FOUND)


# POST login
@router.post('/login')
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: AsyncSession = Depends(get_session)):
    usuario = await autenticar(email=form_data.username, senha=form_data.password, db=db)

    if not usuario:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail='Email ou senha incorretos.')

    return JSONResponse(
        content={"access_token": criar_token_acesso(
            sub=usuario.id), "token_type": "bearer"},
        status_code=status.HTTP_200_OK
    )
