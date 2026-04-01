## Loot
# Enemies and chests can drop loot. Loot is stored in a list of dictionaries, where each dictionary represents a different item. Each item has the following information:
# - item: The name of the item.
# - price: The price of the item in gold coins.
# - description: A brief description of the item, including any special properties or uses it may have.
# - effect: The effect of the item when used by the player (e.g. "restores health", "increases attack power", etc.).

loot=[
    {
        "item": "Health Potion",
        "price": 10,
        "description": "Restores 20 health points.",
        "effect": "restores health"
    },
    {
        "item": "Mana Potion",
        "price": 15,
        "description": "Restores 10 mana points.",
        "effect": "restores mana"
    },
    {
        "item": "Gold Lump",
        "price": 5,
        "description": "A small lump of gold. Can be sold for profit.",
        "effect": None

    },
    {
        "item": "Rusty Dagger",
        "price": 20,
        "description": "A worn-out dagger that has seen better days. It is not very effective in combat, but can be used as a last resort.",
        "effect": None
    },
    {
        "item": "Goblin Ear",
        "price": 15,
        "description": "The ear of a goblin. It can be sold to merchants for a small profit.",
        "effect": None
    },
    {
        "item": "Bone Shard",
        "price": 25,
        "description": "A sharp fragment of bone. It can be used as a makeshift weapon or sold for profit.",
        "effect": None
    },
    {
        "item": "Iron Sword",
        "price": 50,
        "description": "A basic iron sword. It is more effective in combat than a rusty dagger, but still not very powerful.",
        "effect": None
    },
    {
        "item": "Skeleton Key",
        "price": 100,
        "description": "A key that can unlock any door. It is highly valuable and can be sold for a high price.",
        "effect": None
    },
    {
        "item": "Spider Silk",
        "price": 30,
        "description": "A strong and flexible material produced by spiders. It can be used to craft various items or sold for profit.",
        "effect": None
    },
    {
        "item": "Venom Sac",
        "price": 40,
        "description": "A sac filled with venom from a giant spider. It can be used to create poisons or sold for profit.",
        "effect": None
    },
    {
        "item": "Giant Spider Leg",
        "price": 35,
        "description": "The leg of a giant spider. It can be used as a weapon or sold for profit.",
        "effect": None
    },
    {
        "item": "Orcish Axe",
        "price": 75,
        "description": "A heavy axe used by orc warriors. It is powerful but unwieldy.",
        "effect": None
    },
    {
        "item": "Warrior's Helm",
        "price": 60,
        "description": "A sturdy helmet worn by warriors. It provides good protection in combat.",
        "effect": None
    },
    {
        "item": "Orcish Banner",
        "price": 150,
        "description": "A banner that represents the orc warlord's clan. It is highly valuable and can be sold for a high price.",
        "effect": None
    }

]