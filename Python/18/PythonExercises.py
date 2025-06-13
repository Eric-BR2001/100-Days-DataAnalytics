import random

def generate_question():
    operations = ['+', '-', '*']
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operation = random.choice(operations)
    
    if operation == '+':
        correct_answer = num1 + num2
    elif operation == '-':
        correct_answer = num1 - num2
    elif operation == '*':
        correct_answer = num1 * num2

    return f"What is {num1} {operation} {num2}?", correct_answer

def run_quiz():
    score = 0
    total_questions = 5

    print("Welcome to the Math Quiz!")
    print(f"You'll get {total_questions} questions.\n")

    for i in range(total_questions):
        question, answer = generate_question()
        try:
            user_answer = int(input(f"{i+1}) {question} "))
            if user_answer == answer:
                print("Correct!\n")
                score += 1
            else:
                print(f"Wrong! The correct answer was {answer}.\n")
        except ValueError:
            print("Please enter a valid number.\n")

    print(f"Quiz completed! Your score: {score}/{total_questions}")

if __name__ == "__main__":
    run_quiz()
