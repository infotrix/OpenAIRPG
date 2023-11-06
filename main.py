import os
import random
import openai
from game_data import starting_scenes
from character import Character
from dungeon_master import DungeonMaster
from utils import print_colored, DM_COLOR, PLAYER_COLOR, RESET_COLOR

# Set up the OpenAI key
openai.api_key = os.getenv("OPENAI_API_KEY")


def main():
    print("Welcome to the GPT Dungeons & Dragons Adventure!")

    # AI model selection
    model = DungeonMaster.choose_model()

    # Character creation
    character = Character.create_character()

    # System message for the AI Dungeon Master with the character context
    system_message = {
        "role": "system",
        "content": (
            f"You are a knowledgeable and fair Dungeon Master in a game of Advanced Dungeons & Dragons. "
            f"The player's character is {character.name}, a {character.race} {character.character_class}. "
            "Provide detailed descriptions, answer the player’s actions with narrative outcomes, manage combat encounters, "
            "and facilitate dialogue with characters in the world. Simulate dice rolls and maintain the fantasy setting for an engaging game experience."
        ),
    }

    print(f"\nWelcome, {character}! Your adventure awaits!\n")
    print("Type 'quit' to exit.\n")

    # Initialize game history with the system message
    game_history = [system_message]

    # Randomize starting scenario
    if starting_scenes:
        starting_scene = random.choice(starting_scenes)
    else:
        starting_scene = f"{character.name} finds themselves in a place beyond time and space, seeking a path to adventure."

    # Add the starting scene to the game history
    game_history.append({"role": "assistant", "content": starting_scene})

    # Main game loop
    dm = DungeonMaster(model)
    while True:
        print_colored("Dungeon Master: " + game_history[-1]["content"], DM_COLOR)

        player_input = input(PLAYER_COLOR + f"{character.name}: " + RESET_COLOR)
        if player_input.lower() == "quit":
            print("Farewell, adventurer!")
            break

        dm_response = dm.chat(player_input, game_history, character)
        if dm_response:
            print_colored("Dungeon Master: " + dm_response, DM_COLOR)
            game_history.append({"role": "user", "content": player_input})
            game_history.append({"role": "assistant", "content": dm_response})

            # Truncate history to keep it manageable
            if len(game_history) > 20:
                game_history = game_history[-20:]

        # Placeholder for Eleven Labs integration or other audio output features


if __name__ == "__main__":
    main()
