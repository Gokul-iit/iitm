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
    parameter_values = list()
    for parameter_name in request.query_params.keys(): # Iterate through all query parameters but gives only unique keys

        parameter_values.append(request.query_params.getlist(parameter_name))  # Get all values of each parameter

        for value in parameter_values:
            parameters.append(
                {
                    "Parameter": parameter_name,
                    "Value": value,
                }
            )

    print(parameters)

    return {"Parameters": parameters}

from pydantic import BaseModel  # to define data models like classes and objects
from datetime import datetime

class Job(BaseModel):
    name: str
    cost: int
    

jobs = list()

@app.post("/api/create")
def create(job : Job):                         # we can send objects as input
    jobs.append(job)

    return {"Message": "Item created successfully", "Item": job}

@app.get("/api/jobs")
def get_jobs():
    return {"Jobs": jobs}