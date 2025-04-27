from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["http://localhost:5173"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

router = APIRouter(prefix='/api')

@app.get("/ping")
def read_root():
    return "pong"

@app.get("/teachers/load")
def read_root():
    return "pong"

@router.post("/users")
def read_root(data):
    print(data)
    return "pong"

app.include_router(router)

commands = {
    'load_users'
}