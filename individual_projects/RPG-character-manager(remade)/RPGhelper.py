import json
import os
import random
from faker import Faker
import pandas as pd
import matplotlib.pyplot as plt

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CHAR_FILE = os.path.join(BASE_DIR, "characters.json")

fake = Faker()

def save_character(character, file_path=None):
    file_path = file_path or CHAR_FILE
    # Accept either object with attributes or raw dictionary
    if isinstance(character, dict):
        name = character.get("name")
        race = character.get("race")
        level = character.get("level")
        character_class = character.get("character_class")
        strength = character.get("strength")
        dexterity = character.get("dexterity")
        intelligence = character.get("intelligence")
        constitution = character.get("constitution")
        wisdom = character.get("wisdom")
        charisma = character.get("charisma")
    else:
        name = getattr(character, "name", None)
        race = getattr(character, "race", None)
        level = getattr(character, "level", None)
        character_class = getattr(character, "character_class", None)
        strength = getattr(character, "strength", None)
        dexterity = getattr(character, "dexterity", None)
        intelligence = getattr(character, "intelligence", None)
        constitution = getattr(character, "constitution", None)
        wisdom = getattr(character, "wisdom", None)
        charisma = getattr(character, "charisma", None)

    with open("characters.json", "r") as f:
        characters = json.load(f)

    if not isinstance(characters, list):
        characters = []

    characters = [c for c in characters if c.get("name") != name]
    characters.append({
        "name": name,
        "race": race,
        "level": level,
        "character_class": character_class,
        "strength": strength,
        "dexterity": dexterity,
        "intelligence": intelligence,
        "constitution": constitution,
        "wisdom": wisdom,
        "charisma": charisma,
    })
    with open("characters.json", "w") as f:
        json.dump(characters, f)


def create_character(name=None, race=None, level=None, character_class=None, strength=10, dexterity=10, intelligence=10, constitution=10, wisdom=10, charisma=10):
    class character:
        def __init__(self, name, race, level, character_class, strength=10, dexterity=10, intelligence=10, constitution=10, wisdom=10, charisma=10):
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

        def __str__(self):
            return f"{self.name} - Level {self.level} {self.character_class} ({self.race})\nSTR: {self.strength} DEX: {self.dexterity} INT: {self.intelligence} CON: {self.constitution} WIS: {self.wisdom} CHA: {self.charisma}"

    def create_random_character(name=None, race=None, level=None, character_class=None, strength=None, dexterity=None, intelligence=None, constitution=None, wisdom=None, charisma=None):
        name = name.strip() if isinstance(name, str) and name.strip() else fake.name()
        race = race.strip() if isinstance(race, str) and race.strip() else random.choice(["Human", "Elf", "Dwarf", "Halfling", "Gnome", "Half-Orc", "Tiefling", "Dragonborn"])
        level = int(level) if validate_input(level, "int") else random.randint(1, 20)
        character_class = character_class.strip() if isinstance(character_class, str) and character_class.strip() else random.choice(["fighter", "wizard", "rogue", "cleric", "ranger", "paladin", "sorcerer", "warlock", "bard", "druid", "monk", "barbarian"])

        def stat_or_random(value):
            return int(value) if validate_input(value, "int") else random.randint(7, 18)

        strength = stat_or_random(strength)
        dexterity = stat_or_random(dexterity)
        intelligence = stat_or_random(intelligence)
        constitution = stat_or_random(constitution)
        wisdom = stat_or_random(wisdom)
        charisma = stat_or_random(charisma)

        return character(name, race, level, character_class, strength, dexterity, intelligence, constitution, wisdom, charisma)

    print("welcome to the character creator!")
    print("would you like to manualy enter your charactrer's details or have them randomly generated?")
    choice = input("Enter 'manual' or 'random': ")

    if choice.lower() == 'manual':
        name = input("Enter your character's name: ") or name or fake.name()
        race = input("Enter your character's race: ") or race or "Human"
        level = input("Enter your character's level: ")
        level = int(level) if validate_input(level, 'int') else 1
        available_classes = ["fighter", "wizard", "rogue", "cleric", "ranger", "paladin", "sorcerer", "warlock", "bard", "druid", "monk", "barbarian"]
        character_class = input("Enter your character's class: ")
        while character_class not in available_classes:
            print("Invalid class. Please choose from the following:")
            for cls in available_classes:
                print(f"- {cls}")
            character_class = input("Enter your character's class: ")
        strength = int(input("Enter your character's strength: "))
        dexterity = int(input("Enter your character's dexterity: "))
        intelligence = int(input("Enter your character's intelligence: "))
        constitution = int(input("Enter your character's constitution: "))
        wisdom = int(input("Enter your character's wisdom: "))
        charisma = int(input("Enter your character's charisma: "))

        return character(name, race, level, character_class, strength, dexterity, intelligence, constitution, wisdom, charisma)

    if choice.lower() == 'random':
        print("enter any stat you would like to set for your character, or leave it blank to have it randomly generated")
        name = input("Enter your character's name: ")
        race = input("Enter your character's race: ")
        level = input("Enter your character's level: ")
        character_class = input("Enter your character's class: ")
        while character_class not in ["fighter", "wizard", "rogue", "cleric", "ranger", "paladin", "sorcerer", "warlock", "bard", "druid", "monk", "barbarian"]:
            character_class = input("Invalid class. Enter your character's class: ")
        strength = input("Enter your character's strength: ")
        dexterity = input("Enter your character's dexterity: ")
        intelligence = input("Enter your character's intelligence: ")
        constitution = input("Enter your character's constitution: ")
        wisdom = input("Enter your character's wisdom: ")
        charisma = input("Enter your character's charisma: ")

        return create_random_character(name, race, level, character_class, strength, dexterity, intelligence, constitution, wisdom, charisma)

    # fallback for invalid choice
    return character(name or fake.name(), race or "Human", level or 1, character_class or "fighter", strength, dexterity, intelligence, constitution, wisdom, charisma)

