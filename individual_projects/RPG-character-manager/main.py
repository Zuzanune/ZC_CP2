from Editing_function import *
import random
from franco import mainmenu
from arsh import intro
prequisites_database = {}
#The Database NEEDS to remain this way, otherwise the functions will not work correctly.
database = {
    "Zarkon":{"simpleinfo":("Dragonborn", "Fighter"), "level": 8, "Items_Dictionary": {"Weapon": ["Shortsword", "Weapon", "any"], "Armor": ["any", "Armor", "any"], "Inventory": []}, "skills":{("Fireball","A bright streak flashes from the caster to a point within 150 feet, erupting into a 20-foot-radius sphere of fire!")}, "attributes": [["strength", "dexterity", "intelligence", "wisdom", "constitution", "health", "armor class", "charisma"], [random.randint(8, 18), random.randint(8, 18), random.randint(8, 18), random.randint(8, 18), random.randint(8, 18), random.randint(8, 15), random.randint(10, 17), random.randint(8, 18)]]},

    "Gulnum":{"simpleinfo":("Gnome", "Sorcerer"), "level": 4, "Items_Dictionary": {"Weapon": ["Mace", "Weapon", "None"], "Armor": ["None", "Armor", "None"], "Inventory": []}, "skills":{("Magic missile","A missile of magical force springs from the caster's finger to strike a target within 120 feet")}, "attributes": [["strength", "dexterity", "intelligence", "wisdom", "constitution", "health", "armor class", "charisma"], [random.randint(8, 18), random.randint(8, 18), random.randint(8, 18), random.randint(8, 18), random.randint(8, 18), random.randint(8, 15), random.randint(10, 17), random.randint(8, 18)]]},

    "Zylvina":{"simpleinfo":("Elf", "Cleric"), "level": 13,"Items_Dictionary": {"Weapon": ["Whip", "Weapon", "None"], "Armor": ["None", "Armor", "None"], "Inventory": []}, "skills":{("Heal","The character can heal wounds and restore health")}, "attributes": [["strength", "dexterity", "intelligence", "wisdom", "constitution", "health", "armor class", "charisma"], [random.randint(8, 18), random.randint(8, 18), random.randint(8, 18), random.randint(8, 18), random.randint(8, 18), random.randint(8, 15), random.randint(10, 17), random.randint(8, 18)]]},

    #"test":{"simpleinfo":("Human", "Rogue"), "level": 1, "Items_Dictionary": {"Weapon": ["Dagger", "Weapon", "None"], "Armor": ["None", "Armor", "None"], "Inventory": []}, "skills":{("punch","The character can punch an enemy for damage")}, "attributes": [["strength", "dexterity", "intelligence", "wisdom", "constitution", "health", "armor class", "charisma"], [10, 10, 10, 10, 10, 10, 10, 10]]}}
}
if __name__ == "__main__":
    intro()
    mainmenu(database)