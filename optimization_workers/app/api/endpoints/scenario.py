from typing import Optional

from fastapi import Query

from app.api.main import app
from app.api.models.scenario import Scenario, ScenarioInput


@app.post("/rmo/api/v1/library/{sid}")
def import_scenario(sid: str):
    # TODO: Implement import scenario logic
    return {"message": "Scenario imported"}


@app.get("/rmo/api/v1/library")
def list_library_scenarios():
    # TODO: Implement list library scenarios logic
    return [Scenario()]


@app.delete("/rmo/api/v1/library/{sid}")
def delete_library_scenario(sid: str):
    # TODO: Implement delete library scenario logic
    return {"message": "Scenario deleted"}


@app.get("/rmo/api/v1/scenarios")
def list_scenarios():
    # TODO: Implement list scenarios logic
    return [Scenario()]


@app.post("/rmo/api/v1/scenarios")
def create_scenario(scenario: ScenarioInput, source: Optional[str] = Query("")):
    # TODO: Implement create scenario logic
    return {"message": "Scenario created"}


@app.delete("/rmo/api/v1/scenarios")
def delete_all_scenarios():
    # TODO: Implement delete all scenarios logic
    return {"message": "All scenarios deleted"}


@app.get("/rmo/api/v1/scenarios/{sid}")
def get_scenario(sid: str):
    # TODO: Implement get scenario logic
    return Scenario()


@app.put("/rmo/api/v1/scenarios/{sid}")
def update_scenario(sid: str, scenario: Scenario):
    # TODO: Implement update scenario logic
    return {"message": "Scenario updated"}


@app.delete("/rmo/api/v1/scenarios/{sid}")
def delete_scenario(sid: str):
    # TODO: Implement delete scenario logic
    return {"message": "Scenario deleted"}
