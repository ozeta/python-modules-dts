from fastapi import FastAPI
from module_a.app.routers.my_router import pippo
from module_a.app.routers import pet_store
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
app = FastAPI()
# app.include_router(router.get_router())  # Include the router in your FastAPI app

app.include_router(pet_store.router)

@app.get("/")
def read_root():
    logger.info(pippo)
    return  {'msg': 'Hello World'}

