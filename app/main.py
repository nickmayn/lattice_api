from fastapi import FastAPI
from .config import settings
from .router import api_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title=settings.APP_NAME,
              version=settings.VERSION,
              root_path=settings.ROOT_PATH
              )

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)


app.include_router(api_router, prefix=settings.ROOT_PATH)