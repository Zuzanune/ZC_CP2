import json, random, faker, pandas, matplotlib
def save_character(character):
    with open("characters.json", "r") as f:
        characters = json.load(f)
    characters.append({
        "name": character.name,
        "race": character.race,
        "level": character.level,
        "character_class": character.character_class,
        "strength": character.strength,
        "dexterity": character.dexterity,
        "intelligence": character.intelligence,
        "constitution": character.constitution,
        "wisdom": character.wisdom,
        "charisma": character.charisma
    })
    with open("characters.json", "w") as f:
        json.dump(characters, f)

def create_character(name, race, level, character_class, strength=10, dexterity=10, intelligence=10, constitution=10, wisdom=10, charisma=10):
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
    def create_random_character(name = fake.name(), race = random.choice(["Human", "Elf", "Dwarf", "Halfling", "Gnome", "Half-Orc", "Tiefling", "Dragonborn"]), level = random.randint(1, 20), character_class = random.choice(["fighter", "wizard", "rogue", "cleric", "ranger", "paladin", "sorcerer", "warlock", "bard", "druid", "monk", "barbarian"]), strength = random.randint(7, 18), dexterity = random.randint(7, 18), intelligence = random.randint(7, 18), constitution = random.randint(7, 18), wisdom = random.randint(7, 18), charisma = random.randint(7, 18)):
        #name, race, level, character_class, strength, dexterity, intelligence, constitution, wisdom, charisma
        fake = faker.Faker()
        name = name
        race = race
        level = level
        character_class = character_class
        strength = strength
        dexterity = dexterity
        intelligence = intelligence
        constitution = constitution
        wisdom = wisdom
        charisma = charisma
        return character(name, race, level, character_class, strength, dexterity, intelligence, constitution, wisdom, charisma)
    print ("welcome to the character creator!")
    print ("would you like to manualy enter your charactrer's details or have them randomly generated?")
    choice = input("Enter 'manual' or 'random': ")
    if choice.lower() == 'manual':
        name = input("Enter your character's name: ")
        race = input("Enter your character's race: ")
        level = int(input("Enter your character's level: "))
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
    if choice.lower() == 'random':
        print ("enter any stat you would like to set for your character, or leave it blank to have it randomly generated")
        name = input("Enter your character's name: ")
        race = input("Enter your character's race: ")
        level = input("Enter your character's level: ")
        while input("Enter your character's class: ") not in ["fighter", "wizard", "rogue", "cleric", "ranger", "paladin", "sorcerer", "warlock", "bard", "druid", "monk", "barbarian"]:
            character_class = input("Enter your character's class: ")
        strength = input("Enter your character's strength: ")
        dexterity = input("Enter your character's dexterity: ")
        intelligence = input("Enter your character's intelligence: ")
        constitution = input("Enter your character's constitution: ")
        wisdom = input("Enter your character's wisdom: ")
        charisma = input("Enter your character's charisma: ")
        character = create_random_character(name, race, level, character_class, strength, dexterity, intelligence, constitution, wisdom, charisma)
        
    
    return character(name, race, level, character_class, strength, dexterity, intelligence, constitution, wisdom, charisma)
