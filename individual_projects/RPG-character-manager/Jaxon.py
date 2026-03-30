"""
Function for inventory_management(Chardata):
Display inventory
Receive players input if they want to edit it
Yes:
	Get item player wants to edit
	Check if they can use that item(By using the information the item has)
	If they can swap out item if not then repeat until they chose to leave or  it works
	Ask if they want to edit more if not return inventory and exit
No:
	Exit the function


"""


#Example dictonary Items_Dictonaties = {"Weapon":[#item name,#Slot type.#class required,#Weight,],"Armor":[],"Inventory":{} }
Items_Dictonaties = {"Weapon":["Sword","Weapon","none"],"Armor":["Iron Armor","Armor","none"],"Inventory":["Daggers","Weapon","Rouge","Staff","Weapon","None"]}

def inventory_management(Items_Dictonaties,player_class):
    print(f"Your characters weapon is a {Items_Dictonaties["Weapon"][0]}")
    print(f"Your character is wearing {Items_Dictonaties["Armor"][0]} ")
    print(f"This is your inventory:")
    val = 0
    for x in Items_Dictonaties["Inventory"]:
        val += 1
        if val == 1:
            print(x)
        if val == 3:
            val = 0
    Player_answer = input("Would you like to Edit your inventory (1.Yes 2.No):").capitalize().strip()
    if Player_answer == "1" or Player_answer == "Yes":
        asking = True
        while asking:
            players_selected_action = input("Would you like to (1.edit your inevntory 2.Add a item to your inventory 3.To exit):").capitalize().strip()
            if players_selected_action == "1":
                answering = True
                while answering:
                    for x in Items_Dictonaties["Inventory"]:
                        val += 1
                        if val == 1:
                            print(x)
                        if val == 3:
                            val = 0
                    Edit_item = input("What item in your inventory do you want to edit:").capitalize().strip()
                    if Edit_item in Items_Dictonaties["Inventory"]:
                        Item_index = Items_Dictonaties["Inventory"].index(Edit_item)
                        Item_slot = Items_Dictonaties["Inventory"][Item_index + 1]
                        Item_class = Items_Dictonaties["Inventory"][Item_index + 2]
                        if Item_class == player_class or Item_class == "None":
                            for x in range(0,3):
                                    Items_Dictonaties["Inventory"].pop(Item_index) 
                            for x in range(0,3):
                                if Items_Dictonaties[Item_slot][0] != "None":
                                    Items_Dictonaties["Inventory"].append(Items_Dictonaties[Item_slot][x]) 
                            Items_Dictonaties[Item_slot] = [Edit_item,Item_slot,Item_class]
                            print(f"Your charaters weapon is a {Items_Dictonaties["Weapon"][0]}")
                            print(f"Your characters is wearing {Items_Dictonaties["Armor"][0]} ")
                            print(f"This is your inventory:")
                            val = 0
                            for x in Items_Dictonaties["Inventory"]:
                                val += 1
                                if val == 1:
                                    print(x)
                                if val == 3:
                                    val = 0
                            answering = False
                        else:
                            print(f"Your charater class is incorect you need to be a {Item_class} you are a {player_class}")
                    else:
                        print("that is not an item in your inventory")
            if players_selected_action == "2":
                player_item_name = input("What is the name of the item:").capitalize().strip()
                Items_Dictonaties["Inventory"].append(player_item_name)
                player_item_slot = input("What is the slot of the item(Inventory,Weapon,Armor):").capitalize().strip()
                Items_Dictonaties["Inventory"].append(player_item_slot)
                player_item_class = input("What is the required class of the item(If no required one then type any):").capitalize().strip()
                for x in Items_Dictonaties["Inventory"]:
                        val += 1
                        if val == 1:
                            print(x)
                        if val == 3:
                            val = 0
            if players_selected_action == "3":
                asking = False
            

                    
                
                


        



inventory_management(Items_Dictonaties,"None")