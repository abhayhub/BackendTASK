from fastapi import APIRouter
from pydantic import BaseModel
from typing import List
from bson import ObjectId
from Database.mongodb import product_collection

router = APIRouter()

# Pydantic Models
class Size(BaseModel):
    size: str
    quantity: int

class Product(BaseModel):
    name: str
    price: int
    sizes: List[Size]

# GET all products
@router.get("/products", response_model=List[Product])
def get_products():
    products = list(product_collection.find())
    for product in products:
        product["_id"] = str(product["_id"])  # Convert ObjectId to string
    return products
