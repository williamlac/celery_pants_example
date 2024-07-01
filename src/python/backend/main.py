"""Main file for the backend application."""

from backend.celery_tasks import add
import uvicorn
from fastapi import FastAPI

if __name__ == "__main__":
    app = FastAPI()


    @app.get("/")
    async def root():
        return {"message": "Hello World"}
    
    @app.get("/celery")
    async def test_celery():
        add.apply_async((2,2))
        return {"message": "Triggered"}
    
    uvicorn.run(app, host="0.0.0.0", port=8000) 
