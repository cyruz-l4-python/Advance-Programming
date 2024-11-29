import random
import os

def loadJokes():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, 'randomJokes.txt')
    with open(file_path, 'r') as file:
        return file.readlines()

def tellJoke(jokes):
    joke = random.choice(jokes).strip()
    setup, punchline = joke.split('?', 1)
    print(setup + "?")
    input("Press Enter for the punchline...")
    print(punchline)

def runJokeProgram():
    jokes = loadJokes()
    while True:
        command = input('Say "Alexa tell me a joke" to hear a joke or "quit" to exit: ')
        if command.lower() == 'alexa tell me a joke':
            tellJoke(jokes)
        elif command.lower() == 'quit':
            print("Goodbye!")
            break
        else:
            print("Invalid command. Try again.")

runJokeProgram()
