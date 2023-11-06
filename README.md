# GPT-Driven Dungeons & Dragons Text Adventure

Dive into a text-based RPG where the GPT-4 or GPT-3.5-turbo model from OpenAI becomes your Dungeon Master. This terminal game blends the essence of classic Dungeons & Dragons with cutting-edge AI to deliver a personalized storytelling experience.

## Features

- Text-based RPG gameplay with an AI Dungeon Master.
- Customizable characters with name, race, and class options.
- Unique starting scenarios for each new game.
- Colored text output for enhanced readability and immersion.
- Selection between GPT-4 and GPT-3.5-turbo at game start.
- Simple command-line interface with support for custom player names.

## Latest Updates

### Version 0.6 (Date: 2023-11-06)

- Refactored codebase for improved readability and maintainability.
- Integrated player name personalization within AI Dungeon Master responses.
- Resolved issues with circular imports and incorrect parameter passing.
- Updated README to reflect new changes and instructions for players.
- Fixed bugs reported in the previous version related to character creation.

## Upcoming Features

- **Interactive Web Interface**: Implementing a web front-end for browser-based access.
- **Persistent Game State**: Introducing a database to save player progress and game state.
- **Enhanced AI Interactions**: Integrating LangChain for richer NPC and game world dynamics.
- **Voice Command Capability**: Adding OpenAI's Whisper for voice-to-text input during gameplay.
- **Visual Elements**: Planning to use DALL-E for generating images to visually represent game scenes.

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