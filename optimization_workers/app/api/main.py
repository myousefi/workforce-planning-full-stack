from typing import List

from fastapi import FastAPI
from pydantic import BaseModel

from app.api.endpoints.combination import router as combination_router
from app.api.endpoints.jobs import router as jobs_router
from app.api.endpoints.resource import router as resource_router
from app.api.endpoints.scenario import router as scenario_router
from app.api.endpoints.settings import router as settings_router
from app.api.models.kpi import KPI
from app.api.models.solution import Solution

app = FastAPI()

app.include_router(scenario_router)
app.include_router(jobs_router)
app.include_router(settings_router)
app.include_router(scenario_router)
app.include_router(combination_router)
app.include_router(resource_router)


class ErrorMessage(BaseModel):
    code: str
    message: str
    scenario: str


# Define Pydantic models for request/response bodies


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


@app.get("/rmo/api/v1/scenarios/{sid}/solution")
def get_solution(sid: str):
    # TODO: Implement get solution logic
    return Solution()


@app.get("/rmo/api/v1/scenarios/{sid}/kpi")
def get_kpi(sid: str):
    # TODO: Implement get KPI logic
    return KPI()
