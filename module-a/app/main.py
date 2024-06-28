from fastapi import FastAPI
from my_router import pippo

app = FastAPI()
# app.include_router(router.get_router())  # Include the router in your FastAPI app


@app.get("/")
def read_root():
    return  {'msg': 'Hello World'}

