from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from kogpt import kogpt_router
from chatgpt import chatgpt_router

app = FastAPI()

origins = [
    # "http://localhost:8001"
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(kogpt_router.router)
app.include_router(chatgpt_router.router)
