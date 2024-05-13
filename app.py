from typing import Union
from fastapi import FastAPI
import pelis_db

from pydantic import BaseModel

app = FastAPI()

@app.get("/product")
def read_products():
    pass

@app.get("/product/{id}")
def read_one_product(id: int):
    pass

@app.put("/product/{id}")
def update_product(id: int):
    pass

@app.delete("/product/{id}")
def delte_product(id: int):
    pass

@app.get("/productAll/")
def getAll_products():
    pass
@app.post("/product")
def create_one_product():
    pass

