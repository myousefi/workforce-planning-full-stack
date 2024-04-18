from pydantic import BaseModel


class Job(BaseModel):
    job_ID: str
    role: str
    technology: str
    domain: str
    matching_threshold: float
    priority: str
    hire: bool
    disable: bool
