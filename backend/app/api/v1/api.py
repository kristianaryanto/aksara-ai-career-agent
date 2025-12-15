from fastapi import APIRouter
from app.api.v1.endpoints import cv, tutor

api_router = APIRouter()
api_router.include_router(cv.router, prefix="/cv", tags=["CV & Learning Path"])
api_router.include_router(tutor.router, prefix="/tutor", tags=["AI Tutor"])