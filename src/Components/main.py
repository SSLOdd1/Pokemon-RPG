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
location_data = {
    "name": location.name if location else "Unknown",
    "description": location.description if location else "No description available.",
}  # This variable will store the data for the player's current location, including the description, available exits, and any enemies or characters present in the location. This data will be updated whenever the player moves to a new location or when certain events occur that change the state of the location.

# Create a location registry for easy lookup by name
location_registry = {
    "village": locations.greenwood_village,
    "tavern": locations.tavern,
    "blacksmith": locations.blacksmith,
    "general_store": locations.general_store,
    "tavern_basement": locations.tavern_basement,
    "royal_palace": locations.royal_palace,
    "greenwood_forest": locations.greenwood_forest,
    "orc_camp": locations.orc_camp
}
# Create a character registry for easy lookup by name
character_registry = {character["name"]: character for character in characters.characters}

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
    update_location_data()  # Update location data for the starting location
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
        # Merge saved player_data with defaults to preserve any new keys added to the game
        loaded_data = save_data["player_data"]
        for key in playerdata.player_data:
            if key not in loaded_data:
                loaded_data[key] = playerdata.player_data[key]
        playerdata.player_data = loaded_data
        playerdata.inventory = save_data["inventory"]
        
        # Restore location
        global location
        location_name = save_data["metadata"].get("location")
        location = location_registry.get(location_name)
        if location is None and location_name:
            for loc in location_registry.values():
                if loc.name == location_name:
                    location = loc
                    break
        if location is None:
            location = locations.greenwood_village
        update_location_data()  # Update location data after loading location
        
        print(f"Game loaded! Welcome back, {playerdata.player_data['name']}!")

    except json.JSONDecodeError:
        print("Error: Save file is corrupted.")
        start_menu()
        return
    except Exception as e:
        print(f"An error occurred while loading the game: {e}")
        start_menu()
        return

    main_menu()


def resolve_character(character_entry):
    # Normalize character entries so locations can store either full dicts or character names.
    if isinstance(character_entry, dict):
        return character_entry
    if isinstance(character_entry, str):
        return character_registry.get(character_entry, {"name": character_entry})
    return None

def main_menu():
    # This function will present the main menu to the player and handle their input to navigate through the different options in the game.
    while True:
        if location is not None:
            update_location_data()  # Update location data at the start of each loop iteration to ensure it's current, should be redun
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
    available_exits = [exit_name for exit_name in location.exits if exit_name in location_registry]

    if not available_exits:
        print("There are no available exits here.")
        return

    print("You see the following exits: ")
    for index, exit_name in enumerate(available_exits, 1):
        destination = location_registry[exit_name]
        print(f"{index}. {destination.name}")

    print("Where would you like to go? Enter a number or an exit key.")
    choice = input("> ")

    selected_location = None
    if choice.isdigit() and 1 <= int(choice) <= len(available_exits):
        selected_location = location_registry[available_exits[int(choice) - 1]]
    elif choice in available_exits:
        selected_location = location_registry[choice]

    if selected_location is not None:
        location = selected_location
        print(f"You move to {location.name}.")
        update_location_data()  # Update location data after moving to a new location
    else:
        print("Invalid choice. Please try again.")
    
