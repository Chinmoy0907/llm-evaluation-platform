from backend.database.models import Dataset


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