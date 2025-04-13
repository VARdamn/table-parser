from fastapi import FastAPI

app = FastAPI()

@app.get("/ping")
def read_root():
    return "pong"

@app.get("/teachers/load")
def read_root():
    return "pong"

commands = {
    'load_users'
}