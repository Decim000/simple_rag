from fastapi import FastAPI
from routers import document_loader_router, rag_router

app = FastAPI()

app.include_router(document_loader_router)
app.include_router(rag_router)
