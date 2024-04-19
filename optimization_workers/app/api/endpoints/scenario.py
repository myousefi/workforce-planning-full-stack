from typing import Optional

from fastapi import Query, HTTPException, APIRouter
from pymongo.errors import DuplicateKeyError

from app.api.models.scenario import Scenario, ScenarioInput
from app.services.database.mongodb import db


router = APIRouter()


@router.post("/rmo/api/v1/library/{sid}")
def import_scenario(sid: str):
    try:
        scenario = db.scenarios.find_one({"_id": sid})
        if scenario:
            db.library.insert_one(scenario)
            return {"message": "Scenario imported"}
        else:
            raise HTTPException(status_code=404, detail="Scenario not found")
    except DuplicateKeyError:
        raise HTTPException(
            status_code=400, detail="Scenario already exists in the library"
        )


@router.get("/rmo/api/v1/library")
def list_library_scenarios():
    scenarios = list(db.library.find())
    return [Scenario(**scenario) for scenario in scenarios]


@router.delete("/rmo/api/v1/library/{sid}")
def delete_library_scenario(sid: str):
    result = db.library.delete_one({"_id": sid})
    if result.deleted_count == 1:
        return {"message": "Scenario deleted"}
    else:
        raise HTTPException(status_code=404, detail="Scenario not found")


@router.get("/rmo/api/v1/scenarios")
def list_scenarios():
    scenarios = list(db.scenarios.find())
    return [Scenario(**scenario) for scenario in scenarios]


@router.post("/rmo/api/v1/scenarios")
def create_scenario(scenario: ScenarioInput, source: Optional[str] = Query("")):
    scenario_dict = scenario.dict()
    scenario_dict["source"] = source
    try:
        result = db.scenarios.insert_one(scenario_dict)
        scenario_dict["_id"] = str(result.inserted_id)
        return {"message": "Scenario created", "scenario": Scenario(**scenario_dict)}
    except DuplicateKeyError:
        raise HTTPException(status_code=400, detail="Scenario already exists")


@router.delete("/rmo/api/v1/scenarios")
def delete_all_scenarios():
    db.scenarios.delete_many({})
    return {"message": "All scenarios deleted"}


@router.get("/rmo/api/v1/scenarios/{sid}")
def get_scenario(sid: str):
    scenario = db.scenarios.find_one({"_id": sid})
    if scenario:
        return Scenario(**scenario)
    else:
        raise HTTPException(status_code=404, detail="Scenario not found")


@router.put("/rmo/api/v1/scenarios/{sid}")
def update_scenario(sid: str, scenario: Scenario):
    scenario_dict = scenario.dict(exclude_unset=True)
    result = db.scenarios.update_one({"_id": sid}, {"$set": scenario_dict})
    if result.modified_count == 1:
        return {"message": "Scenario updated"}
    else:
        raise HTTPException(status_code=404, detail="Scenario not found")


@router.delete("/rmo/api/v1/scenarios/{sid}")
def delete_scenario(sid: str):
    result = db.scenarios.delete_one({"_id": sid})
    if result.deleted_count == 1:
        return {"message": "Scenario deleted"}
    else:
        raise HTTPException(status_code=404, detail="Scenario not found")
