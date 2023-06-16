# Import math module to help calculate compound interest.
import math

# Menu for user to select financial transaction.
print("investment\t-\tto calculate the amount of interest you'll earn on your investment\nmortgage\t-\tto calculate the amount you'll have to pay on a home loan")

user_choice = input("\nType in either 'investment' or 'mortgage' from the menu above to proceed:\t")

# Code to allow for and validate different capitalization.
if user_choice == "investment" or"INVESTMENT" or "Investment" or "mortgage" or "MORTGAGE" or "Mortgage":
    print("Thank you. You may proceed with your choice.")
else:
    print("Invalid entry! Please enter 'investment' or 'mortgage'.")

# Code to standardize user choice variable.
if user_choice == "INVESTMENT" or "Investment" or "MORTGAGE" or "Mortgage":
    user_choice = user_choice.lower()

# If statement for investment path.
if user_choice == "investment":

# Advice to user to only enter numbers in order to avoid errors.
    print(f"\nYou have chosen {user_choice}. Please answer the following questions.\nOnly enter numbers without £ or % signs.\nDo not use commas ','when entering large numbers.")

    principal = int(input("\nHow much do you want to deposit?\t"))
    # The interest rate in the UK just went from 4% to 4.25%, so I decided it might be better to input the rate as a float rather than an integer.
    rate = float(input("\nPlease enter the interest rate.\t\t"))
    time = int(input("\nHow many years do you want to invest?\t"))

# Define variables to use in formulae.
    P = principal
    r = rate/100
    t = time

# Using 0 and 1 to choose between simple and compound interest more efficient than controlling for capitalization as above.
    interest = int(input("\nPlease enter 0 if you want simple interest or 1 if you want compound interest:\t"))
    if interest == 0:
        print("\nYou have chosen simple interest.")
        amount = P*(1 + r*t)
        print(f"\nTotal amount to receive:\t£{amount}\nProfit on initial investment:\t£{amount - principal} ")
    
    else:
        print("\nYou have chosen compound interest.")
        amount = P* math.pow((1 + r), t)

# When calculating compound interest, Python generates floats with large numbers of decimal places. I needed to round these to two.
# I looked up rounding on the W3 website.
# https://www.w3schools.com/python/ref_func_round.asp

        amount = round(amount,2)
        profit = amount - principal
        profit = round(profit,2)

        print(f"\nTotal amount to receive: \t£{amount}\nProfit on initial investment:\t£{profit}")  
    
# Else statement for mortgage path.
else:
    print(f"\nYou have chosen {user_choice}. Please answer the following questions.\nOnly enter numbers without £ or % signs.\nDo not use commas ','when entering large numbers.")
    
    house_price = int(input("\nWhat is the current price of the house?\t"))
    interest_rate = float(input("\nHow much interest will you pay?\t"))

# From a UX point of view, I thought it better to ask the user the number of years needed to pay off the mortgage and then let the programme calculate the months.
    years = int(input("\nHow many years will you need to pay off the mortgage?\t"))
    
    interest_rate = interest_rate/100
    
# Define variables to use in calculation.
    P = house_price
    i = interest_rate/12
    n = years * 12

    repayment = (i * P)/(1 - (1 + i)**(-n))
    repayment = round(repayment, 2)
    print(f"\nYour monthly repayment is exactly:\t£{repayment}")
    
    
