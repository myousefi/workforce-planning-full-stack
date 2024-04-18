from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

from app.api.models.kpi import KPI
from app.api.models.solution import Solution

app = FastAPI()


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