def manage_inventory():
    # This function will allow the player to manage their inventory, including equipping items, using potions, and selling loot.
    # This function will also include changing equipment, using items, and small crafting capabilities.
    print("You check your inventory...")
    for section in ["equipped", "backpack"]:
        for item in playerdata.inventory.get(section, []):
            print(f"- {item}")
    print(f"You have {playerdata.player_data['gold']} gold.")
    print("What would you like to do?")
    print("1. Manage Equipment")
    print("2. View Backpack")
    print("0. Back")
    choice = input("> ")
    if choice == "1":
        print("You manage your equipment...")
        for item in playerdata.inventory.get("equipped", []):
            print(f"- {item}")
        print("Which slot would you like to change?")
        print("1. Weapon")
        print("2. Armor")
        print("3. Accessories")
        print("0. Back")
        choice = input("> ")
        if choice == "1":
            print(f"You change your weapon... Currently equipped: {playerdata.inventory['equipped']['weapon']}")
            list_of_weapons = [item for item in playerdata.inventory['backpack']['equipment']['weapons']]
            print("Available weapons in your backpack:")
            for i, weapon in enumerate(list_of_weapons, 1):
                print(f"{i}. {weapon}")
            print("0. Back")
            print("Which weapon would you like to equip?")
            choice = input("> ")
            if choice.isdigit() and 1 <= int(choice) <= len(list_of_weapons):
                selected_weapon = list_of_weapons[int(choice) - 1]
                playerdata.inventory['equipped']['weapon'] = selected_weapon
                print(f"You have equipped {selected_weapon}.")
            elif choice == "0":
                return
            else:
                print("Invalid choice. Please try again.")
        elif choice == "2":
            print(f"You change your armor... Currently equipped: {playerdata.inventory['equipped']['armor']}")
            list_of_armor = [item for item in playerdata.inventory['backpack']['equipment']['armor']]
            print("Available armor in your backpack:")
            for i, armor in enumerate(list_of_armor, 1):
                print(f"{i}. {armor}")
            print("0. Back")
            print("Which armor would you like to equip?")
            choice = input("> ")
            if choice.isdigit() and 1 <= int(choice) <= len(list_of_armor):
                selected_armor = list_of_armor[int(choice) - 1]
                playerdata.inventory['equipped']['armor'] = selected_armor
                print(f"You have equipped {selected_armor}.")
            elif choice == "0":
                return
            else:
                print("Invalid choice. Please try again.")
        elif choice == "3":
            print(f"You change your accessories. You have the following equipped: {playerdata.inventory['equipped']['accessories']}")
            list_of_accessories = [item for item in playerdata.inventory['backpack']['equipment']['accessories']]
            print("Available accessories in your backpack:")
            for i, accessory in enumerate(list_of_accessories, 1):
                print(f"{i}. {accessory}")
            print("0. Back")
            print("Which accessory would you like to equip?")
            choice = input("> ")
            if choice.isdigit() and 1 <= int(choice) <= len(list_of_accessories):
                selected_accessory = list_of_accessories[int(choice) - 1]
                print("You have two ring slots. Which one would you like to equip this accessory in?")
                print("1. Ring Slot 1")
                print("2. Ring Slot 2")
                print("3. Amulet")
                print("4. Belt")
                print("0. Back")
                slot_choice = input("> ")
                if slot_choice == "1":
                    playerdata.inventory['equipped']['accessories']['ring1'] = selected_accessory
                    print(f"You have equipped {selected_accessory} in ring slot 1.")
                elif slot_choice == "2":
                    playerdata.inventory['equipped']['accessories']['ring2'] = selected_accessory
                    print(f"You have equipped {selected_accessory} in ring slot 2.")
                elif slot_choice == "3":
                    playerdata.inventory['equipped']['accessories']['amulet'] = selected_accessory
                    print(f"You have equipped {selected_accessory} as amulet.")
                elif slot_choice == "4":
                    playerdata.inventory['equipped']['accessories']['belt'] = selected_accessory
                    print(f"You have equipped {selected_accessory} as belt.")
                elif slot_choice == "0":
                    return
            elif choice == "0":
                return
        elif choice == "0":            
            return
        else:
            print("Invalid choice. Please try again.")
            choice = input("> ")
    elif choice == "2":
        print("You check your backpack... You have the following sections: ")
        sections = ["potions", "crafting_materials", "loot", "quest_items", "equipment"]
        for i, section in enumerate(sections, 1):
            print(f"{i}. {section.capitalize()}")
        print("0. Back")
        print("Which section would you like to view?")
        choice = input("> ")
        if choice.isdigit() and 1 <= int(choice) <= len(sections):
            choice = sections[int(choice) - 1]
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
                print("You check your backpack for equipment... You have the following weapons, armor, and accessories: ")
                for item in playerdata.inventory['backpack']['equipment']['weapons']:
                    print(f"- {item}")
                for item in playerdata.inventory['backpack']['equipment']['armor']:
                    print(f"- {item}")
                for item in playerdata.inventory['backpack']['equipment']['accessories']:
                    print(f"- {item}")
        elif choice == "0":
            return
        else:
            print("Invalid choice. Please try again.")
    elif choice == "0": 
        return
    else: 
        print("Invalid choice. Please try again.")

def view_quests():
    # This function will allow the player to view their current quests, including any active quests and completed quests.
    print("You review your quests...")

    print("Active Quests:")
    for quest in playerdata.active_quests:
        print(f"- {quest['name']}")

    print("Finished Quests:")
    for quest in playerdata.finished_quests:
        print(f"- {quest['name']}")

    print("Failed Quests:")
    for quest in playerdata.failed_quests:
        print(f"- {quest['name']}")

def talk_to_characters():
    # This function will allow the player to talk to characters in the game world, including NPCs and quest givers.
    print("You look around for characters to talk to...")
    if location is not None and location.characters:
        available_characters = [
            resolve_character(character_entry)
            for character_entry in location.characters
        ]
        available_characters = [
            character for character in available_characters
            if character is not None and "name" in character
        ]

        if not available_characters:
            print("You don't see anyone you can talk to.")
            return

        print("You see the following characters:")
        for index, character in enumerate(available_characters, 1):
            print(f"{index}. {character['name']}")
        print("Who would you like to talk to? Enter a number or a name.")
        choice = input("> ")
        selected_character = None
        if choice.isdigit() and 1 <= int(choice) <= len(available_characters):
            selected_character = available_characters[int(choice) - 1]
        else:
            for character in available_characters:
                if character['name'].lower() == choice.lower():
                    selected_character = character
                    break
        if selected_character is not None:
            dialogue_system(selected_character)
        else:
            print("Invalid choice. Please try again.")
    else:
        print("There is no one here to talk to.")

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
    earned_coin = math.ceil(random.randint(0, 5) * playerdata.player_data["charisma"])  # Randomly earn between 0 and 5 coins, times charisma stat
    playerdata.player_data["gold"] += earned_coin
    print(f"You earned {earned_coin} gold from begging.")

