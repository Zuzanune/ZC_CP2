import json
import os
import random
from faker import Faker
import pandas as pd
import matplotlib.pyplot as plt

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CHAR_FILE = os.path.join(BASE_DIR, "characters.json")

fake = Faker()

class character:
    def __init__(self, name, race, level, character_class, strength=10, dexterity=10, intelligence=10, constitution=10, wisdom=10, charisma=10, hp=10, ac=10, skills=[], inventory=[]):
        self.name = name
        self.race = race
        self.level = level
        self.character_class = character_class
        self.strength = strength
        self.dexterity = dexterity
        self.intelligence = intelligence
        self.constitution = constitution
        self.wisdom = wisdom
        self.charisma = charisma
        self.skills = skills
        self.hp = hp
        self.ac = ac

    def __str__(self):
        return f"{self.name} - Level {self.level} {self.character_class} ({self.race})\nSTR: {self.strength} DEX: {self.dexterity} INT: {self.intelligence} CON: {self.constitution} WIS: {self.wisdom} CHA: {self.charisma}"

def create_character(name=None, race=None, level=None, character_class=None, strength=10, dexterity=10, intelligence=10, constitution=10, wisdom=10, charisma=10):
    print("welcome to the character creator!")
    print("would you like to manualy enter your charactrer's details or have them randomly generated?")
    available_races = ["Human", "Elf", "Dwarf", "Halfling", "Gnome", "Half-Orc", "Tiefling", "Dragonborn"]
    while True:
        choice = input("Enter 'manual' or 'random': ")

        if choice.lower() == 'manual':
            name = input("Enter your character's name: ") or name or fake.name()
            while True:
                race = input("Enter your character's race: ").capitalize() or race or "Human"
                if race not in available_races:
                    print("Invalid race. Please choose from the following:")
                    for r in available_races:
                        print(f"- {r}")
                        continue
                break
            level = input("Enter your character's level: ")
            level = int(level) if validate_input(level, 'int') else 1
            available_classes = ["fighter", "wizard", "rogue", "cleric", "ranger", "paladin", "sorcerer", "warlock", "bard", "druid", "monk", "barbarian", "artificer"]
            character_class = input("Enter your character's class: ").lower()
            while character_class not in available_classes:
                print("Invalid class. Please choose from the following:")
                for cls in available_classes:
                    print(f"- {cls}")
                character_class = input("Enter your character's class: ")
            while True:
                str_input = input("Enter your character's strength: ")
                if validate_input(str_input, 'int'):
                    strength = int(str_input)
                    break
                print("Invalid input for strength. Please enter a number.")
            while True:
                str_input = input("Enter your character's dexterity: ")
                if validate_input(str_input, 'int'):
                    dexterity = int(str_input)
                    break
                print("Invalid input for dexterity. Please enter a number.")
            while True:
                str_input = input("Enter your character's intelligence: ")
                if validate_input(str_input, 'int'):
                    intelligence = int(str_input)
                    break
                print("Invalid input for intelligence. Please enter a number.")
            while True:
                str_input = input("Enter your character's constitution: ")
                if validate_input(str_input, 'int'):
                    constitution = int(str_input)
                    break
                print("Invalid input for constitution. Please enter a number.")
            while True:
                str_input = input("Enter your character's wisdom: ")
                if validate_input(str_input, 'int'):
                    wisdom = int(str_input)
                    break
                print("Invalid input for wisdom. Please enter a number.")
            while True:
                str_input = input("Enter your character's charisma: ")
                if validate_input(str_input, 'int'):
                    charisma = int(str_input)
                    break
                print("Invalid input for charisma. Please enter a number.")

            return character(name, race, level, character_class, strength, dexterity, intelligence, constitution, wisdom, charisma)

        if choice.lower() == 'random':
            print("enter any stat you would like to set for your character, or leave it blank to have it randomly generated")
            name = input("Enter your character's name: ")
            race = input("Enter your character's race: ")
            while True:
                level = input("Enter your character's level: ")
                if not validate_input(level, 'int') and level.strip() != "":
                    print("Invalid input for level. Please enter a number.")
                    continue
                level = int(level) if validate_input(level, 'int') else random.randint(1, 20)
                if level > 20:
                    print("Level cannot be greater than 20.")
                    continue
                break
            character_class = input("Enter your character's class: ")
            while character_class not in ["fighter", "wizard", "rogue", "cleric", "ranger", "paladin", "sorcerer", "warlock", "bard", "druid", "monk", "barbarian", ""]:
                character_class = input("Invalid class. Enter your character's class: ")
            strength = input("Enter your character's strength: ")
            dexterity = input("Enter your character's dexterity: ")
            intelligence = input("Enter your character's intelligence: ")
            constitution = input("Enter your character's constitution: ")
            wisdom = input("Enter your character's wisdom: ")
            charisma = input("Enter your character's charisma: ")

            name = name.strip() if isinstance(name, str) and name.strip() else fake.name()
            race = race.strip() if isinstance(race, str) and race.strip() else random.choice(["Human", "Elf", "Dwarf", "Halfling", "Gnome", "Half-Orc", "Tiefling", "Dragonborn"])
            level = int(level) if validate_input(level, "int") else random.randint(1, 20)
            character_class = character_class.strip() if isinstance(character_class, str) and character_class.strip() else random.choice(["fighter", "wizard", "rogue", "cleric", "ranger", "paladin", "sorcerer", "warlock", "bard", "druid", "monk", "barbarian", "Artificer"])

            def statrandom(value):
                return int(value) if validate_input(value, "int") else random.randint(7, 18)

            strength = statrandom(strength)
            dexterity = statrandom(dexterity)
            intelligence = statrandom(intelligence)
            constitution = statrandom(constitution)
            wisdom = statrandom(wisdom)
            charisma = statrandom(charisma)

            return character(name, race, level, character_class, strength, dexterity, intelligence, constitution, wisdom, charisma)
        else:
            print ("invalid choice. please enter manual or random")
    file_path = file_path or CHAR_FILE
    try:
        with open(file_path, "r") as file:
            raw = json.load(file)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}

    if isinstance(raw, dict):
        raw = list(raw.values())
    if not isinstance(raw, list):
        return {}
    return {c["name"]: normalize_char(c) for c in raw if "name" in c}
