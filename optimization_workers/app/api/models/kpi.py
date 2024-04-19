from pydantic import BaseModel


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
