from fastapi import FastAPI

from backend.api.routes import router

app = FastAPI(
    title="LLM Evaluation Platform"
)

app.include_router(router)