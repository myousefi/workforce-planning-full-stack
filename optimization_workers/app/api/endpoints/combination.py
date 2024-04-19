from fastapi import HTTPException, APIRouter
from app.api.models.combination import Combination
from app.services.database.mongodb import db

router = APIRouter()


@router.get("/rmo/api/v1/scenarios/{sid}/combinations")
def list_combinations(sid: str):
    combinations = db.combinations.find({"scenario_id": sid})
    return [Combination(**combination) for combination in combinations]


@router.post("/rmo/api/v1/scenarios/{sid}/combinations")
def create_combination(sid: str, combination: Combination):
    combination_data = combination.dict()
    combination_data["scenario_id"] = sid
    result = db.combinations.insert_one(combination_data)
    combination_data["_id"] = str(result.inserted_id)
    return Combination(**combination_data)


@router.delete("/rmo/api/v1/scenarios/{sid}/combinations")
def delete_all_combinations(sid: str):
    db.combinations.delete_many({"scenario_id": sid})
    return {"message": "All combinations deleted"}


@router.get("/rmo/api/v1/scenarios/{sid}/combinations/{id}")
def get_combination(sid: str, id: str):
    combination = db.combinations.find_one({"_id": id, "scenario_id": sid})
    if combination:
        return Combination(**combination)
    raise HTTPException(status_code=404, detail="Combination not found")


@router.put("/rmo/api/v1/scenarios/{sid}/combinations/{id}")
def update_combination(sid: str, id: str, combination: Combination):
    combination_data = combination.dict(exclude_unset=True)
    result = db.combinations.update_one(
        {"_id": id, "scenario_id": sid}, {"$set": combination_data}
    )
    if result.modified_count:
        return {"message": "Combination updated"}
    raise HTTPException(status_code=404, detail="Combination not found")


@router.delete("/rmo/api/v1/scenarios/{sid}/combinations/{id}")
def delete_combination(sid: str, id: str):
    result = db.combinations.delete_one({"_id": id, "scenario_id": sid})
    if result.deleted_count:
        return {"message": "Combination deleted"}
    raise HTTPException(status_code=404, detail="Combination not found")
