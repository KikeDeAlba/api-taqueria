from itertools import product
from fastapi import FastAPI
from app.routers import admin
from app.routers import orders
from app.routers import products
api = FastAPI()
api.include_router(admin.router)
api.include_router(orders.router)
api.include_router(products.router)
if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run(api, host='0.0.0.0', port=3001)
    