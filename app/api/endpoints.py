from fastapi import APIRouter
from pydantic import BaseModel
from app.services.chat_service import chat_process

router = APIRouter()

class ChatRequest(BaseModel):
    message: str

@router.post("/chat")
async def chat_endpoint(req: ChatRequest):
    return chat_process(req.message)
