from typing import Union
from fastapi import FastAPI, File, UploadFile
import botiga_db
from pydantic import BaseModel

app = FastAPI()

class category(BaseModel):
    name: str
    create_at: str
    update_at: str

class subcategory(BaseModel):
    subcategory_id: int
    category_id: int

class product(BaseModel):
    name: str
    description: str
    company: str
    price: float
    units: int
    subcategory: subcategory

@app.get("/products")
def read_products():
    return botiga_db.read()

@app.get("/product/{id}")
def read_one_product(id: int):
    return botiga_db.read_one(id)

@app.post("/product")
def create_one_product(data: product):
    name = data.name
    description = data.description
    company = data.company
    price = data.price
    units = data.units
    subcategory_id = data.subcategory_id
    return botiga_db.afegir_producte(name, description, company, price, units, subcategory_id)

@app.put("/product/{id}")
def update_product(id: int, price: float, units: int ):
    return botiga_db.update_producte(id, price, units)

@app.delete("/product/{id}")
def delte_product(id: int):
    return botiga_db.delete_product(id)

@app.get("/productAll/")
def getAll_products():
    return botiga_db.readAll()

@app.post("/massivo")
async def carrega_massiva(file: UploadFile):
    return botiga_db.carregar_csv(file)