def load_characters(file_path=None):
    file_path = file_path or CHAR_FILE
    try:
        with open(file_path, "r") as f:
            raw = json.load(f)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}

    if isinstance(raw, dict):
        raw = list(raw.values())
    if not isinstance(raw, list):
        return {}

    return {c["name"]: normalize_char(c) for c in raw if "name" in c}
def save_character(character, file_path="characters.json"):
    try:
        with open(file_path, "r") as f:
            characters = json.load(f)
            if not isinstance(characters, list):
                characters = []
    except (FileNotFoundError, json.JSONDecodeError):
        characters = []

    # Support both object-like and dict-like character representations
    if isinstance(character, dict):
        if "raw" in character and isinstance(character["raw"], dict):
            char_data = character["raw"]
        else:
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
            "charisma": getattr(character, "charisma", None),
        }

    # protect against missing name
    if char_data.get("name") is None:
        return

    characters = [c for c in characters if c.get("name") != char_data.get("name")]
    characters.append({
        "name": char_data.get("name"),
        "race": char_data.get("race"),
        "level": char_data.get("level"),
        "character_class": char_data.get("character_class"),
        "strength": char_data.get("strength"),
        "dexterity": char_data.get("dexterity"),
        "intelligence": char_data.get("intelligence"),
        "constitution": char_data.get("constitution"),
        "wisdom": char_data.get("wisdom"),
        "charisma": char_data.get("charisma"),
    })
    with open(file_path, "w") as f:
        json.dump(characters, f, indent=2)
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
        "charisma": int(raw.get("charisma", 10)) if validate_input(raw.get("charisma", 10), "int") else 10,
    }
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
            [base["strength"], base["dexterity"], base["intelligence"], base["constitution"], base["wisdom"], base["charisma"], 10 + base["level"], 10 + base["level"]],
        ],
        "raw": base,
    }
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
    elif action == "remove":
        print("\nSkills:")
        for i in database[character_name]["skills"]:
            print(f"   - {i[0]}")
        skillToRemove = input("\nEnter the name of the skill you want to remove: ").capitalize().strip()
        skill_to_remove = next((skill for skill in database[character_name]["skills"] if skill[0] == skillToRemove), None)
        if skill_to_remove:
            database[character_name]["skills"].remove(skill_to_remove)
            print(f"\nSkill '{skillToRemove}' has been removed.")
        else:
            print(f"\nSkill '{skillToRemove}' not found in your skills.")


