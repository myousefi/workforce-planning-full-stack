from pydantic import BaseModel


class OptimParams(BaseModel):
    threshold_flag: bool
    hiring_flag: bool
    preallocation_flag: bool
    hiring_limit: float


class OptimSettings(BaseModel):
    params: OptimParams
