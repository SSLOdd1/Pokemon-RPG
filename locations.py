### LOCATIONS ###
# This file contains the locations of various areas in the game world, including towns, dungeons, and other points of interest.
# Some locations are sublocations of others, such as a shop in a town.
# Each location is represented as a dictionary with the following information:
# - name: The name of the location.
# - description: A brief description of the location, including any notable features or landmarks.
# - characters: A list of characters that can be found in the location. These will be pulled from another file. May be blank.
# - enemies: A list of enemies that can be found in the location, along with their probabilities of appearing. May be blank.
# - loot: A list of items that can be found in the location, along with their probabilities of appearing. May be blank.
# - quests: A list of quests that can be completed in the location, along with their descriptions and rewards. May be blank.
# - sublocations: A list of sublocations that can be accessed from the main location, along with their descriptions and any special features they may have. May be blank.

locations=[
    {
        "Greenwood Village" : {
            "description": "A peaceful village surrounded by lush forests. The villagers are friendly and often have quests for adventurers. Includes a basic blacksmith, a general store, and a tavern.",
            "enemies": [],
            "loot": [],
            "quests": [],
            "sublocations": {
                "Blacksmith": {
                    "description": "A small blacksmith shop where the local blacksmith sells basic weapons and armor. The blacksmith can also repair damaged equipment for a fee.",
                    "enemies": [],
                    "loot": [],
                    "quests": [],
                    "sublocations": {}
                },
                "General Store": {
                    "description": "A small general store that sells a variety of items, including potions, crafting materials, and basic equipment. The store is run by a friendly shopkeeper who is always willing to help adventurers find what they need.",
                    "enemies": [],
                    "loot": [],
                    "quests": [],
                    "sublocations": {}
                },
                "Tavern": {
                    "description": "A lively tavern where adventurers can gather to share stories, find new quests, and enjoy a drink. The tavern is run by a jovial innkeeper who is always eager to hear about the latest adventures.",
                    "enemies": [],
                    "loot": [],
                    "quests": [
                        {"name": "Lost Cat", "description": "The innkeeper's beloved cat has gone missing. Help find the cat and return it to the innkeeper for a reward.", "reward": {"item": "Gold Lump", "quantity": 10}}
                    ],
                    "sublocations": {
                        "Tavern Basement": {
                            "description": "A dimly lit basement beneath the tavern. It is rumored to be haunted, and some say that strange noises can be heard coming from down there at night.",
                            "enemies": [
                                {"name": "Rat", "probability": 0.7},
                                {"name": "Giant Spider", "probability": 0.3}
                            ],
                            "loot": [
                                {"item": "Gold Lump", "probability": 0.5},
                                {"item": "Spider Silk", "probability": 0.3},
                                {"item": "Rusty Dagger", "probability": 0.2}
                            ],
                            "quests": [],
                            "sublocations": {}
                        }
                    }}
                }
        }

    }
]