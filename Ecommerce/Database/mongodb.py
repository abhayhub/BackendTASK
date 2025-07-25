from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os

load_dotenv()
uri = os.getenv("uri")

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

db = client["Ecommerce"] # create a Db

product_collection = db["products"]

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
    # sample = {
    #     "name": "Nike SB Force 58",
    #     "price": 72000,
    #     "sizes": [{"size": "UK 8", "quantity": 3}]
    # }
    # result = product_collection.insert_one(sample) ## adding sample to the db
    # print("Inserted product with ID:", result.inserted_id)
except Exception as e:
    print(e)