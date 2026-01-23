#ZC 2nd password generator
#import random
import random
#define lists of all lowercase, uppercase, and special characters
def main():
    global length
    lowercase = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special = "!@#$%^&*()-+"
    numbers = "1234567890"
    spaces = "   "
    passwords = []
    #ask user for password length, type 0 for random
    length = int(input("Enter password length (0 for random): "))

    
    #ask user if they want uppercase, lowercase, special characters
    quest = input("do you want lowercase characters? (y/n)  ")
    if quest == "yes" or quest == "y":
        lower = True
    else:
        lower = False
    quest = input("do you want uppercase characters? (y/n)  ")
    if quest == "yes" or quest == "y":
        upper = True
    else:
        upper = False
    quest = input("do you want special characters? (y/n)  ")
    if quest == "yes" or quest == "y":
        specia = True
    else:
        specia = False
    quest = input("do you want numbers? (y/n)")
    if quest == "yes" or quest == "y":
        nums = True
    else:
        nums = False
    quest = input("do you want spaces? (Y/N)")
    if quest == "yes" or quest == "y":
        space = True
    else:
        space = False
    if lower == False and upper == False and specia == False and nums == False:
        print ("there is no valid passwords that match your criteria")
        return
    quest = input("how many passwords would you like to generate?  ")
    num_passwords = int(quest)
    #loop 4 times:
    def generate_passcode():
        global length
        #if user picked 0, generate random length between 6 and 16
        if length == 0:
            length = random.randint(6, 16)
        case1 = ""
        case2 = ""
        spec = ""
        if lower:
            case1 += lowercase
        if upper:
            case2 += uppercase
        if specia:
            spec += special
        if nums:
            spec += numbers
        if space:
            spec += spaces
        for x in range(1,num_passwords + 1):
            #generate password by picking random characters from the selected character sets until len = the max amount
            password = ""
            for i in range(length):
                password += random.choice(case1 + case2 + spec)
            passwords.append(password)
    generate_passcode() 
    #display list
    count = 0
    for pwd in passwords:
        count += 1
        print(f"{count}: {pwd}")
print ("welcome to the password generator")
while True:
    main()
    cont = input("Do you want to generate another password? (y/n) ")
    if cont.lower() != "y":
        break