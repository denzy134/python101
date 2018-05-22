# 04: CS101 Team Activity
# 
# These are simple coding problems.  You will not be submitting anything
# for points.  Please work together on this.  Add your code for every
# TODO section.  Copy this code to Thonny, or your python system.
# Use the print() function to get the output that is in the double quotes.
#
# This team activity is on Boolean Expressions and if statements
# *******************************************************************

# -------------------------------------------------------------------
# Convert US to Euro
#
# Write a program to request a dollar amount from the user and convert
# it to Euros.  Find the current change rate from the Internet and use
# it in your program
#
# Example output of your program where the user enters 100.0 dollars
#
# Enter dollars: 100.0
# 100.0 dollars is 85.0 Euros
# -------------------------------------------------------------------

# TODO Add your code here



dollarInput = int(input("Enter dollars: "))

dollars = 1.18
euro = dollars * dollarInput
print (str(dollarInput),  "dollars is "+ str(euro) + " Euros")

           