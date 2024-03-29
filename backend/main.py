"""Entrypoint of backend API exposing backend to application server"""

from fastapi import FastAPI
from .api import authentication, user, groups

app = FastAPI(
    title="DreamScape API",
    version="0.0.1"
)

#FILL IN WITH OTHER APIs
app.include_router(authentication.api)
app.include_router(user.api)
app.include_router(groups.api)

#uvicorn backend.main:app --host 0.0.0.0 --port 80
