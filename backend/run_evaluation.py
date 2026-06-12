from backend.database.db import SessionLocal

from backend.database.models import DatasetRow

from backend.adapters.gemini_adapter import (
    generate_answer
)

from backend.services.dataset_service import (
    save_evaluation_result
)


db = SessionLocal()

rows = db.query(DatasetRow).all()

for row in rows:

    print(f"Question: {row.question}")

    answer = generate_answer(
        row.question
    )

    print(f"Generated: {answer}")

    save_evaluation_result(
        db=db,
        dataset_row_id=row.id,
        generated_answer=answer
    )

print("Evaluation Complete!")