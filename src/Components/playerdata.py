### PLAYER DATA ###
## This file contains the player's data, including their name, level, health, mana, experience points, and inventory.
## The player's data is stored in a dictionary, which can be easily accessed and modified throughout the game. The player's inventory is also stored in a separate dictionary, which includes their equipped items and backpack items. This allows for easy management of the player's equipment and inventory throughout the game.

import math


BASE_LEVEL_XP = 100
LEVEL_XP_GROWTH = 1.25

## Player Data
# The player's data is stored in a dictionary with the following keys:
# - name: The player's name.
# - level: The player's current level. The player starts at level 1 and can level up by gaining experience points from defeating enemies and completing quests.
# - health: The player's current health points. The player starts with a certain amount of health, which can be increased by leveling up or equipping certain items.
# - mana: The player's current mana points. The player starts with a certain amount of mana, which can be increased by leveling up or equipping certain items.
# - experience: The player's current experience points. The player gains experience points from defeating enemies and completing quests, which can be used to level up.
# - skills: A list of the player's skills and abilities. As the player levels up, they will gain access to new skills and abilities that can be used in combat or for exploration.
# - gold: The player's current amount of gold. Gold can be used to purchase items, equipment, and services from merchants and other characters in the game world.   

player_data={
    "name": "Player1",
    "level": 1,
    "health": 100,
    "mana": 50,
    "experience": 0,
    "gold": 0,
    "attack": 1,
    "defense": 1,
    "strength": 1,
    "dexterity": 1,
    "intelligence": 1,
    "charisma": 1,
    "luck": 1,
    "skills": []

    
}


def experience_to_next_level(level=None):
    if level is None:
        level = player_data.get("level", 1)

    level = max(1, int(level))
    return math.ceil(BASE_LEVEL_XP * (LEVEL_XP_GROWTH ** (level - 1)))


def process_level_ups():
    current_level = max(1, int(player_data.get("level", 1)))
    current_experience = max(0, int(player_data.get("experience", 0)))
    levels_gained = 0

    while True:
        required_xp = experience_to_next_level(current_level)
        if current_experience < required_xp:
            break

        current_experience -= required_xp
        current_level += 1
        levels_gained += 1

    player_data["level"] = current_level
    player_data["experience"] = current_experience
    return levels_gained


def add_experience(amount):
    amount = int(amount)
    if amount <= 0:
        return 0

    player_data["experience"] = max(0, int(player_data.get("experience", 0))) + amount
    return process_level_ups()

## Quest Tracking
# The player's quest progress is tracked using three lists: active_quests, finished_quests, and failed_quests. Each quest is represented as a dictionary with its name, description, requirements, tasks, and rewards. The player can have multiple active quests at once, and can complete or fail quests based on their actions in the game world.

active_quests = []
finished_quests = []
failed_quests = []

## Inventory System
# The inventory system allows players to manage their items, including weapons, armor, potions, and other consumables.
# This is split between the equipment and backpack sections, which store what is currently equipped and what is in the player's inventory, respectively.
# The equipment section includes slots for weapons, armor, and accessories, while the backpack can hold a variety of items such as potions, crafting materials, loot, and quest items.
# The inventory is split between two dictionaries: one for equipped items and one for backpack items. Each item in the backpack is represented as a dictionary with its name, quantity, and description.

# The equipment section contains the following slots:
# - Weapon: The player's currently equipped weapon. This can be a sword, bow, staff, or any other type of weapon that the player has acquired.
# - Weapons have a name, damage value, and any special effects they may have (e.g. "increases attack power", "has a chance to inflict poison", etc.).
# - Armor: The player's currently equipped armor. This can be a helmet, chestplate, leggings, or boots that the player has acquired.
# - Armor has a name, defense value, and any special effects they may have (e.g. "increases health", "reduces damage taken from fire attacks", etc.).
# - Accessories: The player's currently equipped accessories. This can be one of two rings, an amulet, or a belt that the player has acquired.
# - Accessories have a name and any special effects they may have (e.g. "increases strength", "increases agility", "reduces damage taken", etc.).

# The backpack section can hold a variety of items, including:
# - Potions: Consumable items that can restore health, mana, or provide temporary buffs to the player.
# - Crafting Materials: Items that can be used to craft new equipment or consumables.
# - Loot: Items that can be obtained from defeating enemies or completing quests. These can include gold, gems, and other valuable items.
# - Quest Items: Special items that are required to complete certain quests. These items cannot be sold or used outside of their intended quest.
# - Equipment: Items that the player has acquired but is not currently equipped. These can be stored in the backpack until the player decides to equip them.

inventory={
    "equipped": {
        "weapon": None,  # e.g., {name, price, effect, damage}
        "armor": None,   # e.g., {name, price, effect, defense}
        "accessories": {
            "ring1": None,  # e.g., {name, slot, price, effect}
            "ring2": None,
            "amulet": None,
            "belt": None
        }
    },
    "backpack": {
        # List of items, each as a dict with name, quantity, and optional details
        # e.g., {"name": "Health Potion", "quantity": 3, "description": "Restores 20 health points."},
        "potions": {
            # Example: "Health Potion": {"quantity": 3, "description": "Restores 20 health points."}
        },
        "crafting_materials": {},
        "loot": {},
        "quest_items": {},
        "equipment": {
            "weapons": [],
            "armor": [],
            "accessories": []
        }
    }
}