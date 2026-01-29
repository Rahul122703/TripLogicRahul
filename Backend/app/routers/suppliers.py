from fastapi import APIRouter, HTTPException
from app.services.external_api import ExternalAPI

router = APIRouter(prefix="/suppliers", tags=["Suppliers"])

api = ExternalAPI()


@router.get("/")
def get_suppliers():
    try:
        return api.get("suppliers")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/create")
def create_supplier(payload: dict):
    try:
        return api.post("suppliers/create", payload)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