def inventory_management(database, character_name, player_class):
    Items_Dictionary = database[character_name].get("Items_Dictionary", {"Weapon": ["None"], "Armor": ["None"], "Inventory": []})
    print(f"\nCharacters Weapon: {Items_Dictionary['Weapon'][0]}")
    print(f"Character Wearing: {Items_Dictionary['Armor'][0]}")
    print("\nCharacter Inventory:")

    val = 0
    for x in Items_Dictionary["Inventory"]:
        val += 1
        if val == 1:
            print(x)
        if val == 3:
            val = 0

    Player_answer = input("\nWould you like to: \n1. Yes\n2. No\n\nWhich one would you like to choose (1 - 2)? ").strip().lower()
    if Player_answer in ("1", "yes"):
        asking = True
        while asking:
            players_selected_action = input("Would you like to (1.edit your inventory 2.Add a item to your inventory 3.To exit):").strip().lower()
            if players_selected_action == "1":
                answering = True
                while answering:
                    val = 0
                    for x in Items_Dictionary["Inventory"]:
                        val += 1
                        if val == 1:
                            print(x)
                        if val == 3:
                            val = 0
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
                            print(f"Your characters weapon is a {Items_Dictionary['Weapon'][0]}")
                            print(f"Your characters is wearing {Items_Dictionary['Armor'][0]}")
                            print("This is your inventory:")
                            val = 0
                            for x in Items_Dictionary["Inventory"]:
                                val += 1
                                if val == 1:
                                    print(f"- {x}")
                                if val == 3:
                                    val = 0
                            answering = False
                        else:
                            print(f"Your character class is incorrect. you need to be a {Item_class}, but you are a {player_class}")
                    else:
                        print("That is not an item in your inventory")
            elif players_selected_action == "2":
                player_item_name = input("What is the name of the item:").capitalize().strip()
                Items_Dictionary["Inventory"].append(player_item_name)
                player_item_slot = input("What is the slot of the item(1.Inventory,2.Weapon,3.Armor):").strip()
                if player_item_slot == "1":
                    player_item_slot = "Inventory"
                elif player_item_slot == "2":
                    player_item_slot = "Weapon"
                elif player_item_slot == "3":
                    player_item_slot = "Armor"
                Items_Dictionary["Inventory"].append(player_item_slot)
                player_item_class = input("What is the required class of the item(If no required one then type None):").capitalize().strip()
                if player_item_class not in ["None", "Warrior", "Fighter", "Rogue", "Cleric", "Sorcerer", "Mage", "Wizard", "Paladin", "Ranger", "Druid", "Bard", "Monk", "Barbarian"]:
                    print("That is not a valid class.")
                if player_item_class == "None":
                    player_item_class = "Any"
                Items_Dictionary["Inventory"].append(player_item_class)
                val = 0
                for x in Items_Dictionary["Inventory"]:
                    val += 1
                    if val == 1:
                        print(x)
                    if val == 3:
                        val = 0
            elif players_selected_action == "3":
                asking = False
            else:
                print("Invalid option.")


def editing(database, character_name):
    def displaystat(num, stat_name):
        oldstat = database[character_name]["attributes"][1][num]
        try:
            database[character_name]["attributes"][1][num] = int(newStatValue)
        except ValueError:
            database[character_name]["attributes"][1][num] = newStatValue
        print(f"\n{stat_name.capitalize()} has been updated from {oldstat} to {database[character_name]['attributes'][1][num]}")

    while True:
        changableStats = database[character_name]["attributes"][0]
        print("\nAttributes: ")
        for ii, x in enumerate(changableStats, 1):
            print(f"{ii}. {x.title()}")
        statToEdit = input("\nWhich attribute would you like to edit? ").lower().strip()
        stat_is_valid = statToEdit in changableStats or statToEdit in [s[:3] for s in changableStats] or statToEdit in ["ac", "hel"]
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
                "wisdom": "wisdom", "wis": "wisdom", "4": "wisdom",
                "constitution": "constitution", "con": "constitution", "5": "constitution",
                "charisma": "charisma", "cha": "charisma", "8": "charisma",
                "health": "health", "hel": "health", "6": "health",
                "armor class": "armor class", "ac": "armor class", "7": "armor class",
            }
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
            elif statToEdit in ["str", "dex", "int", "wis", "con", "cha", "hel", "ac"]:
                case_value = statToEdit

            match case_value:
                case "strength" | "str" | "1":
                    displaystat(0, "strength")
                case "dexterity" | "dex" | "2":
                    displaystat(1, "dexterity")
                case "intelligence" | "int" | "3":
                    displaystat(2, "intelligence")
                case "wisdom" | "wis" | "4":
                    displaystat(3, "wisdom")
                case "constitution" | "con" | "5":
                    displaystat(4, "constitution")
                case "charisma" | "cha" | "8":
                    displaystat(5, "charisma")
                case "health" | "hel" | "6":
                    displaystat(6, "health")
                case "armor class" | "ac" | "7":
                    displaystat(7, "armor class")
                case _:
                    print("Could not match stat. Please try again.")

            continue_editing = input("\nWould you like to update another attribute: \n- Yes\n- No\n\nWhich one would you like to choose? ").lower().strip()
            if continue_editing != "yes":
                break
        else:
            print("Invalid stat name. Please try again.")