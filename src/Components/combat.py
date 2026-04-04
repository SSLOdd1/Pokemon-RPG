import random

import enemies
import playerdata


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

def combat_loop(enemy):
    print("Combat loop started.")

    # No attack actions exist yet, so HP values currently do not change during each round.
    while playerdata.player_data.get("health", 0) > 0 and enemy.get("current_health", 0) > 0:
        print(
            f"[Combat Tick] Player HP: {playerdata.player_data.get('health', 0)} | "
            f"{enemy.get('name', 'Enemy')} HP: {enemy.get('current_health', 0)}"
        )
        input("Press Enter to continue combat... ")

    if playerdata.player_data.get("health", 0) <= 0:
        print("You were defeated.")
    elif enemy.get("current_health", 0) <= 0:
        print(f"You defeated {enemy.get('name', 'the enemy')}!")