from fastapi.exceptions import HTTPException
from fastapi import APIRouter, Header, HTTPException, Request, Response, Depends
from ..models import User
from ..services import UserService

api = APIRouter()

@api.get("/search/")
def filter(
    body: list[list],
    user_svc: UserService = Depends()
):
    try:
        return user_svc.filter(availability=body[0], tags=body[1], distance=body[2], price=body[3])
    except Exception as e:
        print("❌" + str(e))
        raise HTTPException(status_code=404, detail=str(e))
        
    