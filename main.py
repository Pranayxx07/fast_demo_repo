from db import BASE,engine
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from user.views import user_rout

BASE.metadata.create_all(engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_rout)