import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from Routes.Product_routes import router as product_router



app = FastAPI()

app.add_middleware(CORSMiddleware,
                   allow_origins=["*"],
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"],
                )


@app.get("/")
def root():
    return {"message": "Ecommerce backend is running"}

# Include product routes
app.include_router(product_router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0",port=3000)
