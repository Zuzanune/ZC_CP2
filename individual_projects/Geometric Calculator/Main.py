"""introduce user
define menu function
    display library
    show actions list as 
    1: new shape
    2:view shapes
    3: compare shapes
    4:select shape
    5: sort shapes
    6: Help
    7: quit
    ask  user for choice
    if choice is 1
        call new shape function
    if choice is 2
        call view shapes function
    if choice is 3      
        call compare shapes function
    if choice is 4
        call select shape function
    if choice is 5
        call sort shapes function
    if choice is 6
        call help function
    if choice is 7
        exit program"""
from helper import *
def main():
    print("Welcome to the Geometric Calculator!")
    while True:
        print("\nMenu:")
        print("1: New Shape")
        print("2: View Shapes")
        print("3: Compare Shapes")
        print("4: Select Shape")
        print("5: Sort Shapes")
        print("6: Help")
        print("7: Quit")
        choice = input("Please enter your choice (1-7): ")
        if choice == '1':
            new_shape()
        elif choice == '2':
            view_shapes()
        elif choice == '3':
            compare_shapes()
        elif choice == '4':
            select_shape()
        elif choice == '5':
            sort_shapes()
        elif choice == '6':
            helps()
        elif choice == '7':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 7.")
main()