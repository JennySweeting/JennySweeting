import math

# Explanation of 'investment' and 'bond' calculators. 
# Prompt user to input which calculator they would like to use.
print("Investment - to calculate the amount of interest you'll earn on your investment")
print("Bond - to calculate the amount of interest you'll have to pay on a home loan")
print()
calculator_type = input("Enter either 'investment' or 'bond' from the menu above to proceed: ")

# Creating a calculator for 'investments'.
# Prompt user to enter the amount they are depositing, interest rate,
#   the number of years investing and if they would like 'simple' or 'compound'
#     interest to be calculated.
# Create else statement to print error message if neither 'simple' or
#   'compound' is entered. 
# Enter the algebraic equations for each calculator inputting the corresponding
#   variables.
# Format the results to print with 2 decimal places.

   
if calculator_type.lower() == "investment":
    amount = float(input("Please enter the amount you are depositing: "))
    percentage_rate = float(input("Please enter the interest rate (just the number, please): "))
    div_percentage = percentage_rate / 100
    years = int(input("Please enter the number of years you are investing: "))
    interest = str(input("Would you like to calculate simple or compound interest? Please type 'simple' or 'compound': "))

    if interest == "simple":
        print()
        simple_rate = ((amount *(1+div_percentage*years)))
        simple_decimal = format(simple_rate, ".2f")
        print("Total after investment period: " + simple_decimal)
    elif interest == "compound":
        print()
        compound_rate = (amount * math.pow((1+div_percentage),years))
        compound_decimal = format(compound_rate, ".2f")
        print("Total after investment period: " + compound_decimal)
    else:
        print("Oops, sorry I didn't recognise your request!")

# Creating a calculator for 'bonds'.
# Prompt user to enter the value of the house, interest rate and how 
#   many months they will take to repay. 
# Enter the algebraic equations for each calculator inputting the corresponding
#   variables.
# Format the results to print with 2 decimal places.

elif calculator_type.lower() == "bond":
    house_value = int(input("Please enter the value of your house: "))
    interest_rate = float(input("Please enter the interest rate: "))
    div_interest = interest_rate / 100 / 12      
    months = int(input("Please enter the time period for repaying the bond (in months): "))
    total = (div_interest * house_value)/(1 - (1+div_interest)**(-months))
    decimal_total = format(total, ".2f")
    print()
    print("The amount you will pay each month is: " + decimal_total)

# Else statement to prompt user to enter valid input to access calculators.
else:
    print("Error! Invalid input, please try again!")










