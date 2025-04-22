from fastapi import FastAPI, Depends
from dependencies import param


app = FastAPI()


@app.get("/")
async def read_root(key: str = Depends(param)):
    return {"age": "22", "name": "Misha"}[key]