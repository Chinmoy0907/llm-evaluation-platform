from backend.database.models import Dataset
from backend.database.models import DatasetRow


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