### QUESTS ###
# This module defines the quests that the player can undertake in the game. Each quest has a name, description, requirements, and rewards.
# Quests can be active, finished, failed, or inactive. Active quests are those that the player is currently undertaking, while finished quests are those that the player has completed successfully. Failed quests are those that the player has attempted but did not complete successfully, while inactive quests are those that the player has not yet undertaken or has abandoned.
# Only inactive quests are defined in this file, and they can be moved to the active quests list when the player starts them. The player's progress on each quest is tracked using the active, finished, and failed quests lists in the playerdata module.
# Each quest is represented as a dictionary with the following information:
# - name: The name of the quest.
# - id: A unique identifier for the quest, which can be used to track the player's progress and trigger certain events or dialogue when the player interacts with characters or locations related to the quest.
# - description: A brief description of the quest, including any relevant background information or story elements.
# - requirements: A list of any requirements that the player must meet in order to undertake the quest, such as having a certain level, possessing a specific item, or having completed a previous quest.
# - tasks: A list of any specific tasks or objectives that the player must complete in order to finish the quest. This can include things like defeating a certain enemy, collecting a certain item, or reaching a specific location.
# - rewards: A list of any rewards that the player will receive upon completing the quest, such as experience points, gold, items, or access to new locations or quests.

import playerdata

inactive_quests = [
    {
        "name": "The Missing Cat",
        "id": "the_missing_cat",
        "description": "Hormund has lost his beloved cat and is offering a reward for its safe return. The player must search the nearby area and find the cat, which may be hiding in a nearby location or may have been taken by a local enemy.",
        "requirements": [],
        "tasks": [], # code for tavern_basement being cleared, since the cat is likely hiding there
        "rewards": [
            {"type": "gold", "amount": 10},
            {"type": "experience", "amount": 50}
        ]
    },
    {
        "name": "The Haunted Basement",
        "id": "the_haunted_basement",
        "description": "The tavern basement is rumored to be haunted, and some say that strange noises can be heard coming from down there at night. Arlene is offering a reward for anyone who can investigate the basement and find out what is causing the disturbances.",
        "requirements": [],
        "tasks": [], # code for tavern_basement being cleared, since the disturbances are likely caused by the enemies in there
        "rewards": [
            {"type": "gold", "amount": 50},
            {"type": "experience", "amount": 100}
        ]
    },
    {
        "name": "The Orc Invasion",
        "id": "the_orc_invasion",
        "description": "The nearby forest is being invaded by a horde of orcs, and the local villagers are in desperate need of help. The player must venture into the forest and defeat the orc leader to stop the invasion and protect the village.",
        "requirements": [],
        "tasks": [], # code for orc_leader being defeated, since the invasion will likely stop after that
        "rewards": [
            {"type": "gold", "amount": 100},
            {"type": "experience", "amount": 200}
        ]
    }
]

def get_quest_by_id(quest_id, quest_list):
    for quest in quest_list:
        if quest["id"] == quest_id:
            return quest
    return None


def get_quest_by_name(quest_name, quest_list):
    for quest in quest_list:
        if quest["name"] == quest_name:
            return quest
    return None


def start_quest(quest_id):
    quest = get_quest_by_id(quest_id, inactive_quests)
    if quest is None:
        quest = get_quest_by_name(quest_id, inactive_quests)
    if quest is None:
        return False

    inactive_quests.remove(quest)
    playerdata.active_quests.append(quest)
    return True


def finish_quest(quest_id):
    quest = get_quest_by_id(quest_id, playerdata.active_quests)
    if quest is None:
        quest = get_quest_by_name(quest_id, playerdata.active_quests)
    if quest is None:
        return False

    playerdata.active_quests.remove(quest)
    playerdata.finished_quests.append(quest)
    reward_quest(quest)
    return True


def reward_quest(quest):
    for reward in quest.get("rewards", []):
        if reward["type"] == "gold":
            playerdata.player_data["gold"] += reward["amount"]
        elif reward["type"] == "experience":
            playerdata.player_data["experience"] += reward["amount"]