from fastapi import FastAPI, Query
from pydantic import BaseModel
from typing import List, Optional

from app.api.Job import Job

app = FastAPI()


# Define Pydantic models for request/response bodies
class Resource(BaseModel):
    resource_ID: str
    profile: str
    private: bool
    disable: bool


class Combination(BaseModel):
    resource_ID: str
    job_ID: str
    preassign: str


class CombinationML(BaseModel):
    resource_ID: str
    job_ID: str
    role: str
    technology: str
    domain: str
    score: float


class Assignment(BaseModel):
    resource_id: str
    job_id: str
    score: float
    matching_threshold: float
    enforced: bool
    priority: str


class Gaps(BaseModel):
    job_id: str
    matching_threshold: float
    priority: str


class Hire(BaseModel):
    job_id: str
    matching_threshold: float
    priority: str


class Idle(BaseModel):
    resource_id: str


class Solution(BaseModel):
    assignments: List[Assignment]
    gaps: List[Gaps]
    idle_workforce: List[Idle]
    hire: List[Hire]
    combinations: List[CombinationML]


class DemandKPI(BaseModel):
    fulfillment: float
    unfilled: float
    fulfillment_available: float
    fulfillment_hiring: float
    weighted: float


class UtilizationKPI(BaseModel):
    available: float
    hiring: float
    utilization: float
    idle_rate: float


class BudgetKPI(BaseModel):
    consumed: float
    remainder: float


class KPI(BaseModel):
    demand: DemandKPI
    utilization: UtilizationKPI
    budget: BudgetKPI


class OptimParams(BaseModel):
    threshold_flag: bool
    hiring_flag: bool
    preallocation_flag: bool
    hiring_limit: float


class OptimSettings(BaseModel):
    params: OptimParams


class ScenarioInput(BaseModel):
    name: str
    description: str


class ScenarioLock(BaseModel):
    owner: str
    timestamp: int


class ScenarioOptim(BaseModel):
    status: str
    submittedAt: int
    startedAt: int
    endedAt: int
    csJobId: str
    solveStatus: str
    errorMsg: str


class Scenario(BaseModel):
    _id: str
    name: str
    index: int
    createdAt: int
    modifiedAt: int
    description: str
    org: str
    lock: ScenarioLock
    optim: ScenarioOptim


class ErrorMessage(BaseModel):
    code: str
    message: str
    scenario: str


class Error(BaseModel):
    error: ErrorMessage


class ValidationMessage(BaseModel):
    param: str
    msg: str
    value: str
    location: str


class ValidationErrorInfo(BaseModel):
    code: str
    message: str
    validation: List[ValidationMessage]


class ValidationError(BaseModel):
    error: ValidationErrorInfo


# Define API endpoints


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


@app.post("/rmo/api/v1/scenarios/{sid}/optim")
def request_optimization(sid: str):
    # TODO: Implement request optimization logic
    return {"message": "Optimization requested"}


@app.delete("/rmo/api/v1/scenarios/{sid}/optim")
def cancel_optimization(sid: str):
    # TODO: Implement cancel optimization logic
    return {"message": "Optimization cancelled"}


@app.get("/rmo/api/v1/scenarios/{sid}/optim/log")
def get_optimization_log(sid: str):
    # TODO: Implement get optimization log logic
    return {"log": "Optimization log"}


@app.get("/rmo/api/v1/scenarios/{sid}/resources")
def list_resources(sid: str):
    # TODO: Implement list resources logic
    return [Resource()]


@app.post("/rmo/api/v1/scenarios/{sid}/resources")
def create_resource(sid: str, resource: Resource):
    # TODO: Implement create resource logic
    return {"message": "Resource created"}


@app.delete("/rmo/api/v1/scenarios/{sid}/resources")
def delete_all_resources(sid: str):
    # TODO: Implement delete all resources logic
    return {"message": "All resources deleted"}


