from fastapi import APIRouter
from app.api.models.job import Job


router = APIRouter()


@router.get("/rmo/api/v1/scenarios/{sid}/jobs")
def list_jobs(sid: str):
    # TODO: Implement list jobs logic
    return [Job()]


@router.post("/rmo/api/v1/scenarios/{sid}/jobs")
def create_job(sid: str, job: Job):
    # TODO: Implement create job logic
    return {"message": "Job created"}


@router.delete("/rmo/api/v1/scenarios/{sid}/jobs")
def delete_all_jobs(sid: str):
    # TODO: Implement delete all jobs logic
    return {"message": "All jobs deleted"}


@router.get("/rmo/api/v1/scenarios/{sid}/jobs/{id}")
def get_job(sid: str, id: str):
    # TODO: Implement get job logic
    return Job()


@router.put("/rmo/api/v1/scenarios/{sid}/jobs/{id}")
def update_job(sid: str, id: str, job: Job):
    # TODO: Implement update job logic
    return {"message": "Job updated"}


@router.delete("/rmo/api/v1/scenarios/{sid}/jobs/{id}")
def delete_job(sid: str, id: str):
    # TODO: Implement delete job logic
    return {"message": "Job deleted"}
