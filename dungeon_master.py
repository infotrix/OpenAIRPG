import openai


class DungeonMaster:
    def __init__(self, model):
        self.model = model

    @staticmethod
    def choose_model():
        print("Choose your AI Dungeon Master:")
        print("1: GPT-4")
        print("2: GPT-3.5-turbo")
        model_choice = input("Select an option (1 or 2): ")
        return "gpt-4" if model_choice != "2" else "gpt-3.5-turbo"

    def chat(self, user_input, game_history, character):
        # Include the character information in the user's message history
        user_message = {
            "role": "user",
            "content": f"{character.name} ({character.race} {character.character_class}): {user_input}",
        }
        try:
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=game_history + [user_message],
            )
            return response.choices[0].message["content"].strip()
        except openai.error.OpenAIError as e:
            print(f"An error occurred: {e}")
            return None
