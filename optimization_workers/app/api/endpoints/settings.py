from fastapi import APIRouter

from app.api.models.settings import OptimSettings

router = APIRouter()


@router.get("/rmo/api/v1/scenarios/{sid}/settings")
def get_settings(sid: str):
    # TODO: Implement get settings logic
    return OptimSettings()


@router.put("/rmo/api/v1/scenarios/{sid}/settings")
def update_settings(sid: str, settings: OptimSettings):
    # TODO: Implement update settings logic
    return {"message": "Settings updated"}


@router.post("/rmo/api/v1/env/settings")
def set_global_settings(settings: dict):
    # TODO: Implement set global settings logic
    return {"message": "Global settings updated"}


@router.get("/rmo/api/v1/env/settings")
def get_global_settings():
    # TODO: Implement get global settings logic
    return {"settings": {}}
