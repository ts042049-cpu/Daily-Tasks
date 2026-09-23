def run_quiz():
    questions = [
        {
            "question": "What is the correct file extension for Python files?",
            "options": ["A) .pyth", "B) .pt", "C) .py", "D) .python"],
            "answer": "C",
        },
        {
            "question": "Which data type is immutable in Python?",
            "options": ["A) List", "B) Tuple", "C) Dictionary", "D) Set"],
            "answer": "B",
        },
        {
            "question": "Which keyword is used to define a function?",
            "options": ["A) func", "B) define", "C) def", "D) function"],
            "answer": "C",
        },
    ]

    score = 0

    for i, q in enumerate(questions, 1):
        print(f"\nQuestion {i}: {q['question']}")
        for option in q["options"]:
            print(f"  {option}")

        # Get and sanitize user input
        user_choice = input("Your answer (A, B, C, or D): ").strip().upper()

        if user_choice == q["answer"]:
            print(" Correct!")
            score += 1
        else:
            print(f" Wrong. The correct answer was {q['answer']}.")

    print(f"\n--- Final Score: {score}/{len(questions)} ---")


if __name__ == "__main__":
    run_quiz()