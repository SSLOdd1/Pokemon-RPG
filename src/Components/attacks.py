### ATTACKS ###
# This will be where all attacks are stored.
# Attacks will be broken up between player attacks, based on equipped weapon, or enemy attacks, based on enemy type.
# Attacks will be stored in dictionaries, storing attack data including name, damage, type, accuracy, and special effects.

# Attack Dictionary Structure:
# {
#     'name': str,           # Name of the attack
#     'damage': int,         # Base damage value
#     'type': str,          # Attack type (e.g., 'physical', 'special', 'status')
#     'accuracy': float,    # Hit accuracy percentage (0-1)
#     'description': str,   # Attack description
# } 

player_attacks = {
    'wooden_sword' : [
        {
            'name': 'Wooden Swing',
            'damage': 3,
            'type': 'attack',
            'accuracy': 0.8,
            'description': 'A basic slash with a wooden sword.'
        },
        {
            'name': 'Wooden Smash',
            'damage': 5,
            'type': 'strength',
            'accuracy': 0.7,
            'description': 'A powerful smash that deals damage based on your strength.'
        },
        {
            "name": "Wooden Stab",
            "damage" : 3,
            "type" : "dexterity",
            "accuracy" : 0.9,
            "description": "A controlled stab at a vital area based on your dexterity."
        }
    ],
    iron_sword :[
        {
            "name": "Iron Slash",
            "damage": 5,
            "type": "attack",
            "accuracy": 0.9,
            "description": "A basic slash with an iron sword."
        },
        {
            "name": "Iron Smash",
            "damage": 7,
            "type": "strength",
            "accuracy": 0.8,
            "description": "A wild smash that does damage based on your strength."
        },
        {
            "name": "Iron Stab",
            "damage": 4,
            "type": "dexterity",
            "accuracy": 1,
            "description": "A controlled stab at a vital area, based on your dexterity."
        }
    ],
    steel_sword: [
         {
            "name": "Steel Slash",
            "damage": 7,
            "type": "attack",
            "accuracy": 1,
            "description": "A basic slash with a steel sword."
        },
        {
            "name": "Steel Smash",
            "damage": 9,
            "type": "strength",
            "accuracy": 0.9,
            "description": "A wild smash that does damage based on your strength."
        },
        {
            "name": "Steel Stab",
            "damage": 5,
            "type": "dexterity",
            "accuracy": 1,
            "description": "A controlled stab at a vital area, based on your dexterity."
        }
    ]
}

enemy_attacks = {} # This is where the enemy attacks go.