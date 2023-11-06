from game_data import races, classes


class Character:
    def __init__(self, name, race, character_class):
        self.name = name
        self.race = race
        self.character_class = character_class

    def __str__(self):
        return f"{self.name} the {self.race} {self.character_class}"

    @staticmethod
    def get_character_creation_input(prompt, choices):
        print(prompt)
        for idx, choice in enumerate(choices, 1):
            print(f"{idx}: {choice}")
        while True:
            selection = input("Choose an option: ")
            if selection.isdigit() and 1 <= int(selection) <= len(choices):
                return choices[int(selection) - 1]
            print("Invalid choice, please try again.")

    @classmethod
    def create_character(cls):
        print("\n--- Character Creation ---\n")
        name = input("What is your character's name? ")
        race = cls.get_character_creation_input("Choose your character's race:", races)
        character_class = cls.get_character_creation_input(
            "Choose your character's class:", classes
        )
        return cls(name, race, character_class)
