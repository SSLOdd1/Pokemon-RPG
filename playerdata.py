### PLAYER DATA ###
## This file contains the player's data, including their name, level, health, mana, experience points, and inventory.
## The player's data is stored in a dictionary, which can be easily accessed and modified throughout the game. The player's inventory is also stored in a separate dictionary, which includes their equipped items and backpack items. This allows for easy management of the player's equipment and inventory throughout the game.

## Player Data
# The player's data is stored in a dictionary with the following keys:
# - name: The player's name.
# - level: The player's current level. The player starts at level 1 and can level up by gaining experience points from defeating enemies and completing quests.
# - health: The player's current health points. The player starts with a certain amount of health, which can be increased by leveling up or equipping certain items.
# - mana: The player's current mana points. The player starts with a certain amount of mana, which can be increased by leveling up or equipping certain items.
# - experience: The player's current experience points. The player gains experience points from defeating enemies and completing quests, which can be used to level up.
# - skills: A list of the player's skills and abilities. As the player levels up, they will gain access to new skills and abilities that can be used in combat or for exploration.

player_data={
    "name": "Player1",
    "level": 1,
    "health": 100,
    "mana": 50,
    "experience": 0,
    "skills": []
}

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

inventory={
    "equipped": {
        "weapon": None,  # e.g., {"name": "Wooden Sword", "damage": 10}
        "armor": None,   # e.g., {"name": "Leather Armor", "defense": 5}
        "accessories": {
            "ring1": None,  # e.g., {"name": "Ring of Strength", "effect": "increases strength"}
            "ring2": None,  # e.g., {"name": "Ring of Agility", "effect": "increases agility"}
            "amulet": None,  # e.g., {"name": "Amulet of Protection", "effect": "reduces damage taken"}
            "belt": None     # e.g., {"name": "Belt of Endurance", "effect": "increases stamina"}
        }
    },
    "backpack": [
        # List of items, each as a dict with name, quantity, and optional details
        # e.g., {"name": "Health Potion", "quantity": 3, "description": "Restores 20 health points."},
    ]
}