def perform():
    # This function will allow the player to perform for coin in the tavern.
    if location != locations.tavern:
        print("You can only perform for coin in the tavern! This should never be called if the player is not in the tavern, but if so, please contact the developer.")
    else:
        if playerdata.inventory.quest_items.get("lute"):
            print("You perform for coin in the tavern...")
            earned_coin = math.ceil(random.randint(0, 10) * playerdata.player_data["charisma"])  # Randomly earn between 0 and 10 coins, times charisma stat
            playerdata.player_data["gold"] += earned_coin
            print(f"You earned {earned_coin} gold from performing.")
        else:
            print("You don't have a lute to perform with! Maybe you can find one in the blacksmith or general store.")

def update_location_data():
    # This function will update the player's current location data, including any changes to the location's description, available exits, and enemies.
    # This function can be called whenever the player moves to a new location or when certain events occur that change the state of the location.
    global location_data
    location_data = {
        "name": location.name if location else "Unknown",
        "description": location.description if location else "No description available.",
}

def dialogue_system(character):
    # This function will handle the dialogue system for talking to characters in the game world, including NPCs and quest givers.
    # Currently, this is just a placeholder function that can be expanded upon in the future to include a more complex dialogue system with different dialogue options, branching conversations, and character interactions.
    print(f"You talk to {character['name']}...")

    dialogue_id = character.get("dialogue_id")
    if not dialogue_id:
        print("They have nothing to say right now.")
        return

    dialogue_registry = getattr(dialogue, "dialogue_data", {})
    lines = dialogue_registry.get(dialogue_id, [])
    if not lines:
        print("They have nothing to say right now.")
        return

    context = build_dialogue_context()

    # Build quick lookup by node id
    by_id = {line.get("id"): line for line in lines if "id" in line}

    # Start at greeting node if present, otherwise first line
    current = next(
        (
            line for line in lines
            if str(line.get("id", "")).endswith("_greeting")
            and conditions_pass(line.get("conditions", []), context)
        ),
        None
    )

    if current is None:
        print("They have nothing to say right now.")
        return

    while current:
        print(f"{character['name']}: {current['text']}")

        responses = get_available_responses(current, context)
        if not responses:
            return

        for i, response in enumerate(responses, 1):
            print(f"{i}. {response['text']}")

        choice = input("> ").strip()
        if not choice.isdigit() or not (1 <= int(choice) <= len(responses)):
            print("Invalid choice. Please try again.")
            continue

        selected = responses[int(choice) - 1]

        should_exit = effect_handler(selected.get("effects"))
        if should_exit:
            return

        next_id = selected.get("next_id")
        if not next_id:
            return
        next_node = by_id.get(next_id)
        if not next_node:
            return
        if not conditions_pass(next_node.get("conditions", []), context):
            print("They have nothing else to discuss right now.")
            return
        current = next_node

def build_dialogue_context():
    active_ids = {q.get("id") for q in playerdata.active_quests}
    finished_ids = {q.get("id") for q in playerdata.finished_quests}
    return {
        "active_quest_ids": active_ids,
        "finished_quest_ids": finished_ids,
    }

def conditions_pass(condition_list, context):
    if not condition_list:
        return True
    try:
        return all(condition(context) for condition in condition_list)
    except Exception as e:
        print(f"Condition error: {e}")
        return False

def get_available_responses(node, context):
    responses = node.get("responses", [])
    available = []
    for response in responses:
        requirements = response.get("requirements", [])
        if conditions_pass(requirements, context):
            available.append(response)
    return available

def effect_handler(effect):
    # This function will handle applying effects from dialogue responses, such as starting quests, opening shops, providing information, etc.

    if not effect:
        return False
    if isinstance(effect, dict):
        effect = [effect]

    should_exit = False

    for e in effect:
        effect_type = e.get("type")
        if effect_type == "start_quest":
            quest_id = e.get("quest_id") or e.get("quest_name")
            if quest_id:
                started = quests.start_quest(quest_id)
                if started:
                    print(f"Starting quest: {quest_id}")
            else:
                print("Error: No quest_id provided for start_quest effect.")

        elif effect_type == "open_shop":
            shop_name = e.get("shop_name")
            print(f"Opening shop: {shop_name} (Shop system not yet implemented)")
        elif effect_type == "provide_information":
            info_type = e.get("information_type")
            print(f"Providing information: {info_type} (Information system not yet implemented)")
        elif effect_type == "exit_dialogue":
            print("Exiting dialogue.")
            should_exit = True
        else:
            print(f"Unknown effect type: {effect_type}")

    return should_exit


if __name__ == "__main__":
    start_menu()