from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Using this we can control requests from different origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def index():
    return {"Message": "Welcome to the API"}

@app.get("/api/params")
def search(request: Request):
    parameters = list()

    for parameter_name in request.query_params.keys():
        parameters.append(parameter_name)

    print(parameters)
    
    return {"Parameters": parameters}