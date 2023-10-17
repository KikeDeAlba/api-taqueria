from fastapi import FastAPI
from app.routers import admin

api = FastAPI()
api.include_router(admin.router)

if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run(api, host='0.0.0.0', port=3001)