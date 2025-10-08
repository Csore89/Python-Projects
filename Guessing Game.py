import random

# Genearte a random number
r = random.randint(1,100)

print("Hello, welcome to my guessing game!")

print("Are your ready to play?")
playing = input("Enter 'yes to play, or 'no' to quit: ").lower()


# Check if the user wants to play
if playing != "yes":
    print("Ok, fine see ya later!")
    quit()

#Ask for the user's name
name = input("Before we begin, what is you name?")
print(f"Ok {name}, let's begin!")

print("I am thinking of a number between 1 and 100.")
guess = int(input("Make your first guess: "))

# Loop until the user guesses the correct number
while guess != r:
    if guess < r:
        print("Too low!  Guess again!")
        guess = int(input("Enter your guess: "))
    elif guess > r:
        print("Too high!  Guess again!")
        guess = int(input("Enter your guess: "))

print(f"Yay, {name}!  You guessed the number {r} correctly!")  #End of the game