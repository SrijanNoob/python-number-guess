import random

print("Welcome to the Number Guessing Game!")

while True:
    valid = ["easy", "medium", "hard"]
    difficulty = input("Choose difficulty (easy/medium/hard): ").lower()
    if difficulty in valid:
        break
    else:
        print("Invalid choice. Please pick easy, medium, or hard.")

print(f"Difficulty set to: {difficulty}")

if difficulty == valid[0]:
    chances = 10
elif difficulty == valid[1]:
    chances = 5
elif difficulty == valid[2]:
    chances = 3
print(f"Great! You have selected the {difficulty} difficulty level.")
print(f"You have {chances} chances to guess the correct number.")
print("Let's start the game!")

num = random.randint(1, 100)
Tries = 0
while Tries < chances:
    Tries += 1

    while True:
        try:
            guess = int(input("Enter your guess: "))
            break
        except ValueError:
            print("Please enter a valid number.")

    if not (1 <= guess <= 100):
        print("Your number is too high or too low!")
        if Tries == chances:
            print("You've run out of attempts!")
            print(f"The number I was thinking of was {num}.")
            print("Better luck next time!")
        continue

    if guess == num:
        print(f"Congratulations! You guessed the correct number in {Tries} attempts.")
        break
    elif guess > num:
        print(f"Incorrect! The number is less than {guess}.")
    elif guess < num:
        print(f"Incorrect! The number is greater than {guess}.")

    if Tries == chances:
        print("You've run out of attempts!")
        print(f"The number I was thinking of was {num}.")
        print("Better luck next time!")


    











