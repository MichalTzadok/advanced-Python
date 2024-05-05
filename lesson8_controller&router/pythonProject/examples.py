from fastapi import FastAPI, Depends, APIRouter
from fastapi.middleware.cors import CORSMiddleware

example_router = APIRouter()


def other_func(name: str):
    return name == "sara"


@example_router.get("/all")
async def get_user(is_authenticated: bool = Depends(other_func)):
    if is_authenticated:
        return "great"
