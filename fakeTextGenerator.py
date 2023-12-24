# ----------------------------------------------------- #
# Generateur de texte aleatoire ( en utilisant 'faker') #
# ----------------------------------------------------- #
import faker
import json
from pathlib import Path

database = Path(__file__).parent / "database.json"

database.touch(exist_ok=True)


# ---------------------------------------------------------------------- #
# une Fonction qui retourne une liste des mots du premier phrase du text #
# ---------------------------------------------------------------------- #
def get_random_word_list(text):
    return [word for word in text.split('.')[0].split() if word]


# -------------------------------------------------- #
# une Fonction qui renvoie une phrase de 7 a 10 mots #
# -------------------------------------------------- #
def get_game_text():
    # Creation d'un Objet Faker
    fake = faker.Faker()

    text_ = get_random_word_list(fake.text())

    while not (7 <= len(text_) <= 10):
        text_ = get_random_word_list(fake.text())

    return " ".join(text_)


if __name__ == "__main__":
    pass
    # data = []
    # for i in range(1000):
    #     print(i)
    #     data.append(get_game_text())

    # with open(database, "w") as file:
    #     json.dump(data, file)