def save_character(character, file_path= CHAR_FILE):
    try:
        with open(file_path, "r") as f:
            characters = json.load(f)
            if not isinstance(characters, list):
                characters = []
    except (FileNotFoundError, json.JSONDecodeError):
        characters = []

    if isinstance(character, dict):
        char_data = character
    else:
        char_data = {
            "name": getattr(character, "name", None),
            "race": getattr(character, "race", None),
            "level": getattr(character, "level", None),
            "character_class": getattr(character, "character_class", None),
            "strength": getattr(character, "strength", None),
            "dexterity": getattr(character, "dexterity", None),
            "intelligence": getattr(character, "intelligence", None),
            "constitution": getattr(character, "constitution", None),
            "wisdom": getattr(character, "wisdom", None),
            "charisma": getattr(character, "charisma", None),}
    if char_data.get("name") is None:
        return

    characters = [c for c in characters if c.get("name") != char_data.get("name")]
    characters.append(char_data)
    def make_json_serializable(obj):
        if isinstance(obj, dict):
            return {k: make_json_serializable(v) for k, v in obj.items()}
        elif isinstance(obj, (list, tuple)):
            return [make_json_serializable(item) for item in obj]
        elif isinstance(obj, set):
            return list(obj)
        else:
            return obj
    serializable_characters = make_json_serializable(characters)
    with open(file_path, "w") as f:
        json.dump(serializable_characters, f, indent=2)

def load_characters(file_path=None):
    file_path = file_path or CHAR_FILE
    try:
        with open(file_path, "r") as file:
            raw = json.load(file)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}

    if isinstance(raw, dict):
        raw = list(raw.values())
    if not isinstance(raw, list):
        return {}
    return {c["name"]: normalize_char(c) for c in raw if "name" in c}

