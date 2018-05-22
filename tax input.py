# -------------------------------------------------------------------
# Compute tax rate
#
# Write a program to request yearly income from the user.  Your program
# will calculate the tax rate for that income
#
# Tax Rates:
#
# Income                  Rate
# 0.0 up to 10000.0        10
# 10000.0 up to 20000.0    20
# 20000.0 up to 100000.0   30
# over 100000.0            35
#
# Example output of your program where the user enters income of 12345.00
#
# Enter income: 12345.00
# Your tax rate is 20%
# -------------------------------------------------------------------

income = float(input("Enter your income: ")
if (income < 10000 and income > 0):
print("Your tax rate is str(10) %")
elif (income > 10000 and income < 20000):
print("Your tax rate is str(20) %")
elif (income > 20000 and income < 100000):
print("Your tax rate is str(25) %")
else:              
print("Your tax rate is str(35) %")
               
               
               
               
               
               
               
               
               