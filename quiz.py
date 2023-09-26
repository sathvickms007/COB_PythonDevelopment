import random

quiz = {
    "What is the capital of France?": "Paris",
    "Which planet is known as the Red Planet?": "Mars",
    "How many continents are there on Earth?": "7",
    "What is the largest mammal in the world?": "Blue Whale",
    "What is the chemical symbol for gold?": "Au",
    "What is the largest organ in the human body?": "Skin",
    "What gas do plants absorb from the atmosphere during photosynthesis?": "Carbon Dioxide",
    "What is the smallest prime number?": "2",
    "Which gas do humans need to breathe in and plants need to perform photosynthesis?": "Oxygen",
    "What is the powerhouse of the cell?": "Mitochondria",
    "What is the largest planet in our solar system?": "Jupiter",
    "What is the chemical symbol for water?": "H2O",
    "What is the largest desert in the world?": "Antarctica",
    "What is the tallest mountain in the world?": "Mount Everest",
    "What is the chemical symbol for oxygen?": "O2",
    "What is the primary function of the heart?": "Pumping blood",
    "What is the closest planet to the Sun?": "Mercury",
    "What is the chemical symbol for carbon?": "C",
    "What is the largest ocean on Earth?": "Pacific Ocean",
    "What is the chemical symbol for silver?": "Ag",
    "What gas do plants release during photosynthesis?": "Oxygen",
    "How many continents are entirely in the southern hemisphere?": "1",
    "What is the second most abundant gas in Earth's atmosphere?": "Oxygen",
    "What is the chemical symbol for sodium?": "Na",
    "What is the chemical symbol for potassium?": "K",
    "What is the largest moon in our solar system?": "Ganymede",
    "What is the chemical symbol for hydrogen?": "H",
    "What is the chemical symbol for nitrogen?": "N",
    "What is the chemical symbol for helium?": "He",
}

def rand_q():
    que = random.choice(list(quiz.keys()))
    ans = quiz[que]
    return que, ans

# Function to play the quiz
def start():
    marks = 0
    c=0
    while True:
        que, ans = rand_q()
        c+=1
        print("\nQuestion:", que)
        inp_ans = input("Your answer: ").strip()

        if inp_ans.lower() == ans.lower():
            print("Correct!")
            marks += 1
        else:
            print("Wrong! The correct answer is:", ans)

        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != "y":
            break

    print("Quiz completed! Your marks is:", marks," out of ",c)

if __name__ == "__main__":
    print("Welcome to the Quiz!")
    start()
