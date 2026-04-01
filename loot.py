## Loot
# Enemies and chests can drop loot. Loot items are represented as instances of the Item class.
# Each item has the following information:
# - name: The name of the item.
# - price: The price of the item in gold coins.
# - description: A brief description of the item, including any special properties or uses it may have.
# - effect: The effect of the item when used by the player (e.g. "restores health", "increases attack power", etc.).


class Item:
    """Represents a loot item that can be dropped by enemies or found in chests."""
    
    def __init__(self, name: str, price: int, description: str, effect: str = None):
        self.name = name
        self.price = price
        self.description = description
        self.effect = effect
    
    def __repr__(self):
        return f"Item(name='{self.name}', price={self.price})"
    
    def __str__(self):
        return self.name


# Loot table containing all available items
loot = [
    Item("Health Potion", 10, "Restores 20 health points.", "restores health"),
    Item("Mana Potion", 15, "Restores 10 mana points.", "restores mana"),
    Item("Gold Lump", 5, "A small lump of gold. Can be sold for profit."),
    Item("Rusty Dagger", 20, "A worn-out dagger that has seen better days. It is not very effective in combat, but can be used as a last resort."),
    Item("Goblin Ear", 15, "The ear of a goblin. It can be sold to merchants for a small profit."),
    Item("Rat Tail", 5, "The tail of a rat. It can be sold to merchants for a small profit."),
    Item("Rat Ear", 5, "The ear of a rat. It can be sold to merchants for a small profit."),
    Item("Rat Fur", 10, "The fur of a rat. It can be used to craft various items or sold for profit."),
    Item("Bone Shard", 25, "A sharp fragment of bone. It can be used as a makeshift weapon or sold for profit."),
    Item("Iron Sword", 50, "A basic iron sword. It is more effective in combat than a rusty dagger, but still not very powerful."),
    Item("Skeleton Key", 100, "A key that can unlock any door. It is highly valuable and can be sold for a high price."),
    Item("Spider Silk", 30, "A strong and flexible material produced by spiders. It can be used to craft various items or sold for profit."),
    Item("Venom Sac", 40, "A sac filled with venom from a giant spider. It can be used to create poisons or sold for profit."),
    Item("Giant Spider Leg", 35, "The leg of a giant spider. It can be used as a weapon or sold for profit."),
    Item("Orcish Axe", 75, "A heavy axe used by orc warriors. It is powerful but unwieldy."),
    Item("Warrior's Helm", 60, "A sturdy helmet worn by warriors. It provides good protection in combat."),
    Item("Orcish Banner", 150, "A banner that represents the orc warlord's clan. It is highly valuable and can be sold for a high price."),
]