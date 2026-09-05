from fastapi import APIRouter

from src.api.v1 import barber_routes

api_router = APIRouter(prefix="/api/v1")
api_router.include_router(barber_routes.router)