@app.get("/rmo/api/v1/scenarios/{sid}/resources/{id}")
def get_resource(sid: str, id: str):
    # TODO: Implement get resource logic
    return Resource()


@app.put("/rmo/api/v1/scenarios/{sid}/resources/{id}")
def update_resource(sid: str, id: str, resource: Resource):
    # TODO: Implement update resource logic
    return {"message": "Resource updated"}


@app.delete("/rmo/api/v1/scenarios/{sid}/resources/{id}")
def delete_resource(sid: str, id: str):
    # TODO: Implement delete resource logic
    return {"message": "Resource deleted"}


@app.get("/rmo/api/v1/scenarios/{sid}/jobs")
def list_jobs(sid: str):
    # TODO: Implement list jobs logic
    return [Job()]


@app.post("/rmo/api/v1/scenarios/{sid}/jobs")
def create_job(sid: str, job: Job):
    # TODO: Implement create job logic
    return {"message": "Job created"}


@app.delete("/rmo/api/v1/scenarios/{sid}/jobs")
def delete_all_jobs(sid: str):
    # TODO: Implement delete all jobs logic
    return {"message": "All jobs deleted"}


@app.get("/rmo/api/v1/scenarios/{sid}/jobs/{id}")
def get_job(sid: str, id: str):
    # TODO: Implement get job logic
    return Job()


@app.put("/rmo/api/v1/scenarios/{sid}/jobs/{id}")
def update_job(sid: str, id: str, job: Job):
    # TODO: Implement update job logic
    return {"message": "Job updated"}


@app.delete("/rmo/api/v1/scenarios/{sid}/jobs/{id}")
def delete_job(sid: str, id: str):
    # TODO: Implement delete job logic
    return {"message": "Job deleted"}


@app.get("/rmo/api/v1/scenarios/{sid}/combinations")
def list_combinations(sid: str):
    # TODO: Implement list combinations logic
    return [Combination()]


@app.post("/rmo/api/v1/scenarios/{sid}/combinations")
def create_combination(sid: str, combination: Combination):
    # TODO: Implement create combination logic
    return {"message": "Combination created"}


@app.delete("/rmo/api/v1/scenarios/{sid}/combinations")
def delete_all_combinations(sid: str):
    # TODO: Implement delete all combinations logic
    return {"message": "All combinations deleted"}


@app.get("/rmo/api/v1/scenarios/{sid}/combinations/{id}")
def get_combination(sid: str, id: str):
    # TODO: Implement get combination logic
    return Combination()


@app.put("/rmo/api/v1/scenarios/{sid}/combinations/{id}")
def update_combination(sid: str, id: str, combination: Combination):
    # TODO: Implement update combination logic
    return {"message": "Combination updated"}


@app.delete("/rmo/api/v1/scenarios/{sid}/combinations/{id}")
def delete_combination(sid: str, id: str):
    # TODO: Implement delete combination logic
    return {"message": "Combination deleted"}


@app.get("/rmo/api/v1/scenarios/{sid}/solution")
def get_solution(sid: str):
    # TODO: Implement get solution logic
    return Solution()


@app.get("/rmo/api/v1/scenarios/{sid}/kpi")
def get_kpi(sid: str):
    # TODO: Implement get KPI logic
    return KPI()


@app.get("/rmo/api/v1/scenarios/{sid}/settings")
def get_settings(sid: str):
    # TODO: Implement get settings logic
    return OptimSettings()


@app.put("/rmo/api/v1/scenarios/{sid}/settings")
def update_settings(sid: str, settings: OptimSettings):
    # TODO: Implement update settings logic
    return {"message": "Settings updated"}


@app.post("/rmo/api/v1/env/settings")
def set_global_settings(settings: dict):
    # TODO: Implement set global settings logic
    return {"message": "Global settings updated"}


@app.get("/rmo/api/v1/env/settings")
def get_global_settings():
    # TODO: Implement get global settings logic
    return {"settings": {}}
