from fastapi import APIRouter, HTTPException
from app.services.external_api import ExternalAPI

router = APIRouter(prefix="/services", tags=["Services"])

api = ExternalAPI()


@router.get("/")
def get_services():
    try:
        return api.get("services")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
