def validate_input(text, kind='int'):
    test_to_check = str(text).strip().capitalize()
    if kind == 'int':
        try:
            int(test_to_check)
            return True
        except ValueError:
            return False
    elif kind == 'float':
        try:
            float(test_to_check)
            return True
        except ValueError:
            return False
    elif kind == 'alpha':
        return test_to_check.isalpha()
    else:
        return False


"""Def budget():
While True:
	Introduce user to budgets and goals if first time
	Get all information from json and save it in dictionary
	Display menu as “1. Goals
			     2. Budget Categories
			     4. Quit”
	User picks option
	If goals:
		If goals section of dictionary is empty:
		Introduce user to saving goals and how to create them
		Have user create saving goal
		Else:
			Display goals and percent complete
			Give user options to add to goal, edit goal, and quit
			If add to goal:
				Select goal
				Ask user how much is being added
				Add that much
				Display new goal percentage. If >100, remove goal
			If edit:
				Select goal
				Display all goal information
				User can edit all information
			If quit
				Continue to start of loop
	If budget
		If budget section is empty
		Introduce users to budgets and how to create them
		User creates budget category
			Else:
				Display all budgets and money remaining
				Give user options to add to category,remove from category,  edit category, and quit
				If add:
					Select category
					Ask user how much is being added
					Add to category
				If edit:
					Select category
					Display all stats
					User can edit all information
				If quit:
					Continue to start of loop
		If quit:
			Return from function
		
		
			
	
"""

def budget(dict):
    while True:
        print("Welcome to the budget keeper!")
        print("1. Goals")
        print("2. Budget Categories")
        print("3. Quit")
        choice = input("Please select an option: ")
        if choice == '1':
            if dict[goals] == {}:
                print("Welcome to the goals section! Here you can create saving goals and track your progress towards them.")
                # Code to create a new goal
            else:
                print("Here are your current goals and their progress:")
                # Code to display goals and their progress
                print("Options:")
                print("1. Add to goal")
                print("2. Edit goal")
                print("3. Quit")
                goal_choice = input("Please select an option: ")
                if goal_choice == '1':
                    # Code to add to a goal
                    count = 1
                    for x in dict[goals]:
                        print(f"{count}. {x}")
                        count += 1
                    print ("Select a goal to add to:")
                    goal_selection = input("Enter the number of the goal: ")
                    
                    pass
                elif goal_choice == '2':
                    # Code to edit a goal
                    pass
                elif goal_choice == '3':
                    continue
                else:
                    print("Invalid option, please try again.")
        elif choice == '2':
            print("Budget Categories section coming soon!")
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid option, please try again.")