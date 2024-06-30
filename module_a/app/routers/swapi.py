from fastapi import APIRouter
import requests
router = APIRouter()
import logging
import module_common.lib.observability as observability
from datetime import datetime


logger = logging.getLogger(__name__)


@router.get("/swapi/starship/{starship_id}")
@observability.log_datetime
def get_starship_by_id(starship_id: int, q: str | None = None):
    logger.info("looking for starship")
    response = requests.get(f"https://swapi.dev/api/starships/{starship_id}")
    return response.json()
