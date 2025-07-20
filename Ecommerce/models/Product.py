from pydantic import BaseModel, Field
from typing import List, Optional
from bson import ObjectId

class Size(BaseModel):
    size: str
    quantity: int

class Product(BaseModel):
    name: str
    price: int
    sizes: List[Size]

#extending Product Pydantic model to include the MongoDB _id field 
class ProductInDB(Product):
    id: Optional[str] = Field(default=None, alias="_id")
