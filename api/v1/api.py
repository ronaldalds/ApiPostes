from fastapi import APIRouter

from api.v1.endpoints import poste, usuario

api_router = APIRouter()

api_router.include_router(poste.router, prefix='/postes', tags=['postes'])
api_router.include_router(
    usuario.router, prefix='/usuarios', tags=['usuarios'])
