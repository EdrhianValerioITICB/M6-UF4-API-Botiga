from typing import Union
from fastapi import FastAPI
import botiga_db
from pydantic import BaseModel

app = FastAPI()

class category():
    name: str
    create_at: str
    update_at: str

class subcategory():
    name: str
    category_id: str
    create_at: str
    update_at: str
    category_id: int

class product(BaseModel):
    name: str
    description: str
    company: str
    price: float
    units: int
    subcategory_id: int

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

