from fastapi import APIRouter, HTTPException
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
@router.get("/getproducts", response_model=List[Product])
def get_products():
    products = list(product_collection.find())
    #Iterating through each MongoDB document in the products list
    for product in products:
        product["_id"] = str(product["_id"])  # Convert ObjectId to string as fastapi can't encode ObjectId
        # ObjectId is not a valid JSON type — it's a MongoDB/BSON-specific type.
    return products

# Create product endpoint
@router.post("/products")
def create_product(product: Product):

     # Check if a product with the same name already exists or not so that we can only store unique products
    existing_product = product_collection.find_one({ "name": product.name })
    
    #if exist then throw a exception
    if existing_product:
        raise HTTPException(status_code=400, detail="Product with this name already exists.")

    product_detail = product.dict()
    result = product_collection.insert_one(product_detail)

    if result.inserted_id:
        return { "message": "Product added", "id": str(result.inserted_id) }
    else:
        raise HTTPException(status_code=500, detail="Product could not be added")

