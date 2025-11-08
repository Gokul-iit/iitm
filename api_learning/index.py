from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
def index():
    return {"Message": "Welcome to the API"}
