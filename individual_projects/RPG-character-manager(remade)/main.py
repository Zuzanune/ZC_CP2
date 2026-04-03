from RPGhelper import create_character, load_characters, editcharacters, save_character
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
            characters = load_characters()
            for char in characters.values():
                display_char = char.get("raw", char) if isinstance(char, dict) else char
                name = display_char.get("name") if isinstance(display_char, dict) else None
                character_class = display_char.get("character_class") if isinstance(display_char, dict) else None
                level = display_char.get("level") if isinstance(display_char, dict) else None
                character_race = display_char.get("race") if isinstance(display_char, dict) else None
                print(f" \nName: {name} \n Class: {character_class} \n Race : {character_race} \n Level: {level}")

                items = char.get("Items_Dictionary", {"Weapon": ["None"], "Armor": ["None"], "Inventory": []}) if isinstance(char, dict) else None
                if items:
                    weapon = items.get("Weapon", ["None"])[0] if isinstance(items.get("Weapon", []), list) and items.get("Weapon") else "None"
                    armor = items.get("Armor", ["None"])[0] if isinstance(items.get("Armor", []), list) and items.get("Armor") else "None"
                    inventory_items = items.get("Inventory", [])
                    print(f" Weapon: {weapon} \n Armor: {armor}")
                    if inventory_items:
                        print(" Inventory:")
                        for i in range(0, len(inventory_items), 3):
                            item_name = inventory_items[i]
                            item_slot = inventory_items[i+1] if i+1 < len(inventory_items) else "no slot"
                            item_class = inventory_items[i+2] if i+2 < len(inventory_items) else "no class"
                            print(f"  - {item_name} ({item_slot}, {item_class})")
                    else:
                        print(" Inventory: None")

                attributes = char.get("attributes") if isinstance(char, dict) else None
                if attributes and isinstance(attributes, list) and len(attributes) >= 2:
                    df = pd.DataFrame([attributes[1]], columns=attributes[0])
                    print(df.T.rename(columns={0: "Value"}).to_string())
                    #display the attributes in a bar chart using matplotlib
                plt.figure(figsize=(10, 6))
                plt.bar(attributes[0], attributes[1], color='blue')
                plt.xlabel('Attributes')
                plt.ylabel('Values')
                plt.title(f"{name}'s Attributes")
                plt.ylim(0, max(attributes[1]) + 2)
                plt.show()

        elif choice == "3":
            #load characters from the file and allow the user to edit them. then save the changes to the file
            editcharacters(load_characters())
        elif choice == "4":
            break
        #idiot proofing
        else:
            print("Invalid choice. Please try again.")
menu()