### DIALOGUE ###
# This file contains the dialogue for the characters in the game. Each character has a list of dialogue lines that they can say when interacted with. The dialogue lines can be used to provide information about the character, their backstory, or to give hints about quests and other game mechanics.
# Each dialogue line is represented as a string, and may include placeholders for dynamic information such as the player's name or current location. The dialogue lines can also be triggered by certain conditions, such as the player having completed a specific quest or having a certain item in their inventory.
# Each line is structured as a dictionary with the following information:
# - text: The actual dialogue line that the character will say.
# - conditions: A list of any conditions that must be met for the character to say this line. This can include things like the player's current location, quests completed, items in inventory, etc. May be blank if there are no conditions.
# - responses: A list of any responses that the player can choose from after the character says this line. Each response is a dictionary with the following information:
#   - text: The text of the player's response.
#   - requirements: A list of any requirements that must be met for the player to choose this response. This can include things like the player's current location, quests completed, items in inventory, etc. May be blank if there are no requirements.
#   - effects: A list of any effects that will occur when the player chooses this response. This can include things like starting a quest, giving the player an item, changing the player's stats, etc. May be blank if there are no effects.

Hormond_dialogue = [
    {
        "id": "Hormond_greeting",
        "text": "Have you seen my cat? His name is Whiskers and he's very dear to me. I last saw him around the tavern, but I haven't been able to find him since.",
        "conditions": [lambda finished_quests: "The Missing Cat" not in finished_quests],
        "responses": [
            {
                "text": "I haven't seen your cat, but I'll keep an eye out for him.",
                "requirements": [],
                "effects": {"type": "exit_dialogue"}
            },
            {
                "text": "I think I saw a cat in the tavern basement. Maybe I'll check there.",
                "requirements": [],
                "effects": [
                    {"type": "start_quest", "quest_name": "The Missing Cat"}
                ]
            }
        ]
    },
    {
        "id": "Hormond_quest_complete",
        "text": "Thanks for looking out for Whiskers. He's really important to me.",
        "conditions": [lambda finished_quests: "The Missing Cat" in finished_quests],
        "responses": [
            {
                "text": "No problem, I hope he's safe and happy.",
                "requirements": [],
                "effects": {"type": "exit_dialogue"}
            }
        ]
    },
    {
        "text": "Welcome to my forge! I can craft powerful weapons and armor for you, using materials that you provide.",
        "conditions": [],
        "responses": [
            {
                "text": "I'd like to craft some weapons.",
                "requirements": [],
                "effects": [
                    {"type": "open_crafting", "crafting_type": "weapons"}
                ]
            },
            {
                "text": "I'd like to craft some armor.",
                "requirements": [],
                "effects": [
                    {"type": "open_crafting", "crafting_type": "armor"}
                ]
            },
            {
                "text": "No thanks, just browsing.",
                "requirements": [],
                "effects": {"type": "exit_dialogue"}

            }
        ]

    }
]

Erlhe_dialogue = [
    {
        "id": "Erhle_greeting",
        "text": "Welcome to my shop! I have a variety of goods for sale, including potions, scrolls, and rare items. Is there anything you're looking for?",
        "conditions": [],
        "responses": [
            {
                "text": "What do you have for sale?",
                "requirements": [],
                "effects": [
                    {"type": "open_shop", "shop_name": "Erhle's General Store"}
                ]
            },
            {
                "text": "No thanks, just browsing.",
                "requirements": [],
                "effects": {"type": "exit_dialogue"}
            }
        ]
    }
]

Arlene_dialogue = [
    {
        "id": "Arlene_greeting",
        "text": "Welcome to my tavern! I can provide you with food, drink, and a place to rest. I also have some information about local rumors and quests if you're interested.",
        "conditions": [],
        "responses": [
            {
                "text": "I'd like to see what you have for sale.",
                "requirements": [],
                "effects": [
                    {"type": "open_shop", "shop_name": "Arlene's Tavern"}
                ],
                "next_id": "shop_response"
            },
            {
                "text": "Do you have any information about local rumors or quests?",
                "requirements": [],
                "effects": [
                    {"type": "provide_information", "information_type": "rumors_and_quests"}
                ],
                "next_id": "Arlene_quest_offer"
            },
            {
                "text": "No thanks, just browsing.",
                "requirements": [],
                "effects": {"type": "exit_dialogue"}
            }
        ]
    },
    {
        "id": "Arlene_no_quests",
        "text": "Sorry, I don't have any quests for you right now. But feel free to check back later, as I might have some new quests for you in the future.",
        "conditions": [lambda finished_quests, active_quests: "The Haunted Basement" in finished_quests or "The Haunted Basement" in active_quests],
        "responses": [
            {
                "text": "I'll check back later.",
                "requirements": [],
                "effects": {"type": "exit_dialogue"}
            }
        ]
    },
    {
        "id": "Arlene_quest_offer",

        "text": "Actually, I do have a quest for you. There's been some trouble with noises in the basement. If you could take care of them, I'd really appreciate it.",
        "conditions": [
            lambda ctx: "the_haunted_basement" not in ctx["active_quest_ids"]
                and "the_haunted_basement" not in ctx["finished_quest_ids"]
        ],
        "responses": [
            {
                "text": "Sure, I'll check out the basement.",
                "requirements": [],
                "effects": [
                    {"type": "start_quest", "quest_name": "The Haunted Basement"}
                ],
                "next_id": "Arlene_quest_accepted"
            },
            {
                "text": "No thanks, I'm not interested in that quest.",
                "requirements": [],
                "effects": {"type": "exit_dialogue"}
            }
        ]
    },
    {
        "id": "Arlene_quest_accepted",
        "text": "Thanks so much! I hope you can figure out what's going on down there.",
        "conditions": [],
        "responses": [
            {
                "text": "I'll do my best!",
                "requirements": [],
                "effects": {"type": "exit_dialogue"}
            }
        ]
    },
    {
        "id": "Arlene_quest_complete",
        "text": "Thanks for taking care of the noises in the basement. I was getting really worried about it.",
        "conditions": [lambda finished_quests: "The Haunted Basement" in finished_quests],
        "responses": [
            {
                "text": "I'm glad I could help!",
                "requirements": [],
                "effects": {"type": "exit_dialogue"}
            }
        ]
    }
]

Gwen_dialogue = [
    {
        "id": "Gwen_greeting",
        "text": "Welcome to the royal palace! As the ruler of Greenwood Village, I'm always looking for brave adventurers to help with quests related to the safety and prosperity of our village. Is there anything I can assist you with?",
        "conditions": [],
        "responses": [
            {
                "text": "Do you have any quests for me?",
                "requirements": [],
                "effects": [
                    {"type": "provide_information", "information_type": "available_quests"}
                ]
            },
            {
                "text": "No thanks, just browsing.",
                "requirements": [],
                "effects": {"type": "exit_dialogue"}
            }
        ]
    }
]


# Central registry used by main.py to look up dialogue by character dialogue_id.
dialogue_data = {
    "Hormond_dialogue": Hormond_dialogue,
    "Erhle_dialogue": Erlhe_dialogue,
    "Arlene_dialogue": Arlene_dialogue,
    "Gwen_dialogue": Gwen_dialogue,
}