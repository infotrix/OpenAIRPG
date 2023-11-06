import os
import openai
import random

# import elebvenlabs
# import elevenlabs

openai.api_key = os.getenv("OPENAI_API_KEY")
# ANSI escape codes for colors
DM_COLOR = "\033[32m"  # Blue color for the Dungeon Master
PLAYER_COLOR = "\033[33m"  # Green color for the player
RESET_COLOR = "\033[0m"  # Reset to default terminal color


def print_colored(text, color):
    print(color + text + RESET_COLOR)


system_message = {
    "role": "system",
    "content": (
        "You are a knowledgeable and fair Dungeon Master in a game of Advanced Dungeons & Dragons. "
        "You are familiar with all the rules, which you enforce consistently, but you also value the fun "
        "and creativity of the players. Provide detailed descriptions, answer the player’s actions with "
        "narrative outcomes, manage combat encounters, and facilitate dialogue with characters in the world. "
        "You can create and describe new characters, settings, and items on the fly. Keep track of the player's "
        "stats and inventory. When dice rolls are necessary, you'll simulate the outcome. Do not make real-world references "
        "and maintain the fantasy setting. Your goal is to create an engaging and dynamic story while ensuring a "
        "balanced and enjoyable game experience."
    ),
}


def chat_with_gpt4_dungeon_master(user_input, game_history, model):
    try:
        response = openai.ChatCompletion.create(
            model=model,  # Dynamically selected model
            messages=game_history + [{"role": "user", "content": user_input}],
        )
        return response.choices[0].message["content"].strip()
    except openai.error.OpenAIError as e:
        print(f"An error occurred: {e}")
        return None


# Possible races and classes from AD&D
races = ["Human", "Elf", "Dwarf", "Halfling", "Gnome", "Half-Elf", "Half-Orc"]
classes = [
    "Fighter",
    "Wizard",
    "Cleric",
    "Rogue",
    "Paladin",
    "Ranger",
    "Druid",
    "Monk",
    "Bard",
]


def get_character_creation_input(prompt, choices):
    print(prompt)
    for idx, choice in enumerate(choices, 1):
        print(f"{idx}: {choice}")
    while True:
        selection = input("Choose an option: ")
        if selection.isdigit() and 1 <= int(selection) <= len(choices):
            return choices[int(selection) - 1]
        print("Invalid choice, please try again.")


def dnd_game_loop():
    print("Welcome to the GPT Dungeons & Dragons Adventure!")

    # AI model selection
    print("Choose your AI Dungeon Master:")
    print("1: GPT-4")
    print("2: GPT-3.5-turbo")
    model_choice = input("Select an option (1 or 2): ")
    model = "gpt-4" if model_choice != "2" else "gpt-3.5-turbo"

    # Character creation
    print("\n--- Character Creation ---\n")
    character_name = input("What is your character's name? ")

    character_race = get_character_creation_input(
        "Choose your character's race:", races
    )
    character_class = get_character_creation_input(
        "Choose your character's class:", classes
    )

    print(
        f"\nWelcome, {character_name} the {character_race} {character_class}! Your adventure awaits!\n"
    )
    print("Type 'quit' to exit.\n")

    # List of starting scenes
    starting_scenes = [
        "You find yourself in a dimly lit tavern. Patrons quietly converse around you. What will you do?",
        "You wake up in a dark, damp dungeon cell. Your head is throbbing and you can't remember how you got here.",
        "You stand at the edge of a bustling market, the shouts of vendors and the smell of fresh goods fill the air.",
        "You are at the gates of a majestic city, guards eye you suspiciously as they patrol the walls.",
        "You are in a dense forest, the canopy above barely letting any light through. The path forward is unclear.",
    ]

    starting_scene = random.choice(starting_scenes)
    game_history = [system_message, {"role": "assistant", "content": starting_scene}]

    # Ensure that the selected model is passed to the chat function
    while True:
        print_colored("Dungeon Master: " + game_history[-1]["content"], DM_COLOR)

        player_input = input(PLAYER_COLOR + "You: " + RESET_COLOR)
        if player_input.lower() == "quit":
            print("Farewell, adventurer!")
            break

        dm_response = chat_with_gpt4_dungeon_master(
            player_input, game_history, model
        )  # Pass the selected model here
        if dm_response:
            print_colored("Dungeon Master: " + dm_response, DM_COLOR)
            game_history.append({"role": "user", "content": player_input})
            game_history.append({"role": "assistant", "content": dm_response})

            if len(game_history) > 20:
                game_history = game_history[-20:]
        # Eleven labs reading (will max out quickly on free tier)
        # audio = elevenlabs.generate(game_history[-1])
        # elevenlabs.play(audio)


if __name__ == "__main__":
    dnd_game_loop()
