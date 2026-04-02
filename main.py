### MAIN FILE ###
# This is the main file for the Pokemon/RPG game. It will contain the main game loop and handle user input.
# The rough idea is to have a text-based interface where the player can choose to explore, fight enemies, manage their inventory, and complete quests.
# The game will be structured around a main loop that continues until the player chooses to exit or their character dies.
# The main loop will present the player with a menu of options, such as "Explore", "Fight", "Inventory", "Quests", and "Exit".
# Each option will lead to a different part of the game, where the player can interact with the world, fight enemies, manage their inventory, and complete quests.
# The game will also include a leveling system, where the player gains experience points from defeating enemies and completing quests. As the player levels up, they will gain access to new abilities, equipment, and areas to explore.

## Importing necessary modules and data
import playerdata
import enemies
import loot
import locations
import characters
import json
import os
import random
import math
import quests
import dialogue
from datetime import datetime

## Variables

location = None  # This variable will keep track of the player's current location in the game world. It will be updated as the player explores and moves between different areas.

# Create a location registry for easy lookup by name
location_registry = {
    "village": locations.greenwood_village,
    "tavern": locations.tavern,
    "blacksmith": locations.blacksmith,
    "general_store": locations.general_store,
    "tavern_basement": locations.tavern_basement,
    "royal_palace": locations.royal_palace
}

## Functions
# The main functions in this file will include:
def start_menu():
    # This function will present the player with the option to start a new game, load a saved game, or exit the game.
    print("Welcome to the Pokemon/RPG game!")
    print("1. Start New Game")
    print("2. Load Game")
    print("0. Exit")
    choice = input("> ")
    if choice == "1":
        new_game()
    elif choice == "2":
        load_game()
    elif choice == "0":
        print("Thanks for playing! Goodbye!")
        exit()
    else:
        print("Invalid choice. Please try again.")
        start_menu()

def new_game():
    # This function will start a new game, initializing the player's data and inventory, and presenting the main menu.
    print("Welcome to the Pokemon/RPG game!")
    print("Please enter your character's name:")
    player_name = input("> ")
    playerdata.player_data["name"] = player_name
    print(f"Hello, {player_name}! Your adventure begins now.")
    global location
    location = locations.greenwood_village  # Start the player in the village
    main_menu()

