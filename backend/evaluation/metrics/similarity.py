from difflib import SequenceMatcher


def calculate_similarity(
    expected_answer,
    generated_answer
):

    score = SequenceMatcher(
        None,
        expected_answer.lower(),
        generated_answer.lower()
    ).ratio()

    return round(score, 2)