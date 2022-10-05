from click import echo
from sqlalchemy.ext.asyncio import (AsyncEngine, AsyncSession,
                                    create_async_engine)
from sqlalchemy.orm import sessionmaker

from core.configs import settings

engine: AsyncEngine = create_async_engine(settings.DB_URL)

Session: AsyncSession = sessionmaker(engine,
                                     autocommit=False,
                                     autoflush=False,
                                     expire_on_commit=False,
                                     class_=AsyncSession,
                                     )