def save_game():
    # This function will save the player's progress, allowing them to continue from where they left off at a later time. This will involve writing the player's data and inventory to a file, so that it can be loaded when the player chooses to continue their game.
    try:
        # Create saves directory if needed
        if not os.path.exists("saves"):
            os.makedirs("saves")

        # Prepare data to save
        save_data = {
            "metadata": {
                "save_time": datetime.now().isoformat(),
                "version": "1.0",
                "character_name": playerdata.player_data["name"],
                "level": playerdata.player_data["level"],
                "location": location.name if location else None
            },
            "player_data": playerdata.player_data,
            "inventory": playerdata.inventory
        }

        # Write save data to file
        save_filename = f"saves/{playerdata.player_data['name']}_save.json"
        with open(save_filename, "w") as save_file:
            json.dump(save_data, save_file, indent=4)
        print(f"Game saved successfully as {save_filename}!")

    except IOError as e:
        print(f"An error occurred while saving the game: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def load_game():
    # This function will load a saved game
    try:
        # Check if saves directory exists
        if not os.path.exists("saves"):
            print("No saved games found.")
            start_menu()
            return

        # List available save files
        save_files = [f for f in os.listdir("saves") if f.endswith(".json")]
        
        if not save_files:
            print("No saved games found.")
            start_menu()
            return

        print("\nAvailable saves:")
        for i, save_file in enumerate(save_files, 1):
            print(f"{i}. {save_file}")
        
        # Let player choose which save to load
        choice = input("> ")
        
        if not choice.isdigit() or int(choice) < 1 or int(choice) > len(save_files):
            print("Invalid choice.")
            start_menu()
            return
        
        # Load the chosen save file
        save_filename = f"saves/{save_files[int(choice) - 1]}"
        with open(save_filename, "r") as save_file:
            save_data = json.load(save_file)
        
        # Restore game state
        playerdata.player_data = save_data["player_data"]
        playerdata.inventory = save_data["inventory"]
        
        # Restore location
        global location
        location_name = save_data["metadata"]["location"]
        location = location_registry.get(location_name, locations.greenwood_village)
        
        print(f"Game loaded! Welcome back, {playerdata.player_data['name']}!")
        main_menu()

    except json.JSONDecodeError:
        print("Error: Save file is corrupted.")
        start_menu()
    except Exception as e:
        print(f"An error occurred while loading the game: {e}")
        start_menu()

def main_menu():
    # This function will present the main menu to the player and handle their input to navigate through the different options in the game.
    while True:
        if location is not None:
            print(f"\nYou are currently at: {location.name}")
            print(location.description)
        print("\nMain Menu:")
        print("1. Explore")
        print("2. Inventory")
        print("3. Quests")
        print("4. Talk to characters")
        print("5. Fight")
        if location == locations.tavern:
            print("6. Perform for coin")
        elif location == locations.greenwood_village:
            print("6. Beg for coin")
        print("9. Save Game")
        print("0. Exit")
        choice = input("> ")
        
        if choice == "1":
            explore()
        elif choice == "2":
            manage_inventory()
        elif choice == "3":
            view_quests()
        elif choice == "4":
            talk_to_characters()
        elif choice == "5":
            fight()
        elif choice == "6":
            if location == locations.tavern:
                perform()
            elif location == locations.greenwood_village:
                beg()
            else:
                print("This option is not available in your current location.")
        elif choice == "9":
            save_game()
        elif choice == "0":
            print("Thanks for playing! Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def explore():
    # This function will handle the exploration aspect of the game, allowing the player to encounter enemies, find loot, and discover new areas.
    # This function will also update the player's current location variable as they move between different areas in the game world, and provide new information based on the location.
    global location
    print("You see the following exits: ")
    for exit_name in location.exits:
        print(f"- {exit_name}")
    print("Where would you like to go?")
    choice = input("> ")
    if choice in location_registry and choice in location.exits:
        location = location_registry[choice]
        print(f"You move to {location.name}.")
    else:
        print("Invalid choice. Please try again.")
    
def manage_inventory():
    # This function will allow the player to manage their inventory, including equipping items, using potions, and selling loot.
    # This function will also include changing equipment, using items, and small crafting capabilities.
    print("You check your inventory...")
    for section in ["equipped", "backpack"]:
        for item in playerdata.inventory.get(section, []):
            print(f"- {item}")
        print("Would you like to manage your equipment, or view your backpack?")
    choice = input("> ")
    if choice == "equipment":
        print("You manage your equipment...")
        for item in playerdata.inventory.get("equipped", []):
            print(f"- {item}")
        print("Would you like to change your equipment, or go back to the main menu? (slot/back)")
        choice = input("> ")
        if choice == "weapon":
            print(f"You change your weapon... Currently equipped: {playerdata.inventory['equipped']['weapon']}")
            list_of_weapons = [item for item in playerdata.inventory['backpack']['equipment']['weapons']]
            print("Available weapons in your backpack:")
            for weapon in list_of_weapons:
                print(f"- {weapon}")
            print("Which weapon would you like to equip? (name/back)")
            choice = input("> ")
            if choice in list_of_weapons:
                playerdata.inventory['equipped']['weapon'] = choice
                print(f"You have equipped {choice}.")
            elif choice == "back":
                return
            else:
                print("Invalid choice. Please try again.")
                choice = input("> ")
        elif choice == "armor":
            print(f"You change your armor... Currently equipped: {playerdata.inventory['equipped']['armor']}")
            list_of_armor = [item for item in playerdata.inventory['backpack']['equipment']['armor']]
            print("Available armor in your backpack:")
            for armor in list_of_armor:
                print(f"- {armor}")
            print("Which armor would you like to equip? (name/back)")
            choice = input("> ")
            if choice in list_of_armor:
                playerdata.inventory['equipped']['armor'] = choice
                print(f"You have equipped {choice}.")
            elif choice == "back":
                return
            else:
                print("Invalid choice. Please try again.")
                choice = input("> ")
        elif choice == "accessories":
            print(f"You change your accessories. You have the following equipped: {playerdata.inventory['equipped']['accessories']}")
            list_of_accessories = [item for item in playerdata.inventory['backpack']['equipment']['accessories']]
            print("Available accessories in your backpack:")
            for accessory in list_of_accessories:
                print(f"- {accessory}")
            print(f"Which accessory would you like to equip in {choice}? (name/back)")
            choice = input("> ")
            if choice in list_of_accessories:
                if choice.slot == "ring":
                    print("You have two ring slots. Which one would you like to equip this accessory in? (ring1/ring2/back)")
                    slot_choice = input("> ")
                    if slot_choice in ["ring1", "ring2"]:
                        playerdata.inventory['equipped']['accessories'][slot_choice] = choice
                        print(f"You have equipped {choice} in {slot_choice}.")
                    elif slot_choice == "back":
                        return
                    else:
                        print("Invalid choice. Please try again.")
                        slot_choice = input("> ")
                playerdata.inventory['equipped']['accessories'][choice] = choice
                print(f"You have equipped {choice} in {choice}.")
        elif choice == "back":            
            return
        else:
            print("Invalid choice. Please try again.")
            choice = input("> ")
    elif choice == "backpack":
        print("You check your backpack... You have the following sections: ")
        for section in ["potions", "crafting_materials", "loot", "quest_items", "equipment"]:
            print(f"- {section.capitalize()}")
        print("Which section would you like to view? (name/back)")
        choice = input("> ")
        if choice in ["potions", "crafting_materials", "loot", "quest_items"]:
            print(f"{choice}:")
            for item in playerdata.inventory['backpack'].get(choice, []):
                print(f"- {item}")
            if choice == "potions":
                pass  # This is where the player would be able to use potions from their backpack
            elif choice == "crafting_materials":
                pass  # This is where the player would be able to use crafting materials from their backpack
            elif choice == "loot":
                for item in playerdata.inventory['backpack']['loot']:
                    print(f"- {item}")
            elif choice == "quest_items":
                for item in playerdata.inventory['backpack']['quest_items']:
                    print(f"- {item}")
            elif choice == "equipment":
                print ("You check your backpack for equipment... You have the following weapons, armor, and accessories: ")
                for item in playerdata.inventory['backpack']['equipment']['weapons']:
                    print(f"- {item}")
                for item in playerdata.inventory['backpack']['equipment']['armor']:
                    print(f"- {item}")
                for item in playerdata.inventory['backpack']['equipment']['accessories']:
                    print(f"- {item}")
            elif choice == "back":
                return
            else:
                print("Invalid choice. Please try again.")
                choice = input("> ")
    else: 
        print("Invalid choice. Please try again.")
        choice = input("> ")

def view_quests():
    # This function will allow the player to view their current quests, including any active quests and completed quests.
    # Currently, this is just a placeholder function that can be expanded upon in the future to include a more complex quest system with different quest types, objectives, and rewards.
    print("You review your quests...")

def talk_to_characters():
    # This function will allow the player to talk to characters in the game world, including NPCs and quest givers.
    # Currently, this is just a placeholder function that can be expanded upon in the future to include a more complex dialogue system with different dialogue options, branching conversations, and character interactions.
    print("You look around for characters to talk to...")

def fight():
    # This function will handle looking for combat.
    print("You prepare for battle...")
    if location is not None and location.enemies:
        enemy = random.choices(location.enemies, weights=[enemy['probability'] for enemy in location.enemies])[0]
        print(f"You encounter a {enemy['name']}!")
        combat(enemy)
    else:
        print("There are no enemies here.")

def combat(enemy):
    # This function will handle the actual combat mechanics, including calculating damage, applying effects, and determining the outcome of the battle.
    # Currently, this is just a placeholder function that can be expanded upon in the future to include a more complex combat system with different player abilities, enemy behaviors, and loot drops.
    print(f"You fight the {enemy['name']}... (Combat system not yet implemented)")

def beg():
    # This function will allow the player to beg for coin in the village.
    print("You beg for coin in the village...")
    earned_coin = math.ceil(random.randint(0, 5) * playerdata.player_data.charisma)  # Randomly earn between 0 and 5 coins, times charisma stat
    playerdata.player_data["gold"] += earned_coin
    print(f"You earned {earned_coin} gold from begging.")

def perform():
    # This function will allow the player to perform for coin in the tavern.
    if location != locations.tavern:
        print("You can only perform for coin in the tavern! This should never be called if the player is not in the tavern, but if so, please contact the developer.")
    else:
        if playerdata.inventory.quest_items.get("lute"):
            print("You perform for coin in the tavern...")
            earned_coin = math.ceil(random.randint(0, 10) * playerdata.player_data.charisma)  # Randomly earn between 0 and 10 coins, times charisma stat
            playerdata.player_data["gold"] += earned_coin
            print(f"You earned {earned_coin} gold from performing.")
        else:
            print("You don't have a lute to perform with! Maybe you can find one in the blacksmith or general store.")
start_menu()