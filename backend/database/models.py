from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey

from sqlalchemy.orm import relationship

from database.db import Base

from datetime import datetime

class Dataset(Base):
    __tablename__ = "datasets"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    description = Column(Text)
    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    # Relationship between two tables 
    rows = relationship(
        "DatasetRow",
        back_populates="dataset",
        cascade="all, delete-orphan"
        )
    
class DatasetRow(Base):
    __tablename__ = "dataset_rows"

    id = Column(Integer, primary_key=True, index=True)
    dataset_id = Column(
        Integer,
        ForeignKey("datasets.id")
    )

    question = Column(Text, nullable=False)
    expected_answer = Column(Text)
    dataset = relationship(
        "Dataset",
        back_populates="rows"
    )