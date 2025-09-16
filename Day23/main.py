from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, validator
from fastapi.responses import JSONResponse

app = FastAPI()

class Product(BaseModel):
    name: str
    price: float
    category: str

    @validator("price")
    def price_must_be_positive(cls, value):
        if value <= 0:
            raise ValueError("Price must be greater than 0")
        return value

products = {}

@app.post("/products/")
async def create_product(product: Product):
    if product.name in products:
        return JSONResponse(
            status_code=400,
            content={"error": f"Product '{product.name}' already exists"}
        )
    products[product.name] = product
    return JSONResponse(
        status_code=201,
        content={"message": "Product created successfully", "product": product.dict()}
    )

@app.get("/products/{name}")
async def get_product(name: str):
    if name not in products:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"product": products[name]}
