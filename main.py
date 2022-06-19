from enum import Enum

from main import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get('/')
async def root():
    return {"message": "Hello, world!"}
