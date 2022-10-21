from fastapi import FastAPI

from api.v1.api import api_router
from core.configs import settings

app = FastAPI(title='API Postes', version="0.1.0")
app.include_router(api_router, prefix=settings.API_V1_STR)


if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000,
                log_level='info', reload=True)