def normalize_char(raw):
    base = {
        "name": raw.get("name", "Unknown"),
        "race": raw.get("race", "Unknown"),
        "level": int(raw.get("level", 1)) if validate_input(raw.get("level", 1), "int") else 1,
        "character_class": raw.get("character_class", "fighter"),
        "strength": int(raw.get("strength", 10)) if validate_input(raw.get("strength", 10), "int") else 10,
        "dexterity": int(raw.get("dexterity", 10)) if validate_input(raw.get("dexterity", 10), "int") else 10,
        "intelligence": int(raw.get("intelligence", 10)) if validate_input(raw.get("intelligence", 10), "int") else 10,
        "constitution": int(raw.get("constitution", 10)) if validate_input(raw.get("constitution", 10), "int") else 10,
        "wisdom": int(raw.get("wisdom", 10)) if validate_input(raw.get("wisdom", 10), "int") else 10,
        "charisma": int(raw.get("charisma", 10)) if validate_input(raw.get("charisma", 10), "int") else 10,}
    dex_mod = modifier(base["dexterity"])
    con_mod = modifier(base["constitution"])
    health = 10 + con_mod + (base["level"] - 1) * (6 + con_mod)
    armor_class = 10 + dex_mod
    return {
        "name": base["name"],
        "race": base["race"],
        "level": base["level"],
        "character_class": base["character_class"],
        "strength": base["strength"],
        "dexterity": base["dexterity"],
        "intelligence": base["intelligence"],
        "constitution": base["constitution"],
        "wisdom": base["wisdom"],
        "charisma": base["charisma"],
        "simpleinfo": [base["name"], base["character_class"]],
        "skills": set(tuple(x) for x in raw.get("skills", [])) if isinstance(raw.get("skills", []), list) else set(),
        "Items_Dictionary": raw.get("Items_Dictionary", {"Weapon": ["None"], "Armor": ["None"], "Inventory": []}),
        "attributes": [
            ["strength", "dexterity", "intelligence", "constitution", "wisdom", "charisma", "health", "armor class"],
            [base["strength"], base["dexterity"], base["intelligence"], base["constitution"], base["wisdom"], base["charisma"], health, armor_class],],
        "raw": base}
def validate_input(text, kind='int'):
    test_to_check = str(text).strip()
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

def modifier(score):
    return (score - 10) // 2
def editcharacters(database):
    print("\nWhich character would you like to edit? ")
    count = 0
    for i, character in enumerate(database.keys()):
        count += 1
        print(f"{i+1}. {character}")
    choice = input("\nEnter the number of the character you want to edit, or type q to return to the main menu: ").strip()
    if choice.lower() == 'q':
        return
    if not validate_input(choice, 'int'):
        print("Please enter a number.")
        return
    choice = int(choice)
    if choice < 1 or choice > count:
        print("Invalid choice.")
        return
    character_name = list(database.keys())[choice - 1]

    while True:
        print(f"\nEditing {character_name}")
        print("1. Edit Skills")
        print("2. Edit Inventory")
        print("3. Edit Stats")
        print("4. Return to Main Menu")
        action = input("\nChoose an option: ").strip()
        if action == "1":
            EditSkills(database, character_name)
        elif action == "2":
            inventory_management(database, character_name, database[character_name]["simpleinfo"][1])
        elif action == "3":
            editing(database, character_name)
        elif action == "4":
            break
        else:
            print("Invalid option.")


def EditSkills(database, character_name):
    action = input("\nWould you like to: \n- Add\n- Remove\n\nWhich one would you like to choose? ").lower().strip()
    if action == "add":
        skillname = input("\nEnter the name of the skill you want to add: ").capitalize().strip()
        skilldesc = input("Enter a description for the skill: ").strip()
        database[character_name]["skills"].add((skillname, skilldesc))
        print(f"Skill '{skillname}' has been added.")
        save_character(database[character_name])
    elif action == "remove":
        print("\nSkills:")
        for i in database[character_name]["skills"]:
            print(f"   - {i[0]}")
        skillToRemove = input("\nEnter the name of the skill you want to remove: ").capitalize().strip()
        skill_to_remove = next((skill for skill in database[character_name]["skills"] if skill[0] == skillToRemove), None)
        if skill_to_remove:
            database[character_name]["skills"].remove(skill_to_remove)
            print(f"\nSkill '{skillToRemove}' has been removed.")
            save_character(database[character_name])
        else:
            print(f"\nSkill '{skillToRemove}' not found in your skills.")


