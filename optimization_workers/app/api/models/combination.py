from pydantic import BaseModel


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
