## Enemies
# Enemy data is stored in a list of dictionaries. Each inner dictionary represents a different enemy type, and contains the following information:
# - name: The name of the enemy.
# - health: The amount of health the enemy has.
# - attack: The amount of damage the enemy can deal to the player.
# - defense: The amount of damage the enemy can block from the player's attacks.
# - type: The type of enemy (e.g. "normal", "boss", "undead", "poisonous" etc.).
# - description: A brief description of the enemy, including any special abilities or weaknesses they may have.
# - loot: A list of items that the enemy may drop when defeated, along with the probability of each item dropping.
# - experience: The amount of experience points the player gains when defeating the enemy.

class Enemy:
    """Represents an enemy that the player can encounter and fight in the game."""
    
    def __init__(self, name: str, health: int, attack: int, defense: int, type: str, description: str, loot: list, experience: int):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.type = type
        self.description = description
        self.loot = loot
        self.experience = experience
    
    def __repr__(self):
        return f"Enemy(name='{self.name}', health={self.health}, type='{self.type}')"
    
    def __str__(self):
        return self.name


enemies = [
    Enemy(
        name="Goblin",
        health=30,
        attack=5,
        defense=2,
        type="normal",
        description="A small, green creature that is quick and agile. They are often found in groups and can be dangerous if not dealt with quickly.",
        loot=[
            {"item": "Gold Lump", "probability": 0.5},
            {"item": "Rusty Dagger", "probability": 0.3},
            {"item": "Goblin Ear", "probability": 0.2}
        ],
        experience=25
    ),
    Enemy(
        name="Rat",
        health=20,
        attack=3,
        defense=1,
        type="normal",
        description="A common pest that can be found in many locations. They are weak but can be a nuisance if they swarm the player.",
        loot=[
            {"item": "Rat Tail", "probability": 0.5},
            {"item": "Rat Ear", "probability": 0.3},
            {"item": "Rat Fur", "probability": 0.2}
        ],
        experience=10
    ),
    Enemy(
        name="Skeleton Warrior",
        health=50,
        attack=10,
        defense=5,
        type="undead",
        description="A reanimated skeleton that wields a sword and shield. They are slow but can be difficult to defeat due to their high defense.",
        loot=[
            {"item": "Bone Shard", "probability": 0.4},
            {"item": "Iron Sword", "probability": 0.4},
            {"item": "Skeleton Key", "probability": 0.2}
        ],
        experience=50
    ),
    Enemy(
        name="Giant Spider",
        health=40,
        attack=8,
        defense=3,
        type="poisonous",
        description="A large spider that can climb walls and ceilings. They can inject venom that causes damage over time.",
        loot=[
            {"item": "Spider Silk", "probability": 0.5},
            {"item": "Venom Sac", "probability": 0.3},
            {"item": "Giant Spider Leg", "probability": 0.2}
        ],
        experience=75
    ),
    Enemy(
        name="Orc Warlord",
        health=100,
        attack=20,
        defense=10,
        type="boss",
        description="A powerful orc leader who commands a group of followers. He is heavily armored and can deal devastating attacks.",
        loot=[
            {"item": "Orcish Axe", "probability": 0.4},
            {"item": "Warrior's Helm", "probability": 0.4},
            {"item": "Orcish Banner", "probability": 0.2}
        ],
        experience=150
    )
]