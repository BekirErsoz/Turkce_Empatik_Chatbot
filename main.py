from fastapi import FastAPI
from app.api.endpoints import router

app = FastAPI(title="Türkçe Empatik Chatbot API")
app.include_router(router)

# For `uvicorn main:app` entrypoint
