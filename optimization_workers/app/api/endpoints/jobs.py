from app.api.main import app
from app.api.models.job import Job


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
