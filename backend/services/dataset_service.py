from backend.database.models import Dataset
from backend.database.models import DatasetRow
import pandas as pd
from backend.database.models import DatasetRow
from backend.database.models import (
    Dataset,
    DatasetRow,
    EvaluationResult
)


def create_dataset(db, name, description):

    dataset = Dataset(
        name=name,
        description=description
    )

    db.add(dataset)
    db.commit()
    db.refresh(dataset)

    return dataset

def get_all_datasets(db):
    return db.query(Dataset).all()

def get_dataset_by_id(db, dataset_id):
    return (
        db.query(Dataset)
        .filter(Dataset.id == dataset_id)
        .first()
    )

def create_dataset_row(
    db,
    dataset_id,
    question,
    expected_answer
):

    row = DatasetRow(
        dataset_id=dataset_id,
        question=question,
        expected_answer=expected_answer
    )

    db.add(row)
    db.commit()
    db.refresh(row)

    return row

def get_dataset_rows(
    db,
    dataset_id
):

    return (
        db.query(DatasetRow)
        .filter(
            DatasetRow.dataset_id == dataset_id
        )
        .all()
    )

def upload_dataset_csv(
    db,
    dataset_id,
    file_path
):

    df = pd.read_csv(file_path)

    created_rows = 0

    for _, row in df.iterrows():

        dataset_row = DatasetRow(
            dataset_id=dataset_id,
            question=row["question"],
            expected_answer=row["expected_answer"]
        )

        db.add(dataset_row)

        created_rows += 1

    db.commit()

    return {
        "rows_created": created_rows
    }

def save_evaluation_result(
    db,
    dataset_row_id,
    generated_answer,
    similarity_score
):

    result = EvaluationResult(
        dataset_row_id=dataset_row_id,
        generated_answer=generated_answer,
        similarity_score=similarity_score
    )

    db.add(result)

    db.commit()

    db.refresh(result)

    return result