import random

numberofGuess = 0
number = random.randint(1,100)

name = input("Hello! What is your name? ")

print(name + ", I am thinking of a whole number between 1 and 100.")

while numberofGuess < 5:
  guess = input("Take a guess ")
  guess = int(guess)

  numberofGuess = numberofGuess + 1;

  if guess < number:
    print("Your guess is too low!")

  if guess > number:
    print("Your guess is too high!")

  if guess==number:
    break

if guess==number:
  numberofGuess=str(numberofGuess)
  print("Good job! You took " + numberofGuesses + " guesses :)")

if guess!=number:
  number=str(number)
  print("Sorry. The number I was thinking of was " + number + " :)")