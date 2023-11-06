# Define ANSI escape codes for colored text
DM_COLOR = "\033[32m"
PLAYER_COLOR = "\033[33m"
RESET_COLOR = "\033[0m"


def print_colored(text, color):
    print(color + text + RESET_COLOR)
