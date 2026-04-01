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

def load_game():
    # This function will load a saved game, allowing the player to continue from where they left off. This will involve reading the player's data and inventory from a file, and updating the game state accordingly.
    print("Loading game... (This feature is not yet implemented)")

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
            print("You change your weapon...")
            # Code to change weapon goes here
        elif choice == "armor":
            print("You change your armor...")
            # Code to change armor goes here
        elif choice in ["ring1", "ring2", "amulet", "belt"]:
            print(f"You change your {choice}...")
            # Code to change accessory goes here
        elif choice == "back":            return
        else:
            print("Invalid choice. Please try again.")
            choice = input("> ")
    elif choice == "backpack":
        break
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
    # This function will handle the combat system, allowing the player to fight against enemies and gain experience points and loot.
    # Currently, this is just a placeholder function that can be expanded upon in the future to include a more complex combat system with different enemy types, player abilities, and loot drops.
    print("You prepare for battle...")

new_game()