import random

# Generate a random number between 1 and 100
number_to_guess = random.randint(1, 100)

print ("Welcome to the Guess the Number game!")
print ("I have chosen a number between 1 and 100. Can you guess ir?")

while True:
    # Ask the user for their guess
    guess = input("Enter your guess:")

    # Check if the input is a number
    if not guess.isdigit():
        print ("Please enter a valid number.")
        continue 

    # Convert the input to an integer
    guess = int (guess)

    # Compare the guess to the number
    if guess < number_to_guess:
        print("Too low! Try again.")
    elif guess > number_to_guess:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed the number!")
        break 
              