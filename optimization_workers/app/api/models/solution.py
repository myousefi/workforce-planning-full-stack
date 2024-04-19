from typing import List

from pydantic import BaseModel

from app.api.models.combination import CombinationML


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
