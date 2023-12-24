# ------------------------------------------------------------- #
# Generateur de texte aleatoire version 2 ( sans module faker ) #
# ------------------------------------------------------------- #
import json
import random

from pathlib import Path

database = Path(__file__).parent / "data" / "database.json"

with open(database, "r") as file:
    game_data = json.load(file)


def get_game_text():
    return random.choice(game_data)