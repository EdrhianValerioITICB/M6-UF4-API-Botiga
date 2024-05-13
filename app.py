from typing import Union
from fastapi import FastAPI
import botiga_db
from pydantic import BaseModel

app = FastAPI()

# class category():
#     name: str
#     create_at: str
#     update_at: str

# class subcategory():
#     name: str
#     category_id: str
#     create_at: str
#     update_at: str
#     category_id: category

# class product(BaseModel):
#     name: str
#     description: str
#     company: str
#     price: float
#     units: int
#     subcategory_id: subcategory

@app.get("/products")
def read_products():
    return botiga_db.read()

@app.get("/product/{id}")
def read_one_product(id: int):
    return botiga_db.read_one(id)

@app.post("/product")
def create_one_product(data):
    return botiga_db.create(data)

@app.put("/product/{id}")
def update_product(id: int, price: float, units: int ):
    return botiga_db.update_producte(id, price, units)

@app.delete("/product/{id}")
def delte_product(id: int):
    return botiga_db.delete_product(id)

@app.get("/productAll/")
def getAll_products():
    return botiga_db.readAll()



