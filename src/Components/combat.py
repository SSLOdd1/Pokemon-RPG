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
    combat_loop(enemy)


def start_fight(location):
    enemy = choose_enemy_for_location(location)
    if enemy is None:
        print("There are no valid enemies here.")
        return

    print(f"You encounter a {enemy['name']}!")
    begin_combat(enemy)

def resolve_attack(target, attack):
    damage = attack.get("damage", 0)
    accuracy = attack.get("accuracy", 1.0)
    defense = target.get("defense", 0)
    damage_dealt = max(0, damage - defense) * (1 if random.random() <= accuracy else 0)
    target["current_health"] = max(0, target.get("current_health", 0) - damage_dealt)
    print(f"You use {attack['name']} against {target.get('name', 'the enemy')}, doing {damage_dealt} damage!")

def defeat():
    print("You have been defeated.")
    # Will later add option to respawn at nearest village, at the cost of some gold, or to load from a player home, costing no gold.

def victory(enemy):
    print(f"You defeated {enemy.get('name', 'the enemy')}!")
    # Will later add experience gain, loot drops, and potential quest progression here.


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
                continue
            else:
                selected_attack = available_attacks[int(choice) - 1]
                resolve_attack(enemy, selected_attack)
            # Resolve damage round and apply any special effects, updating player and enemy health accordingly.


    if playerdata.player_data.get("health", 0) <= 0:
        defeat()
    elif enemy.get("current_health", 0) <= 0:
        victory(enemy)

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