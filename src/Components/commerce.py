### COMMERCE ###
# This module defines the commerce system in the game, which allows players to buy and sell items with NPCs. The commerce system includes a list of items that can be bought and sold, as well as the prices for each item. The player can interact with NPCs to access the commerce system and make transactions.
# Each NPC that offers commerce will have a list of items that they sell, along with their prices. The player can choose to buy or sell items, and the prices will be determined by the NPC's inventory and the player's current gold. The commerce system will also include any special interactions or discounts that may apply to certain items or NPCs.
# The commerce system will be integrated with the player's inventory and gold, allowing the player to manage their resources and make informed decisions about their purchases and sales. The player can also use the commerce system to acquire rare or powerful items that may not be available through other means, such as looting or crafting.

import playerdata

def list_items_for_sale(shop_id):
    """Returns a list of items for the given shop id."""
    shop = SHOPS.get(shop_id)
    if not shop:
        return []
    return shop.get("items_for_sale", [])

def handle_shop(shop_id):
    """Handles the shopping interaction with the given shop ID."""
    while True:
        items = list_items_for_sale(shop_id)
        if not items:
            print("This shop has nothing for sale.")
            return

        print("Items for sale:")
        for index, item in enumerate(items, 1):
            print(f"{index}. {item['name']} - {item['price']} gold")

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

        success, message = buy_item(shop_id, selected_item["name"], qty)
        print(message)

def _add_item_to_backpack(item_name, qty):
    loot_bag = playerdata.inventory["backpack"].setdefault("loot", {})
    loot_bag[item_name] = loot_bag.get(item_name, 0) + qty


def buy_item(shop_id, item_name, qty=1):
    """Allows the player to buy an item from the given shop id."""
    items_for_sale = list_items_for_sale(shop_id)
    for item in items_for_sale:
        if item["name"] == item_name:
            total_price = item["price"] * qty
            player_gold = playerdata.player_data.get("gold", 0)
            if player_gold >= total_price:
                playerdata.player_data["gold"] = player_gold - total_price
                _add_item_to_backpack(item_name, qty)
                return True, f"You bought {qty}x {item_name} for {total_price} gold."

            return False, "You do not have enough gold."
    return False, "That item is not sold here."

def sell_item(item_name, qty=1):
    """Allows the player to sell an item to the given NPC, if they have it in their inventory."""
    loot_bag = playerdata.inventory["backpack"].setdefault("loot", {})
    current_qty = loot_bag.get(item_name, 0)
    if current_qty < qty:
        return False, "You do not have enough of that item to sell."

    sell_price_per_item = 1
    total_price = sell_price_per_item * qty

    loot_bag[item_name] = current_qty - qty
    if loot_bag[item_name] <= 0:
        del loot_bag[item_name]

    playerdata.player_data["gold"] = playerdata.player_data.get("gold", 0) + total_price
    return True, f"You sold {qty}x {item_name} for {total_price} gold."

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


SHOPS = {
    "Arlene_tavern_shop": Arlene_tavern_shop,
    "Hormond_blacksmith_shop": Hormond_blacksmith_shop,
    "Erhle_general_store_shop": Erhle_general_store_shop,
}