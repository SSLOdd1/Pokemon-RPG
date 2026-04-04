### COMMERCE ###
# This module defines the commerce system in the game, which allows players to buy and sell items with NPCs. The commerce system includes a list of items that can be bought and sold, as well as the prices for each item. The player can interact with NPCs to access the commerce system and make transactions.
# Each NPC that offers commerce will have a list of items that they sell, along with their prices. The player can choose to buy or sell items, and the prices will be determined by the NPC's inventory and the player's current gold. The commerce system will also include any special interactions or discounts that may apply to certain items or NPCs.
# The commerce system will be integrated with the player's inventory and gold, allowing the player to manage their resources and make informed decisions about their purchases and sales. The player can also use the commerce system to acquire rare or powerful items that may not be available through other means, such as looting or crafting.

def list_items_for_sale(npc):
    """Returns a list of items that the given NPC has for sale, along with their prices."""
    return npc.get("interactions", {}).get("commerce", {}).get("items_for_sale", [])

def handle_shop(shop_id):
    """Handles the shopping interaction with the given shop ID."""
    while True:
        items = list_items_for_sale(shop_id)  # should return list of item dicts
        if not items:
            print("This shop has nothing for sale.")
            return

        print("0. Leave shop")
        choice = input("> ").strip()

        if choice == "0":
            return

        if not choice.isdigit() or not (1 <= int(choice) <= len(items)):
            print("Invalid choice.")
            continue

        selected_item = items[int(choice) - 1]

        qty_input = input("How many? (default 1) > ").strip()
        qty = int(qty_input) if qty_input.isdigit() and int(qty_input) > 0 else 1

        success, message = buy_item(selected_item, qty)
        print(message)

def buy_item(npc, item_name, player_gold):
    """Allows the player to buy an item from the given NPC, if they have enough gold."""
    items_for_sale = list_items_for_sale(npc)
    for item in items_for_sale:
        if item["name"] == item_name:
            price = item["price"]
            if player_gold >= price:
                player_gold -= price
                print(f"You bought {item_name} for {price} gold.")
                playerdata.player_data["gold"] = player_gold  # Update player's gold
                playerdata.inventory["backpack"].append(item)  # Add item to player's inventory
                return item  # Return the item to indicate a successful purchase

            else:
                return None  # Not enough gold
    return None  # Item not found

def sell_item(npc, item_name, player_inventory):
    """Allows the player to sell an item to the given NPC, if they have it in their inventory."""
    for item in player_inventory:
        if item["name"] == item_name:
            price = item.get("sell_price", 0)
            return price  # Return the price to indicate a successful sale
    return None  # Item not found in inventory

Arlene_tavern_shop = {
    "items_for_sale": [
        {"name": "Bread", "price": 5},
        {"name": "Ale", "price": 10},
        {"name": "Stew", "price": 15}
    ]
}

Hormond_blacksmith_shop = {
    "items_for_sale": [
        {"name": "Wooden Sword", "price": 20},
        {"name": "Iron Sword", "price": 50},
        {"name": "Steel Sword", "price": 100},
        {"name": "Leather Armor", "price": 30},
        {"name": "Chainmail Armor", "price": 70},
        {"name": "Plate Armor", "price": 150}
    ]
}

Erhle_general_store_shop = {
    "items_for_sale": [
        {"name": "Health Potion", "price": 25}
    ]
}