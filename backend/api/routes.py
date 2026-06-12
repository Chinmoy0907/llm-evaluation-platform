from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from backend.database.db import get_db
from backend.database.schemas import DatasetCreate
from backend.services.dataset_service import (
    create_dataset,
    get_all_datasets,
    get_dataset_by_id
)

router = APIRouter()


@router.post("/datasets")
def create_dataset_api(
    dataset: DatasetCreate,
    db: Session = Depends(get_db)
):

    result = create_dataset(
        db=db,
        name=dataset.name,
        description=dataset.description
    )

    return {
        "id": result.id,
        "name": result.name,
        "description": result.description
    }

@router.get("/datasets")
def get_datasets(
    db: Session = Depends(get_db)
):

    datasets = get_all_datasets(db)

    return datasets

@router.get("/datasets/{dataset_id}")
def get_dataset(
    dataset_id: int,
    db: Session = Depends(get_db)
):

    dataset = get_dataset_by_id(
        db,
        dataset_id
    )

    if not dataset:
        return {
            "error": "Dataset not found"
        }

    return dataset