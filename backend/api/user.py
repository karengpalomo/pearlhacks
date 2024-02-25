from fastapi.exceptions import HTTPException
from fastapi import APIRouter, Header, HTTPException, Request, Response, Depends
from ..models import User, SearchParams
from ..services import UserService
from typing import Optional, List

api = APIRouter()

# must be list of strings, 
@api.get("/search/")
def filter(
    params: SearchParams,
    user_svc: UserService = Depends()
):
    try:
        # Filter based on the provided parameters, excluding any that are None
        return user_svc.filter(tags=params.tags, distance=params.distance,
                               prices=params.price, availability=params.availability)
    except Exception as e:
        print("❌" + str(e))
        raise HTTPException(status_code=404, detail=str(e))
    