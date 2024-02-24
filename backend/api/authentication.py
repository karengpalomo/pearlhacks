from fastapi.exceptions import HTTPException
from fastapi import APIRouter, Header, HTTPException, Request, Response, Depends
from ..models import User
from ..services import UserService

api = APIRouter()

@api.post("/signup/")
def create_user(username: str, email: str, password: str, first_name: str, last_name: str, user_svc: UserService = Depends()) -> str:
    try:
        user_svc.create_user(username, email, password, first_name, last_name)
        return "OK"
    except Exception as e:
        print(e)
        raise HTTPException(status_code=404, detail=str(e))

@api.post('/login/')
def login(username: str, password: str, user_svc: UserService = Depends()) -> User:
    try:
        return user_svc.login(username, password)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
        
    