def inventory_management(database, character_name, player_class):
    Items_Dictionary = database[character_name].get("Items_Dictionary", {"Weapon": ["None"], "Armor": ["None"], "Inventory": []})
    print(f"\nCharacters Weapon: {Items_Dictionary['Weapon'][0]}")
    print(f"Character Wearing: {Items_Dictionary['Armor'][0]}")
    print("\nCharacter Inventory:")
    for i in range(0, len(Items_Dictionary["Inventory"]), 3):
        item_name = Items_Dictionary["Inventory"][i]
        item_slot = Items_Dictionary["Inventory"][i+1] if i+1 < len(Items_Dictionary["Inventory"]) else "Unknown"
        item_class = Items_Dictionary["Inventory"][i+2] if i+2 < len(Items_Dictionary["Inventory"]) else "Unknown"
        print(f"- {item_name} ({item_slot}, {item_class})")

    Player_answer = input("\nWould you like to: \n1. Yes\n2. No\n\nWhich one would you like to choose (1 - 2)? ").strip().lower()
    if Player_answer in ("1", "yes"):
        asking = True
        while asking:
            players_selected_action = input("Would you like to (1.edit your inventory 2.Add a item to your inventory 3.To exit):").strip().lower()
            if players_selected_action == "1":
                answering = True
                while answering:
                    print("Current Inventory:")
                    for i in range(0, len(Items_Dictionary["Inventory"]), 3):
                        item_name = Items_Dictionary["Inventory"][i]
                        item_slot = Items_Dictionary["Inventory"][i+1] if i+1 < len(Items_Dictionary["Inventory"]) else "Unknown"
                        item_class = Items_Dictionary["Inventory"][i+2] if i+2 < len(Items_Dictionary["Inventory"]) else "Unknown"
                        print(f"- {item_name} ({item_slot}, {item_class})")
                    Edit_item = input("What item in your inventory do you want to edit:").capitalize().strip()
                    if Edit_item in Items_Dictionary["Inventory"]:
                        Item_index = Items_Dictionary["Inventory"].index(Edit_item)
                        Item_slot = Items_Dictionary["Inventory"][Item_index + 1]
                        Item_class = Items_Dictionary["Inventory"][Item_index + 2]
                        if Item_class == player_class or Item_class == "Any":
                            for _ in range(3):
                                Items_Dictionary["Inventory"].pop(Item_index)
                            if Item_slot in Items_Dictionary and Items_Dictionary[Item_slot][0] != "None":
                                for x in Items_Dictionary[Item_slot]:
                                    Items_Dictionary["Inventory"].append(x)
                            Items_Dictionary[Item_slot] = [Edit_item, Item_slot, Item_class]
                            print(f"Your character's weapon is a {Items_Dictionary['Weapon'][0]}")
                            print(f"Your character is wearing {Items_Dictionary['Armor'][0]}")
                            print("This is your inventory:")
                            for i in range(0, len(Items_Dictionary["Inventory"]), 3):
                                item_name = Items_Dictionary["Inventory"][i]
                                item_slot = Items_Dictionary["Inventory"][i+1] if i+1 < len(Items_Dictionary["Inventory"]) else "Unknown"
                                item_class = Items_Dictionary["Inventory"][i+2] if i+2 < len(Items_Dictionary["Inventory"]) else "Unknown"
                                print(f"- {item_name} ({item_slot}, {item_class})")
                            answering = False
                        else:
                            print(f"Your character class is incorrect. you need to be a {Item_class}, but you are a {player_class}")
                    else:
                        print("That is not an item in your inventory")
            elif players_selected_action == "2":
                player_item_name = input("What is the name of the item:").capitalize().strip()
                Items_Dictionary["Inventory"].append(player_item_name)
                while True:
                    player_item_slot = input("What is the slot of the item(1.Inventory,2.Weapon,3.Armor):").strip()
                    if player_item_slot == "1":
                        player_item_slot = "Inventory"
                        break
                    elif player_item_slot == "2":
                        player_item_slot = "Weapon"
                        break
                    elif player_item_slot == "3":
                        player_item_slot = "Armor"
                        break
                    else:
                        print("Invalid slot. Please enter 1, 2, or 3.")
                Items_Dictionary["Inventory"].append(player_item_slot)
                player_item_class = "None"
                if player_item_class not in ["None", "Warrior", "Fighter", "Rogue", "Cleric", "Sorcerer", "Mage", "Wizard", "Paladin", "Ranger", "Druid", "Bard", "Monk", "Barbarian"]:
                    print("That is not a valid class.")
                if player_item_class == "None":
                    player_item_class = "Any"
                Items_Dictionary["Inventory"].append(player_item_class)
                print("Updated Inventory:")
                for i in range(0, len(Items_Dictionary["Inventory"]), 3):
                    item_name = Items_Dictionary["Inventory"][i]
                    item_slot = Items_Dictionary["Inventory"][i+1] if i+1 < len(Items_Dictionary["Inventory"]) else "Unknown"
                    item_class = Items_Dictionary["Inventory"][i+2] if i+2 < len(Items_Dictionary["Inventory"]) else "Unknown"
                    print(f"- {item_name} ({item_slot}, {item_class})")
            elif players_selected_action == "3":
                asking = False
                save_character(database[character_name])
            else:
                print("Invalid option.")


