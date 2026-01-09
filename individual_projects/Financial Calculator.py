# ZC 1st Financial Calculator.py
def text_help(text, type):
    if type.isnumeric():
        if text.isnumeric():
            return True
        else:
            return False
    elif type.isalpha():
        if text.isalpha():
            return True
        else:
            return False
# def savings_time_calculator function():
def STC():
    #     ask user how much they are contributing and how often they contribute
    while True:
        con = input("how much are you contributing?  ")
        if text_help(con, "1") == False:
            print ("invalid input")
            continue
        con = int(con)
        time = input("how often are you contributing. enter weekly or monthly")
        if text_help(time, "a") == False:
            print ("invalid input")
            continue
        goal = input("what is your goal?")
        if text_help(goal, "1") == False:
            print ("invalid input")
            continue
        goal = int(goal)
        break
    #     calculate how long it will take to reach their savings goal
    count = 0
    tot = 0
    while True:
        count += 1
        tot += con
        if tot >= goal:
            break
    #     return the result
    return count
# def compound_interest_calculator():
def CIC():
    while True:
        #     ask user for the starting amount of money
        smon = input("startin amount:  ")
        if text_help(smon, 1) == False:
            print ("invalid input")
            
#     ask user for the annual interest rate
#     ask user for the number of years
#     calculate the compound interest
#     return the total amount after interest
# def budget_allocator():
#     define budget_categories as a empty dictionary
#     ask user how many budget categories they have
#     ask user total monthy income
#     in a for loop, ask user what the name of the catagory is, then the percentage of the monthly income it takes up
#     return dictionary
# def sale_price_calculator(tip):
#     ask user original cost
#     if tip:
#           ask user tip percent
#           total percent = 1 + tip percent
#     else:
#           ask user discount percent
#           total percent = 1 - discount percent
#     multiply original by total percent
#     return total
# def tip_calculator():
#      return sale_price_calculator(True)
# def main():
    #while True:
        # ask user which aspect of the financial calculator they want to use
        #1. Savings Time Calculator
        #2. Compound Interest Calculator
        #3. Budget Allocator
        #4. Sale Price Calculator
        #5. Tip Calculator
        # if one:
    #       print the amount of time it will take is: savings_time_calculator()
        #if 2:
#           tell user total amount. call CIP calculator
#       if 3:
#           go through dictionary and tell user each key value pair
#       if 4:
#           tell user items new price
#       if 5:
#           tell user items new price

