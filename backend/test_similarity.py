from backend.evaluation.metrics.similarity import (
    calculate_similarity
)

print(
    calculate_similarity(
        "New Delhi",
        "The capital of India is New Delhi"
    )
)