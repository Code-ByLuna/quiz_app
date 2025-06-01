def run_quiz():
    questions = [
    {
        "question": "What is the capital of India?",
        "options": {
            "A": "Berlin",
            "B": "New Delhi",
            "C": "Rome",
            "D": "Paris"
        },
        "answer": "B"
    },
    {
        "question": "Who developed Python?",
        "options": {
            "A":"Elon Musk",
            "B": "Guido van Rossum",
            "C": "Dennis Ritchie",
            "D": "Sundar Pichai"
        },
        "answer": "B"
    },
    {
        "question": "What is 2+3?",
        "options": {
            "A": "5",
            "B": "9",
            "C": "10",
            "D": "25"
        },
        "answer": "A"
    } 
]
    score=0
    for i,q in enumerate(questions,1):
        print("\n"+ q["question"])
        for key, val in q["options"].items():
         print(f"{key}. {val}")
        user_ans = input("Your answer(A/B/C/D):").strip().upper()
        if user_ans==q["answer"]:
         print("Correct answer!")
         score=score+1
        else:
         print(f"Wrong answer! Correct answer was {q['answer']}")
    print("\n----QUIZ COMPLETE----")
    print(f"\nYour final score is {score}/{len(questions)}")

    if score==len(questions):
     print("🌟 Excellent! You're a quiz master!")
    elif score>= len(questions)//2:
     print("👍Good job!Keep practicing.")
    else:
     print("😊Don't worry! Try again.")
#ask to restart
    restart=input("\n Do you want to try again?(yes/no):").strip().lower()
    if restart=="yes":
     run_quiz()
    else:
        print("👋Thanks for playing!")
    
run_quiz()