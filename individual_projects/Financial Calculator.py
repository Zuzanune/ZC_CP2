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
        smom = input("starting amount:  ")
        if text_help(smom, "1") == False:
            print ("invalid input")
            continue
        smom = int(smom)
#     ask user for the annual interest rate
        air = input("annual interest rate:  ")
        if text_help(air, "1") == False:
            print ("invalid input")
            continue
        air = int(air) / 100
#     ask user for the number of years
        year = input("how many years will it be active:  ")
        if text_help(year, "1") == False:
            print ("invalid input")
            continue
        year = int(year)
        break
#     calculate the compound interest
    for x in range(year):
        smom *= (1 + air)
#     return the total amount after interest
    return smom
# def budget_allocator():
def budget_allocator():
#     define budget_categories as a empty dictionary
    b_c = {}
#     ask user how many budget categories they have
    while True:
        b_c_a = input("how many budget catagories do you have")
        if text_help(b_c_a, "1") == False:
            print ("invalid input")
            continue
        b_c_a = int(b_c_a)
#     ask user total monthy income
        tmi = input("what is your monthly income:  ")
        if text_help(tmi, "1") == False:
            print ("invalid input")
            continue
        tmi = int(tmi)
        break
#     in a for loop, ask user what the name of the catagory is, then the percentage of the monthly income it takes up
    for i in range(b_c_a):
        while True:
            tempor = input("what is the name of catagory one:  ")
            if text_help(tempor, "a") == False:
                print ("invalid input")
                continue
            percent = input("what percentage of your income does this catagory take up:  ")
            if text_help(percent, "1") == False:
                print ("invalid input")
                continue
            percent = int(percent)
            break
        b_c[tempor] = round((tmi * (percent / 100)), 2)
#     return dictionary
    return b_c
# def sale_price_calculator(tip):
def sale_price_calculator(tip):
    while True:
#     ask user original cost
        oc = input("what is the original cost:  ")
        if text_help(oc, "1") == False:
            print ("invalid input")
            continue
        oc = int(oc)
#     if tip:
        if tip:
#           ask user tip percent
            tp = input("what is the tip percent:  ")
            if text_help(tp, "1") == False:
                print ("invalid input")
                continue
            tp = int(tp) / 100
#           total percent = 1 + tip percent
            total_percent = 1 + tp
#     else:
        else:
#           ask user discount percent
            dp = input("what is the discount percent:  ")
            if text_help(dp, "1") == False:
                print ("invalid input")
                continue
            dp = int(dp) / 100
#           total percent = 1 - discount percent
            total_percent = 1 - dp
        break
#     multiply original by total percent
    total = oc * total_percent
    # return total
    return total
# def tip_calculator():
def tip_calculator():
#      return sale_price_calculator(True)
    return sale_price_calculator(True)
# def main():
def main():
    #while True:
    while True:
        # ask user which aspect of the financial calculator they want to use
        #1. Savings Time Calculator
        #2. Compound Interest Calculator
        #3. Budget Allocator
        #4. Sale Price Calculator
        #5. Tip Calculator
        print("Which calculator would you like to use?")
        print("1. Savings Time Calculator")
        print("2. Compound Interest Calculator")
        print("3. Budget Allocator")
        print("4. Sale Price Calculator")
        print("5. Tip Calculator")
        choice = input("Enter the number of your choice: ")
        if choice == "1":
            time_needed = STC()
            print(f"It will take {time_needed} periods to reach your savings goal.")
        elif choice == "2":
            total_amount = CIC()
            print(f"The total amount after interest is: {total_amount}")
        elif choice == "3":
            budget = budget_allocator()
            print("Your budget allocation is as follows:")
            for category, amount in budget.items():
                print(f"{category}: ${amount}")
        elif choice == "4":
            new_price = sale_price_calculator(False)
            print(f"The new sale price is: ${new_price}")
        elif choice == "5":
            total_with_tip = tip_calculator()
            print(f"The total amount with tip is: ${total_with_tip}")
        else:
            print("Invalid input.")
        
        again = input("Would you like to perform another calculation? (yes/no): ")
        if again.lower() != "yes":
            break

