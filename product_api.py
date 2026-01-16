from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
app=FastAPI()
class Product(BaseModel):
    id:int
    name:str
    description:str
    price:float
products = [
   Product(id=1,name="Phone", description="A Tablet Phones",price=688.9),
   Product(id=2,name="Laptop", description="Asus laptop",price=888.9),
   Product(id=3,name="vehicles", description="A motor bike",price=1988.9),
   Product(id=4,name="shooes", description="A puma shoes",price=288.9)
]
@app.get("/")
def root():
    return {"message": "FastAPI is running successfully 🚀"}
@app.get("/products")
def get_all_products():
    return products
@app.get("/products/{id}")
def product_get_all(id:int):
    for product in products:
        if product.id==id:
            return product
    return {"error":"products not found"}
@app.post("/products")
def post_products(Product:Product):
    products.append(Product)
    return Product




