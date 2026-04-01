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

inactive_quests = []