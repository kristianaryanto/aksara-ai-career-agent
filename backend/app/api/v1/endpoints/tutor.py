from fastapi import APIRouter
from pydantic import BaseModel
from app.services import gemini_service

router = APIRouter()

class TutorQuery(BaseModel):
    question: str
    context: str # e.g., text from a specific course material

@router.post("/chat")
async def chat_with_tutor(query: TutorQuery):
    response = gemini_service.get_tutor_response(query.question, query.context)
    return {"answer": response}