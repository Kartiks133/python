import random
import numpy as np
from sklearn.linear_model import LinearRegression

def train_model():
    X = np.array(range(1, 101)).reshape(-1, 1)
    y = np.array([abs(50 - i) for i in range(1, 101)])
    model = LinearRegression()
    model.fit(X, y)
    return model

def play_game():
    print("Welcome to the AI-Powered Guess the Number Game!")
    print("I'm thinking of a number between 1 and 100. Can you guess it?")

    target = random.randint(1, 100)
    model = train_model()
    attempts = 0

    while True:
        try:
            guess = int(input("Enter your guess: "))
            if guess < 1 or guess > 100:
                print("Please guess a number between 1 and 100.")
                continue

            attempts += 1
            prediction = model.predict(np.array([[guess]]))[0]
            closeness = abs(target - guess)

            if guess == target:
                print(f"Congratulations! You guessed it in {attempts} attempts.")
                break
            elif closeness <= 5:
                print("Very Close! Keep trying.")
            elif guess < target:
                print("Too Low!")
            else:
                print("Too High!")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 100.")

if __name__ == "__main__":
    play_game()
