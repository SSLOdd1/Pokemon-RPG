import copy

ENEMIES = {
    "goblin": {
        "id": "goblin",
        "name": "Goblin",
        "health": 30,
        "attack": 5,
        "defense": 2,
        "type": "normal",
        "special_effects": [],
        "experience": 25,
        "loot": [
            {"item": "Gold Lump", "probability": 0.5},
            {"item": "Rusty Dagger", "probability": 0.3},
            {"item": "Goblin Ear", "probability": 0.2},
        ],
    },
    "giant_spider": {
        "id": "giant_spider",
        "name": "Giant Spider",
        "health": 40,
        "attack": 8,
        "defense": 3,
        "type": "poisonous",
        "special_effects": ["poison_on_hit"],
        "experience": 75,
        "loot": [
            {"item": "Spider Silk", "probability": 0.5},
            {"item": "Venom Sac", "probability": 0.3},
            {"item": "Giant Spider Leg", "probability": 0.2},
        ],
    },
    "rat": {
        "id": "rat",
        "name": "Giant Rat",
        "health": 20,
        "attack": 3,
        "defense": 1,
        "type": "normal",
        "special_effects": [],
        "experience": 10,
        "loot": [
            {"item": "Rat Tail", "probability": 0.5},
            {"item": "Cheese", "probability": 0.3},
            {"item": "Gold Lump", "probability": 0.2},
        ],
    },
}

def get_enemy_by_id(enemy_id):
    return ENEMIES.get(enemy_id)

def create_enemy_instance(enemy_id):
    template = get_enemy_by_id(enemy_id)
    if template is None:
        return None

    instance = copy.deepcopy(template)
    instance["current_health"] = template["health"]
    instance["status_effects"] = []
    return instance