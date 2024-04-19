from pydantic import BaseModel


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
