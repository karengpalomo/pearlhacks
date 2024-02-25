from fastapi.exceptions import HTTPException
from fastapi import APIRouter, Header, HTTPException, Request, Response, Depends
from ..models import User, SearchParams, EditProfileRequest, Place
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
    
@api.post("/users/{user_id}/add_friend/{friend_id}")
def add_friend(user_id: int, friend_id: int, user_svc = UserService()):
    user = user_svc.add_friend(user_id, friend_id)
    if not user:
        raise HTTPException(status_code=404, detail="User or friend not found")
    return {"message": "Friend added successfully"}

@api.post("/users/{user_id}/remove_friend/{friend_id}")
def remove_friend(user_id: int, friend_id: int, user_svc = UserService()):
    user = user_svc.remove_friend(user_id, friend_id)
    if not user:
        raise HTTPException(status_code=404, detail="User or friend not found")
    return {"message": "Friend removed successfully"}

@api.put("/users/{user_id}/edit-profile")
def edit_profile(user_id: int, edit_request: EditProfileRequest, user_svc = UserService()):
    user = user_svc.edit_profile(user_id, edit_request.bio, edit_request.location, edit_request.tags_to_add, edit_request.tags_to_remove)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user.to_model()

@api.get("/users/{user_id}/friends", response_model=List[User])
def view_friends(user_id: int, user_svc = UserService()):
    friends = user_svc.get_friends(user_id)
    if friends is None:
        raise HTTPException(status_code=404, detail="User not found")
    return friends

@api.get("/users/by-username/{username}", response_model=User)
def get_user(username: str, user_svc = UserService()):
    user = user_svc.get_user_by_username(username)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@api.post("/users/favorite-place")
def add_favorite_place(user_id: int, place: Place, user_svc = UserService()):
    try:
        updated_user = user_svc.add_favorite(user_id=user_id, place=place)
        return {"message": "Place added to favorites successfully", "user": updated_user.id}
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

