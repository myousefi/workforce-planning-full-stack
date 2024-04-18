from app.api.main import app
from app.api.models.resource import Resource


@app.get("/rmo/api/v1/scenarios/{sid}/resources")
def list_resources(sid: str):
    # TODO: Implement list resources logic
    return [Resource()]


@app.post("/rmo/api/v1/scenarios/{sid}/resources")
def create_resource(sid: str, resource: Resource):
    # TODO: Implement create resource logic
    return {"message": "Resource created"}


@app.delete("/rmo/api/v1/scenarios/{sid}/resources")
def delete_all_resources(sid: str):
    # TODO: Implement delete all resources logic
    return {"message": "All resources deleted"}


@app.get("/rmo/api/v1/scenarios/{sid}/resources/{id}")
def get_resource(sid: str, id: str):
    # TODO: Implement get resource logic
    return Resource()


@app.put("/rmo/api/v1/scenarios/{sid}/resources/{id}")
def update_resource(sid: str, id: str, resource: Resource):
    # TODO: Implement update resource logic
    return {"message": "Resource updated"}


@app.delete("/rmo/api/v1/scenarios/{sid}/resources/{id}")
def delete_resource(sid: str, id: str):
    # TODO: Implement delete resource logic
    return {"message": "Resource deleted"}
