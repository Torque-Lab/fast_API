from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Operation(BaseModel):
    a: float
    b: float

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI Calculator!"}

@app.post("/add")
def add_numbers(op: Operation):
    return {"result": op.a + op.b}

@app.post("/subtract")
def subtract_numbers(op: Operation):
    return {"result": op.a - op.b}

@app.post("/multiply")
def multiply_numbers(op: Operation):
    return {"result": op.a * op.b}

@app.post("/divide")
def divide_numbers(op: Operation):
    if op.b == 0:
        raise HTTPException(status_code=400, detail="Cannot divide by zero")
    return {"result": op.a / op.b}
