from fastapi import APIRouter
import requests

router = APIRouter()
import logging

logger = logging.getLogger(__name__)


@router.get("/pet_store/{pet_id}")
def get_pet_by_id(pet_id: int, q: str | None = None):
    logger.info("looking for pet")
    response = requests.get(f"https://petstore3.swagger.io/api/v3/pet/{pet_id}")
    return response.json()
