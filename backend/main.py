from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from ws_gpt import router as ws_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Svelte frontend dev
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(ws_router)
