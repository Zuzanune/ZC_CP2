from RPGhelper import create_character, load_characters, editcharacters, save_character, compare
import pandas as pd
import matplotlib.pyplot as plt
print ("Welcome to the RPG Character Manager! \n here you can create and manage your RPG characters! \n compatable with Dungeons and Dragons 5th edition! \n")
def menu():
    while True:
        #display menu options
        print("\nOptions:")
        print("1. Create Character")
        print("2. View Characters")
        print("3. Edit Characters")
        print("4. Exit")
        characters = load_characters()

        choice = input("Enter your choice: ")

        if choice == "1":
            #create a new character and save itto the file
            character = create_character()
            save_character(character)
        elif choice == "2":
            #load characters from the file and display them. with pandas. also display the character's attributes in a bar chart using matplotlib
            compare()
        elif choice == "3":
            #load characters from the file and allow the user to edit them. then save the changes to the file
            editcharacters(load_characters())
        elif choice == "4":
            break
        #idiot proofing
        else:
            print("Invalid choice. Please try again.")
menu()