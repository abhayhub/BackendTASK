from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel
from typing import List, Optional
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
@router.get("/getproducts")
def get_products(
    name: Optional[str] = Query(None),
    size: Optional[str] = Query(None),
    limit: int = Query(10),
    offset: int = Query(0)):
    query = {}
    
    # If name is provided then search products with name
    if name:
        query["name"] = {"$regex": name, "$options": "i"}

    # If size is provided then match products having that size in sizes array.
    if size:
        query["sizes.size"] = size

    # Perform query with pagination
    products = list(
        product_collection
        .find(query)
        .sort("_id")
        .skip(offset)
        .limit(limit)
    )


    # Convert ObjectId to string
    for product in products:
        product["_id"] = str(product["_id"])

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

