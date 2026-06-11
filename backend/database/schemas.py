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