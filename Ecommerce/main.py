import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List



# class Size(BaseModel):
#     size: str
#     quantity: int

# # define base model
# class Product(BaseModel):
#     name : str
#     price : int
#     sizes : List[Size] # In pydantic we can't
#     #declare inline object structures like [{...}] directly. 
#     # Instead, you should define a separate model for the size object.

# class Products(BaseModel):
#     products : List[Product]


app = FastAPI()

app.add_middleware(CORSMiddleware,
                   allow_origins=["*"],
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"],
                )

memory_db = {"products" : []}

# @app.get("/getProduct", response_model=Products)
# def get_Prd():
#     return Products(products=memory_db["products"])

# @app.post("/addProduct", response_model=Products)
# def add_prdct(prdct: Products):
#     # Flatten the list and add each product to the db
#     memory_db["products"].extend(prdct.products)
#     return Products(products=memory_db["products"])

@app.get("/")
def root():
    return {"message": "Ecommerce backend is running"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0",port=8080)
