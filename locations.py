### LOCATIONS ###
# This file contains the locations of various areas in the game world, including towns, dungeons, and other points of interest.
# Some locations are sublocations of others, such as a shop in a town.
# Locations are represented as instances of the Location class with the following information:
# - name: The name of the location.
# - description: A brief description of the location, including any notable features or landmarks.
# - characters: A list of characters that can be found in the location, along with their descriptions and any quests they may offer. May be blank.
# - enemies: A list of enemies that can be found in the location, along with their probabilities of appearing.
# - loot: A list of items that can be found in the location, along with their probabilities of appearing.
# - exits: A list of names representing areas accessible from the main location.


class Location:
    """Represents a location in the game world."""
    
    def __init__(self, name: str, description: str, characters: list = None, enemies: list = None, loot: list = None, exits: list = None):
        self.name = name
        self.description = description
        self.characters = characters or []
        self.enemies = enemies or []
        self.loot = loot or []
        self.exits = exits or []
    
    def __repr__(self):
        return f"Location(name='{self.name}')"
    
    def __str__(self):
        return self.name


tavern_basement = Location(
    name="Greenwood Tavern Basement",
    description="A dimly lit basement beneath the tavern. It is rumored to be haunted, and some say that strange noises can be heard coming from down there at night.",
    characters=[],
    enemies=[
        {"name": "Rat", "probability": 0.7},
        {"name": "Giant Spider", "probability": 0.3}
    ],
    loot=[
        {"item": "Gold Lump", "probability": 0.5},
        {"item": "Spider Silk", "probability": 0.3},
        {"item": "Rusty Dagger", "probability": 0.2}
    ],
    exits=["tavern"]
)

tavern = Location(
    name="Greenwood Tavern",
    description="A lively tavern where adventurers can gather to share stories, find new quests, and enjoy a drink. The tavern is run by a jovial innkeeper who is always eager to hear about the latest adventures.",
    characters=[],
    enemies=[],
    loot=[],
    exits=["tavern_basement", "greenwood_village"]
)

blacksmith = Location(
    name="Greenwood Blacksmith",
    description="A small blacksmith shop where the local blacksmith sells basic weapons and armor. The blacksmith can also repair damaged equipment for a fee.",
    characters=[],
    enemies=[],
    loot=[],
    exits=["greenwood_village"]
)

general_store = Location(
    name="Greenwood General Store",
    description="A small general store that sells a variety of items, including potions, crafting materials, and basic equipment. The store is run by a friendly shopkeeper who is always willing to help adventurers find what they need.",
    characters=[],
    enemies=[],
    loot=[],
    exits=["greenwood_village"]
)

greenwood_village = Location(
    name="Greenwood Village",
    description="A peaceful village surrounded by lush forests. The villagers are friendly and often have quests for adventurers. Includes a basic blacksmith, a general store, and a tavern.",
    characters=[],
    enemies=[],
    loot=[],
    exits=["blacksmith", "general_store", "tavern"]
)

royal_palace = Location(
    name="Royal Palace",
    description="The grand residence of the king and queen, filled with ornate decorations and guarded by royal knights.",
    characters=[],
    enemies=[],
    loot=[],
    exits=["greenwood_village"]
)