
import random

userGuess = 0

n = random.randint(1,100)

while userGuess < 8:
    guess = int(input("Enter your guess from 1 to 100: "))
    
    userGuess = userGuess + 1;
    
    if guess > n:
      print('Guess too high')
    
    if guess < n:
      print('Guess too low')
    
    if guess == n:
      break

if guess == n:
    userGuess = str(userGuess)
    print ('You took ' + userGuess + ' guesses ')
    
if guess!= n:
    n = str(n)
    print ('the number i was thinking of is ' + n)
    

    
    
   