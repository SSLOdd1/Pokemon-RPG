### CHARACTERS ###
# This file contains the definitions of all characters in the game, including their names, descriptions, and any special abilities or traits they may have. This file will be used to populate the characters that can be found in each location, as well as any characters that may be encountered during quests or battles.
# Each character is represented as a dictionary with the following information:
# - name: The name of the character.
# - description: A brief description of the character, including any notable features or traits.
# - dialogue: A list of any dialogue lines that the character may have, along with any conditions or triggers for when they will be said. May be blank.
# - quests: A list of any quests that the character may offer to the player, along with their descriptions and rewards. May be blank.
# - location: The location where the character can be found. This will be used to populate the characters in each location, and may also be used to trigger certain events or quests when the player interacts with the character. May be blank if the character is not tied to a specific location.
# - Interactions: A list of any special interactions or abilities that the character may have, such as being able to teach the player new skills, open for commerce, or provide unique items. May be blank.

characters=[
    {
        "name": "Hormond the Blacksmith",
        "description": "A skilled blacksmith who can forge powerful weapons and armor.",
        "dialogue": ["Have you seen my cat? His name is Whiskers and he's very dear to me. I last saw him around the tavern, but I haven't been able to find him since."],
        "quests": [],
        "location": "blacksmith",
        "shop_id": "Hormond_blacksmith_shop",
        "interactions": [
            {
                "type": "crafting",
                "description": "Hormond can forge weapons and armor for the player, using materials that the player provides. He can also repair damaged equipment."
            },
            {
                "type": "commerce",
                "description": "Hormond can sell the player items, equipment, and materials for gold."
            }
        ]
    },
    {
        "name": "Erhle the Merchant",
        "description": "A shrewd merchant who can sell the player a variety of goods, including potions, scrolls, and rare items.",
        "dialogue": [],
        "quests": [],
        "location": "general_store",
        "shop_id": "Erhle_general_store_shop",
        "interactions": [
            {
                "type": "commerce",
                "description": "Erhle can sell the player a variety of goods, including potions, scrolls, and rare items."
            }
        ]
    },
    {
        "name": "Arlene the Tavern Keeper",
        "description": "A friendly tavern keeper who can provide the player with food, drink, and a place to rest. She may also have information about local rumors and quests.",
        "dialogue_id": "Arlene_dialogue",
        "quests": [],
        "location": "tavern",
        "shop_id": "Arlene_tavern_shop",
        "interactions": [
            {
                "type": "commerce",
                "description": "Arlene can provide the player with food and drink."
            },
            {
                "type": "quest_giver",
                "description": "Arlene may offer the player quests related to the tavern."
            }
        ]
    },
    {
        "name": "Gwen, Ruler of Greenwood",
        "description": "The benevolent ruler of Greenwood Village, known for her wisdom and kindness.",
        "dialogue": [],
        "quests": [],
        "location": "royal_palace",
        "shop_id": None,
        "interactions": [
            {
                "type": "quest_giver",
                "description": "Gwen may offer the player quests related to the safety and prosperity of Greenwood Village."
            }
        ]
    }
]