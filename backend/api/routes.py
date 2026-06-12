from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from backend.database.db import get_db
from backend.database.schemas import DatasetCreate
from backend.database.schemas import DatasetRowCreate
from backend.services.dataset_service import (
    create_dataset,
    get_all_datasets,
    get_dataset_by_id,
    create_dataset_row,
    get_dataset_rows
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

@router.post("/datasets/{dataset_id}/rows")
def create_row(
    dataset_id: int,
    row: DatasetRowCreate,
    db: Session = Depends(get_db)
):

    result = create_dataset_row(
        db=db,
        dataset_id=dataset_id,
        question=row.question,
        expected_answer=row.expected_answer
    )

    return result

@router.get("/datasets/{dataset_id}/rows")
def get_rows(
    dataset_id: int,
    db: Session = Depends(get_db)
):

    rows = get_dataset_rows(
        db=db,
        dataset_id=dataset_id
    )

    return rows