import random

import enemies
import playerdata
import attacks


def choose_enemy_for_location(location):
    encounter_table = []
    weights = []

    for entry in location.enemies:
        enemy_id = entry.get("enemy_id") if isinstance(entry, dict) else None
        weight = entry.get("weight", 1.0) if isinstance(entry, dict) else 1.0

        if not enemy_id:
            continue

        enemy_instance = enemies.create_enemy_instance(enemy_id)
        if enemy_instance is None:
            continue

        encounter_table.append(enemy_instance)
        weights.append(weight)

    if not encounter_table:
        return None

    return random.choices(encounter_table, weights=weights)[0]


def _resolve_player_effects():
    effects = []
    skills = playerdata.player_data.get("skills", [])
    if isinstance(skills, list):
        effects.extend([f"Skill: {skill}" for skill in skills if skill])

    equipped = playerdata.inventory.get("equipped", {})
    for slot in ("weapon", "armor"):
        item = equipped.get(slot)
        if isinstance(item, dict) and item.get("effect"):
            effects.append(f"{slot.capitalize()} effect: {item['effect']}")

    accessories = equipped.get("accessories", {})
    for slot_name, accessory in accessories.items():
        if isinstance(accessory, dict) and accessory.get("effect"):
            effects.append(f"{slot_name} effect: {accessory['effect']}")

    return effects


def begin_combat(enemy):
    player_name = playerdata.player_data.get("name", "Player")
    player_health = playerdata.player_data.get("health", "Unknown")
    player_effects = _resolve_player_effects()

    enemy_name = enemy.get("name", "Unknown Enemy")
    enemy_health = enemy.get("current_health", enemy.get("health", "Unknown"))
    enemy_effects = enemy.get("special_effects", [])

    print("\n=== Combat Begins ===")
    print(f"Player: {player_name}")
    print(f"Health: {player_health}")
    print(f"Special Effects: {', '.join(player_effects) if player_effects else 'None'}")
    print("")
    print(f"Enemy: {enemy_name}")
    print(f"Health: {enemy_health}")
    print(f"Special Effects: {', '.join(enemy_effects) if enemy_effects else 'None'}")
    return combat_loop(enemy)


def start_fight(location):
    enemy = choose_enemy_for_location(location)
    if enemy is None:
        print("There are no valid enemies here.")
        return None

    print(f"You encounter a {enemy['name']}!")
    return begin_combat(enemy)

def resolve_attack(target, attack):
    damage = attack.get("damage", 0)
    accuracy = attack.get("accuracy", 1.0)
    defense = target.get("defense", 0)
    hit = random.random() <= accuracy
    damage_dealt = max(0, damage - defense) if hit else 0
    target["current_health"] = max(0, target.get("current_health", 0) - damage_dealt)
    print(f"You use {attack['name']} against {target.get('name', 'the enemy')}, doing {damage_dealt} damage!")
    if not hit:
        print("The attack missed!")


def resolve_enemy_attack(enemy):
    enemy_name = enemy.get("name", "Enemy")
    damage = enemy.get("attack", 0)
    accuracy = enemy.get("accuracy", 0.9)
    player_defense = playerdata.player_data.get("defense", 0)

    hit = random.random() <= accuracy
    damage_dealt = max(0, damage - player_defense) if hit else 0

    playerdata.player_data["health"] = max(
        0,
        playerdata.player_data.get("health", 0) - damage_dealt,
    )

    print(f"{enemy_name} attacks you for {damage_dealt} damage!")
    if not hit:
        print(f"{enemy_name}'s attack missed!")


