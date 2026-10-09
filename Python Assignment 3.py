import random

# Generate a random number between 1 and 10
secret_number = random.randint(1, 10)

# Maximum number of attempts
attempts = 3

while attempts > 0:
    guess = int(input("Guess the number (between 1 and 10): "))

    if guess < 1 or guess > 10:
        print("Your guess is out of range. Please guess a number between 1 and 10.")
        continue

    attempts -= 1

    if guess < secret_number:
        print("Too low. Try again.")

    elif guess > secret_number:
        print("Too high. Try again.")

    else:
        print("Congratulations! You guessed the correct number.")
        break

else:
    print("Better luck next time! The correct number was", secret_number)


    # Task 2: Multiplication Table Generator

number = int(input("Enter the number for which you want the multiplication table: "))

for i in range(1, 11):
    print(number, "x", i, "=", number * i)


# Task 3: BMI Calculator

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi


weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

bmi = calculate_bmi(weight, height)

print("Your BMI is:", round(bmi, 2))