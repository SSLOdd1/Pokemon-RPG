### QUESTS ###
# This module defines the quests that the player can undertake in the game. Each quest has a name, description, requirements, and rewards.
# Quests can be active, finished, failed, or inactive. Active quests are those that the player is currently undertaking, while finished quests are those that the player has completed successfully. Failed quests are those that the player has attempted but did not complete successfully, while inactive quests are those that the player has not yet undertaken or has abandoned.
# Each quest is represented as a dictionary with the following information:
# - name: The name of the quest.
# - description: A brief description of the quest, including any relevant background information or story elements.
# - requirements: A list of any requirements that the player must meet in order to undertake the quest, such as having a certain level, possessing a specific item, or having completed a previous quest.
# - rewards: A list of any rewards that the player will receive upon completing the quest, such as experience points, gold, items, or access to new locations or quests.

active_quests = []

finished_quests = []

failed_quests = []

inactive_quests = [
    {
        "name": "The Missing Cat",
        "description": "Hormund has lost his beloved cat and is offering a reward for its safe return. The player must search the nearby area and find the cat, which may be hiding in a nearby location or may have been taken by a local enemy.",
        "requirements": [], # code for tavern_basement being cleared, since the cat is likely hiding there
        "rewards": [
            {"type": "gold", "amount": 10},
            {"type": "experience", "amount": 50}
        ]
    },
    {
        "name": "The Haunted Basement",
        "description": "The tavern basement is rumored to be haunted, and some say that strange noises can be heard coming from down there at night. Arlene is offering a reward for anyone who can investigate the basement and find out what is causing the disturbances.",
        "requirements": [], # code for tavern_basement being cleared, since the disturbances are likely caused by the enemies in there
        "rewards": [
            {"type": "gold", "amount": 50},
            {"type": "experience", "amount": 100}
        ]
    }
]