# quiz_app.py

import random
from questions import quiz_questions  #  Imported from another file

# Shuffle the questions
random.shuffle(quiz_questions)

score = 0

print("🎯 Welcome to the Quiz App!\n")

for i, q in enumerate(quiz_questions):
    print(f"Q{i+1}: {q['question']}")
    for option in q["options"]:
        print(option)
    user_answer = input("Your answer (A/B/C/D): ").upper()

    if user_answer == q["answer"]:
        print("✅ Correct!\n")
        score += 1
    else:
        print(f"❌ Wrong! Correct answer is {q['answer']}\n")

print(f"🏁 Quiz Finished! You got {score}/{len(quiz_questions)} correct.")