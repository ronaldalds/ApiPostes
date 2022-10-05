from core.database import Session
from core.security import gerar_hash_senha
from models.usuario_model import UsuarioModel


async def create_admin() -> UsuarioModel:
    print("criando admin")
    nome: str = "admin"
    sobrenome: str = "admin"
    email: str = "admin@gmail.com"
    eh_admin: bool = True
    senha: str = gerar_hash_senha("123")
    novo_usuario: UsuarioModel = UsuarioModel(
        nome=nome,
        sobrenome=sobrenome,
        email=email,
        eh_admin=eh_admin,
        senha=senha
    )

    async with Session() as conn:

        conn.add(novo_usuario)
        await conn.commit()
        print("admin criado")
        return novo_usuario


if __name__ == '__main__':
    import asyncio

    asyncio.run(create_admin())
