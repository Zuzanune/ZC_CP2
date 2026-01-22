#ZC 2nd password generator
#import random
import random
#define lists of all lowercase, uppercase, and special characters
lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
special = "!@#$%^&*()-+"
passwords = []
#ask user for password length, type 0 for random
length = int(input("Enter password length (0 for random): "))

#if user picked 0, generate random length between 6 and 16
if length == 0:
    length = random.randint(6, 16)
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
    special = True
else:
    special = False
#loop 4 times:
for x in range(1,4):
    #generate password by picking random characters from the selected character sets until len = the max amount
    password = ""
    for i in range(length):
        password += random.choice(lowercase + uppercase + special)
    passwords.append(password)

#display list