from RPGhelper import create_character, load_characters, editcharacters, save_character
import pandas as pd
print ("Welcome to the RPG Character Manager! \n here you can create and manage your RPG characters! \n compatable with Dungeons and Dragons 5th edition! \n")

while True:
    print("\nOptions:")
    print("1. Create Character")
    print("2. Load Characters")
    print("3. Edit Characters")
    print("4. Exit")
    characters = load_characters()

    choice = input("Enter your choice: ")

    if choice == "1":
        character = create_character()
        save_character(character)
    elif choice == "2":
        characters = load_characters()
        for char in characters.values():
            display_char = char.get("raw", char) if isinstance(char, dict) else char
            name = display_char.get("name") if isinstance(display_char, dict) else None
            character_class = display_char.get("character_class") if isinstance(display_char, dict) else None
            level = display_char.get("level") if isinstance(display_char, dict) else None
            character_race = display_char.get("race") if isinstance(display_char, dict) else None
            print(f" \nName: {name} \n Class: {character_class} \n Race : {character_race} \n Level: {level}")
            

            attributes = char.get("attributes") if isinstance(char, dict) else None
            if attributes and isinstance(attributes, list) and len(attributes) >= 2:
                df = pd.DataFrame([attributes[1]], columns=attributes[0])
                print(df.T.rename(columns={0: "Value"}).to_string())

    elif choice == "3":
        editcharacters(load_characters())
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please try again.")
        