def grant_enemy_loot(enemy):
    loot_table = enemy.get("loot", []) if isinstance(enemy, dict) else []

    backpack_loot = playerdata.inventory.setdefault("backpack", {}).setdefault("loot", {})

    # Normalize older loot-entry formats to integer quantities.
    for item_name, entry in list(backpack_loot.items()):
        if isinstance(entry, dict):
            backpack_loot[item_name] = max(0, int(entry.get("quantity", 0)))

    if not loot_table:
        return []

    dropped_items = []
    for entry in loot_table:
        if not isinstance(entry, dict):
            continue

        item_name = entry.get("item")
        probability = entry.get("probability", 0.0)
        if not item_name:
            continue

        if random.random() <= max(0.0, min(1.0, probability)):
            dropped_items.append(item_name)

    if not dropped_items:
        return []

    for item_name in dropped_items:
        current_qty = backpack_loot.get(item_name, 0)
        if isinstance(current_qty, dict):
            current_qty = int(current_qty.get("quantity", 0))
        backpack_loot[item_name] = max(0, int(current_qty)) + 1

    return dropped_items

def defeat():
    print("You have been defeated.")

    current_gold = max(0, int(playerdata.player_data.get("gold", 0)))
    gold_penalty = max(1, current_gold // 10) if current_gold > 0 else 0
    playerdata.player_data["gold"] = max(0, current_gold - gold_penalty)

    max_health = max(1, int(playerdata.player_data.get("max_health", 100)))
    respawn_health = max(1, max_health // 2)
    playerdata.player_data["health"] = respawn_health

    if gold_penalty > 0:
        print(f"You pay {gold_penalty} gold for emergency recovery.")
    print(f"You recover and respawn with {respawn_health} health.")

def victory(enemy):
    print(f"You defeated {enemy.get('name', 'the enemy')}!")
    dropped_items = grant_enemy_loot(enemy)
    if dropped_items:
        print(f"Loot dropped: {', '.join(dropped_items)}")
    else:
        print("No loot dropped this time.")
    # Will later add potential quest progression here.
    exp_gained = enemy.get("experience", 0)
    if exp_gained > 0:
        print(f"You gain {exp_gained} experience points!")
        # Placeholder for adding experience to player data and handling level-ups.

def combat_loop(enemy):
    print("Combat loop started.")

    # No attack actions exist yet, so HP values currently do not change during each round.
    while playerdata.player_data.get("health", 0) > 0 and enemy.get("current_health", 0) > 0:
        print(
            f"[Combat Tick] Player HP: {playerdata.player_data.get('health', 0)} | "
            f"{enemy.get('name', 'Enemy')} HP: {enemy.get('current_health', 0)}"
        )
        available_attacks = get_available_attacks()
        if not available_attacks:
            print("You have no attacks available! You can only defend or try to flee.")
            # Placeholder for defend and flee options.
        else:
            print("Available Attacks:")
            for idx, attack in enumerate(available_attacks, start=1):
                print(f"{idx}. {attack['name']} - {attack['description']} (Damage: {attack['damage']}, Accuracy: {int(attack['accuracy'] * 100)}%)")
            choice = input("Choose an attack by entering the corresponding number: ").strip()
            if not choice.isdigit() or not (1 <= int(choice) <= len(available_attacks)):
                print("Invalid choice.")
            else:
                selected_attack = available_attacks[int(choice) - 1]
                resolve_attack(enemy, selected_attack)
            # Resolve damage round and apply any special effects, updating player and enemy health accordingly.

        if playerdata.player_data.get("health", 0) > 0 and enemy.get("current_health", 0) > 0:
            resolve_enemy_attack(enemy)


    if playerdata.player_data.get("health", 0) <= 0:
        defeat()
        return "defeat"
    elif enemy.get("current_health", 0) <= 0:
        victory(enemy)
        return "victory"

    return None

def get_available_attacks():
    equipped_weapon = playerdata.inventory.get("equipped", {}).get("weapon")

    weapon_name = None
    if isinstance(equipped_weapon, str):
        weapon_name = equipped_weapon
    elif isinstance(equipped_weapon, dict):
        weapon_name = equipped_weapon.get("name")

    if weapon_name and weapon_name in attacks.player_attacks:
        return attacks.player_attacks[weapon_name]

    return attacks.player_attacks.get("Unarmed", [])