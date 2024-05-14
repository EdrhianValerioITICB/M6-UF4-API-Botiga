from typing import Union
from fastapi import FastAPI, File, UploadFile
import botiga_db
from pydantic import BaseModel
import producte

"""
API-REST de Productos, Subcategorias, Categorias
Ejecucion: uvicorn main:app --reload
"""
app = FastAPI()
# BaseModels
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
    subcategory_id: int

# Endpoints
# GET (leer todos, leer uno, leer con mas detalles)
@app.get("/products")
def read_products():
    return producte.productes_schema(botiga_db.read())

@app.get("/product/{id}")
def read_one_product(id: int):
    return producte.producte_schema(botiga_db.read_one(id))

@app.get("/productAll/")
def getAll_products():
    return producte.readAll_schema(botiga_db.readAll())

# POST (crear uno, carga masiva)
@app.post("/product")
def create_one_product(data: product):
    name = data.name
    description = data.description
    company = data.company
    price = data.price
    units = data.units
    subcategory_id = data.subcategory_id
    return botiga_db.afegir_producte(name, description, company, price, units, subcategory_id)

@app.post("/loadProducts")
async def carrega_massiva(file: UploadFile = File(...)):
    return botiga_db.carregar_csv(file)

# PUT Y DELETE (modificar y eliminar)
@app.put("/product/{id}")
def update_product(id: int, price: float, units: int ):
    return botiga_db.update_producte(id, price, units)

@app.delete("/product/{id}")
def delete_product(id: int):
    return botiga_db.delete_product(id)

