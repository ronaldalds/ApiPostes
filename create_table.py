

from core.configs import settings
from core.database import engine
from core.deps import get_session
from core.security import gerar_hash_senha


async def create_tables() -> None:
    import models.__all_models
    print('Criando as tabelas no banco de dados')

    async with engine.begin() as conn:
        await conn.run_sync(settings.DBBaseModel.metadata.drop_all)
        await conn.run_sync(settings.DBBaseModel.metadata.create_all)
        print('Tabelas criadas com sucesso...')


async def admin() -> None:
    from models.usuario_model import UsuarioModel
    print("criando admin")
    novo_usuario: UsuarioModel = UsuarioModel(
        nome="admin",
        sobrenome="admin",
        email="admin@gmail.com",
        senha=gerar_hash_senha("123")
    )

    async with engine.begin() as session:

        session.add(novo_usuario)
        await session.commit()

    # async with Session as conn:
    # await conn.execute(f'INSERT INTO usuarios (nome, sobrenome, email, senha, eh_admin) VALUES ("admin", "admin", "admin@gmail.com", "{gerar_hash_senha("123")}", "{True}")')
    print("admin criado")
if __name__ == '__main__':
    import asyncio

    asyncio.run(create_tables())
    asyncio.run(admin())