def editing(database, character_name):
    def displaystat(num, stat_name):
        oldstat = database[character_name]["attributes"][1][num]
        new_val = int(newStatValue)
        database[character_name]["attributes"][1][num] = new_val
        database[character_name]["raw"][stat_name] = new_val
        print(f"\n{stat_name.capitalize()} has been updated from {oldstat} to {new_val}")

    while True:
        changableStats = [stat for stat in database[character_name]["attributes"][0] if stat not in ["health", "armor class"]]
        print("\nAttributes: ")
        for ii, x in enumerate(changableStats, 1):
            print(f"{ii}. {x.title()}")
        statToEdit = input("\nWhich attribute would you like to edit? ").lower().strip()
        stat_is_valid = statToEdit in changableStats or statToEdit in [s[:3] for s in changableStats]
        try:
            stat_num = int(statToEdit)
            stat_is_valid = stat_is_valid or (1 <= stat_num <= len(changableStats))
        except ValueError:
            pass

        if stat_is_valid:
            stat_name_map = {
                "strength": "strength", "str": "strength", "1": "strength",
                "dexterity": "dexterity", "dex": "dexterity", "2": "dexterity",
                "intelligence": "intelligence", "int": "intelligence", "3": "intelligence",
                "wisdom": "wisdom", "wis": "wisdom", "5": "wisdom",
                "constitution": "constitution", "con": "constitution", "4": "constitution",
                "charisma": "charisma", "cha": "charisma", "6": "charisma",}
            actual_stat_name = stat_name_map.get(statToEdit, statToEdit)
            while True:
                newStatValue = input(f"What would you like to change {actual_stat_name} to? ").strip()
                if not validate_input(newStatValue, 'int'):
                    print("Please enter a numeric value.")
                    continue
                break

            case_value = statToEdit
            if statToEdit.isdigit():
                case_value = statToEdit
            elif statToEdit in ["str", "dex", "int", "wis", "con", "cha"]:
                case_value = statToEdit

            match case_value:
                case "strength" | "str" | "1":
                    displaystat(0, "strength")
                case "dexterity" | "dex" | "2":
                    displaystat(1, "dexterity")
                    dex_mod = modifier(database[character_name]["attributes"][1][1])
                    database[character_name]["attributes"][1][7] = 10 + dex_mod  # armor class
                    print(f"Armor Class updated to {database[character_name]['attributes'][1][7]}")
                case "intelligence" | "int" | "3":
                    displaystat(2, "intelligence")
                case "constitution" | "con" | "4":
                    displaystat(3, "constitution")
                    con_mod = modifier(database[character_name]["attributes"][1][3])
                    level = database[character_name]["raw"]["level"]
                    database[character_name]["attributes"][1][6] = 10 + con_mod + (level - 1) * (6 + con_mod)
                    print(f"Health updated to {database[character_name]['attributes'][1][6]}")
                case "wisdom" | "wis" | "5":
                    displaystat(4, "wisdom")
                case "charisma" | "cha" | "6":
                    displaystat(5, "charisma")
                case _:
                    print("Could not match stat. Please try again.")

            continue_editing = input("\nWould you like to update another attribute: \n- Yes\n- No\n\nWhich one would you like to choose? ").lower().strip()
            if continue_editing != "yes":
                newstatlist = database[character_name]["attributes"][1]
                save_character(database[character_name])
                break
        else:
            print("Invalid stat name. Please try again.")