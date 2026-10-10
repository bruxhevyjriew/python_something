import math
import random

x = random.randint(0, 100)
y = 2 * x
z = 0

print("Guess the number!")
print("Five guesses, 0–100.\n")

while x != y:
    z = z + 1
    while True:
        y = input(f"({z}/5) Enter your guess: ")
        try:
            y = int(y)
            break
        except ValueError:
            print("Please input a number!")
    if y == x:
        print(f"{y} is the answer. You win!")
        break
    elif z == 5:
        print(f"Game Over! The correct answer was {x}.")
        break
    if y > x and z != 5:
        print(f"Too high. Try again!")
    if y < x and z != 5:
        print(f"Too low. Try again!")