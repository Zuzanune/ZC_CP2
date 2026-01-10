# ZC 1st Financial Calculator.py
def validate_input(text, kind):
    s = str(text).strip()
    if kind == 'int':
        try:
            int(s)
            return True
        except ValueError:
            return False
    elif kind == 'float':
        try:
            float(s)
            return True
        except ValueError:
            return False
    elif kind == 'alpha':
        return s.isalpha()
    else:
        return False
# def savings_time_calculator function():
def STC():
    #     ask user how much they are contributing and how often they contribute
    while True:
        con = input("how much are you contributing?  ")
        if not validate_input(con, 'int'):
            print("invalid input")
            continue
        con = int(con)
        time = input("how often are you contributing. enter weekly or monthly")
        if not validate_input(time, 'alpha'):
            print("invalid input")
            continue
        goal = input("what is your goal?")
        if not validate_input(goal, 'int'):
            print("invalid input")
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
        if not validate_input(smom, 'float'):
            print("invalid input")
            continue
        smom = float(smom)
#     ask user for the annual interest rate
        air = input("annual interest rate:  ")
        if not validate_input(air, 'float'):
            print("invalid input")
            continue
        air = float(air) / 100
#     ask user for the number of years
        year = input("how many years will it be active:  ")
        if not validate_input(year, 'int'):
            print("invalid input")
            continue
        year = int(year)
        break
#     calculate the compound interest
    def compound(pri, rate, years):
        result = pri
        for _ in range(years):
            result *= (1 + rate)
        return result
#     return the total amount after interest
    return compound(smom, air, year)
# def budget_allocator():
def budget_allocator():
#     define budget_categories as a empty dictionary
    b_c = {}
    total_percent = 0
#     ask user how many budget categories they have
    while True:
        b_c_a = input("how many budget catagories do you have")
        if not validate_input(b_c_a, 'int'):
            print("invalid input")
            continue
        b_c_a = int(b_c_a)
#     ask user total monthy income
        tmi = input("what is your monthly income:  ")
        if not validate_input(tmi, 'float'):
            print("invalid input")
            continue
        tmi = float(tmi)
        break
#     in a for loop, ask user what the name of the catagory is, then the percentage of the monthly income it takes up
    for i in range(b_c_a):
        while True:
            tempor = input(f"what is the name of catagory {i+1}:  ")
            if not validate_input(tempor, 'alpha'):
                print("invalid input")
                continue
            percent = input("what percentage of your income does this catagory take up:  ")
            if not validate_input(percent, 'int'):
                print("invalid input")
                continue
            percent = int(percent)
            if total_percent + percent > 100:
                print (f"invalid input. You have {100 - total_percent}% remaining.")
                continue
            break
        total_percent += percent
        b_c[tempor] = round((tmi * (percent / 100)), 2)
#     return dictionary
    return b_c
# def sale_price_calculator(tip):
def sale_price_calculator(tip):
    while True:
#     ask user original cost
        oc = input("what is the original cost:  ")
        if not validate_input(oc, 'float'):
            print("invalid input")
            continue
        oc = float(oc)
#     if tip:
        if tip:
#           ask user tip percent
            tp = input("what is the tip percent:  ")
            if not validate_input(tp, 'float'):
                print("invalid input")
                continue
            tp = float(tp) / 100
#           total percent = 1 + tip percent
            total_percent = 1 + tp
#     else:
        else:
#           ask user discount percent
            dp = input("what is the discount percent:  ")
            if not validate_input(dp, 'float'):
                print("invalid input")
                continue
            dp = float(dp) / 100
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
            print ("goodbye")
            break
main()
