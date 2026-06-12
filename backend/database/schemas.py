from pydantic import BaseModel
from datetime import datetime


class DatasetCreate(BaseModel):
    name: str
    description: str


class DatasetResponse(BaseModel):
    id: int
    name: str
    description: str
    created_at: datetime

    class Config:
        from_attributes = True


class DatasetRowCreate(BaseModel):
    question: str
    expected_answer: str


class DatasetRowResponse(BaseModel):
    id: int
    dataset_id: int
    question: str
    expected_answer: str

    class Config:
        from_attributes = True