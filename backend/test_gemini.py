from adapters.gemini_adapter import generate_answer

response = generate_answer(
    "What is the capital of India?"
)

print(response)