from backend.database.db import SessionLocal
from backend.evaluation.metrics.similarity import (
    calculate_similarity
)
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

    score = calculate_similarity(
        row.expected_answer,
        answer
    )

    print(f"Generated: {answer}")
    print(f"Score: {score}")

    save_evaluation_result(
        db=db,
        dataset_row_id=row.id,
        generated_answer=answer,
        similarity_score=score
    )

print("Evaluation Complete!")