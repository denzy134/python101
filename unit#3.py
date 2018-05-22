print("This is a Tithing Calculator\n")

moneyEarned = int(input("Enter how much money you earned: "))
print ("Your total amount is:", "$", moneyEarned)
 
fastOffering = int(input("Enter how much you would like to pay for fast offering: "))
print ("Your fast offering is: $ ", fastOffering)
titheOwed = (10/100) * moneyEarned
totalContributions = titheOwed + fastOffering
 
print ("You will pay $ ", (round(totalContributions,2)), "as your total tithe.")


