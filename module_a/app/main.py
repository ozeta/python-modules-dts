from fastapi import FastAPI
from module_a.app.routers import pet_store, swapi
import logging
import uvicorn
import module_common.lib.observability as observability

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
app = FastAPI()
# app.include_router(router.get_router())  # Include the router in your FastAPI app

app.include_router(pet_store.router)
app.include_router(swapi.router)


@app.get("/")
@observability.log_datetime
def read_root():
    return  {'msg': 'Hello World'}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)