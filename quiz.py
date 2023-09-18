import random

quiz = [
    {
        "Q": "What is 100%10 ?",
        "ANS": "0"
    },
    {
        "Q": "Which keyword is used to define a function in Python?",
        "ANS": "def"
    },
    {
        "Q": "What is the output of 'print(3 * 'Python')'?",
        "ANS": "PythonPythonPython"
    },
    {
        "Q": "Which library is commonly used for data analysis in Python?",
        "ANS": "Pandas"
    },
    {
        "Q": "What does PEP 8 stand for in Python development?",
        "ANS": "Python Enhancement Proposal 8"
    },
    {
        "Q": "What is the purpose of 'pip' in Python?",
        "ANS": "Package management"
    },
    {
        "Q": "What is a 'lambda' function in Python?",
        "ANS": "Anonymous function"
    },
    {
        "Q": "Which module is used for handling regular expressions in Python?",
        "ANS": "re"
    },
    {
        "Q": "which symbol is used for single line comment in Python?",
        "ANS": "#"
    }
]

def randomq():
    return random.choice(quiz)

def startq():
    correct = 0
    totalq = 10

    print("Welcome to the Quiz!")
    print(f"You will be asked {totalq} random quiz questions. Type 'quit' to exit.")

    for _ in range(totalq):
        question_data = randomq()
        question = question_data["Q"]
        answer = question_data["ANS"]

        print("\nQuestion:", question)
        user_answer = input("Your answer: ").strip()

        if user_answer.lower() == "quit":
            break

        if user_answer.lower() == answer.lower():
            print("Correct!")
            correct += 1
        else:
            print(f"Sorry, the correct answer is: {answer}")

    print(f"Quiz completed!\n Your score is: {correct}/{totalq}")

if __name__ == "__main__":
    startq()
