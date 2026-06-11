from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from backend.database.db import get_db
from backend.database.schemas import DatasetCreate
from backend.services.dataset_service import create_dataset

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