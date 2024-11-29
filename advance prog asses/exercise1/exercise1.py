import random

def displayMenu():
    print("Choose your level:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")

def randomInt(level):
    if level == 1:
        return random.randint(1, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(1000, 9999)

def decideOperation():
    return random.choice(["+", "-"])

def displayProblem(num1, num2, operation):
    print(f"{num1} {operation} {num2} = ", end="")
    try:
        return int(input())
    except ValueError:
        return None

def isCorrect(user_answer, correct_answer):
    return user_answer == correct_answer

def displayResults(score):
    print("\nDone!")
    print(f"Score: {score}/100")
    if score > 90:
        print("Grade: A+")
    elif score > 80:
        print("Grade: A")
    elif score > 70:
        print("Grade: B")
    elif score > 60:
        print("Grade: C")
    else:
        print("Grade: F")

def mathQuiz():
    while True:
        displayMenu()
        try:
            level = int(input("Pick a level (1-3): "))
            if level not in [1, 2, 3]:
                print("Pick 1, 2, or 3.")
                continue
        except ValueError:
            print("Numbers only, please.")
            continue

        score = 0
        for _ in range(10):
            num1 = randomInt(level)
            num2 = randomInt(level)
            operation = decideOperation()
            if operation == "-" and num1 < num2:
                num1, num2 = num2, num1

            correct_answer = num1 + num2 if operation == "+" else num1 - num2

            user_answer = displayProblem(num1, num2, operation)
            if user_answer is not None and isCorrect(user_answer, correct_answer):
                print("You got it!")
                score += 10
                continue

            print("Nope, try again.")
            user_answer = displayProblem(num1, num2, operation)
            if user_answer is not None and isCorrect(user_answer, correct_answer):
                print("Nice save!")
                score += 5
            else:
                print(f"Wrong. It was {correct_answer}.")

        displayResults(score)
        play_again = input("Play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            print("Later!")
            break

mathQuiz()
