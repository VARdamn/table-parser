from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import all_routers
from app.db.session import engine, Base
import app.db.models

app = FastAPI()

origins = ["http://localhost:5173"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/ping")
def ping():
    return "pong"

for router in all_routers:
    app.include_router(router, prefix="/api")


@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)
    