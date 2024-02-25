from fastapi.exceptions import HTTPException
from fastapi import APIRouter, Header, HTTPException, Request, Response, Depends
from ..models import User, SearchParams, EditProfileRequest, Place
from ..services import UserService, GroupService
from typing import Optional, List

api = APIRouter()

@api.post("/groups/{user_id}/create_group/")
def create_group(user_id: int, group_name: str, group_svc = GroupService()):
    group = group_svc.create_group(group_name=group_name)
    if not group:
        raise HTTPException(status_code=404, detail="Error")
    return {"message": "Friend added successfully"}

@api.post("/groups/{group_id}/add_member/{username}")
def add_member(group_id: int, username: str, group_svc = GroupService()):
    try:
        group_svc.add_member(group_id=group_id, username=username)
        return 'OK'
    except Exception as e:
        raise HTTPException(status_code=404, detail=e)

@api.get("/groups/{group_id}/view_members/")
def view_members(group_id: int, group_svc = GroupService()):
    try:
        group_svc.view_members(group_id=group_id)
        return "OK"
    except Exception as e:
        raise HTTPException(status_code=404, detail=e)
    
@api.get("/groups/view_groups/{user_id}/")
def view_user_groups(user_id: int, group_svc = GroupService()):
    try:
        group_svc.view_user_groups(user_id=user_id)
        return "OK"
    except Exception as e:
        raise HTTPException(status_code=404, detail=e)