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