# GPT-Driven Dungeons & Dragons Text Adventure

Embark on a text-based RPG adventure where the GPT-4 or GPT-3.5-turbo model from OpenAI takes the role of the Dungeon Master. This command-line experience fuses classic AD&D rules with modern AI capabilities to create a unique and dynamic storytelling adventure.

## Features

- Engaging text-based RPG gameplay.
- AI-driven Dungeon Master for dynamic storytelling.
- Character customization with name, race, and class choices.
- Randomized starting scenarios for varied gameplay.
- ANSI color-coded text for immersive player/DM interactions.
- Player choice of AI model at game start for tailored experiences.

## Latest Updates

### Version 0.5 (Date: 2023-11-06)

- Introduced character customization options at the beginning of the game.
- Added functionality for the player to select the AI model at startup.
- Implemented ANSI color codes for Dungeon Master and player text.
- Created a randomized starting scene feature to enhance gameplay variety.
- Various bug fixes and performance improvements.

## TODO

- **Web Accessible Frontend**: Develop a web-based interface to allow easy access from any browser.
- **Database Integration**: Implement a database system to persistently store player stats, history, adventure logs, and the current world state.
- **LangChain Integration**: Incorporate LangChain to enhance AI interactions, enabling more complex companion and NPC behaviors.
- **Whisper Integration**: Utilize OpenAI's Whisper model for accurate voice recognition, allowing voice commands and dictation as input.
- **DALL-E Integration**: Integrate with DALL-E to dynamically generate images of scenes, NPCs, and monsters to visually accompany the text-based adventure.


---

## Prerequisites

- Python 3.6 or later.
- OpenAI API key.

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/your-repository-name.git
cd your-repository-name
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Configure your OpenAI API key (replace `your_api_key` with your actual key):

```bash
export OPENAI_API_KEY='your_api_key'
```

## Usage

Run the game:

```bash
python main.py
```

Follow the prompts to select the AI model, create your character, and begin your journey!

---

## Gameplay

- Type commands and interact with the world as you would in traditional text-based RPGs.
- The AI Dungeon Master will guide you through the adventure with descriptions, NPC interactions, and the outcomes of your actions.
- Use 'quit' to safely exit the game.

## Contributing

Contributions are welcome! Feel free to fork the repository, make changes, and submit pull requests.

## Acknowledgements

- OpenAI for providing the API that powers this game's core functionality.
- The AD&D community for inspiring the gameplay mechanics.

Enjoy your quest, adventurer!

## License

---

MIT License

Copyright (c) 2023 Ken Newton

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Enjoy your quest, adventurer!