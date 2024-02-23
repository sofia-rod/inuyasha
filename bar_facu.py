from inuyasha import Inuyasha
from naraku import Naraku
from kagome import Kagome
import random

ON_SITE_TRIGGER_INTERACTIONS = {
    'Inuyasha' : ['Naraku'],
    'Kagome': [],
    'Naraku': []
}

WINNING_CALM_INTERACTIONS = ['Naraku']

ATTACK_TRIGGER_INTERACTIONS = {
    'Naraku' : ['Inuyasha', 'Kagome'],
    'Inuyasha' : ['Naraku'],
    'Kagome' : ['Naraku']
}

TALKING_TRIGGER_INTERACTIONS = {
    'Inuyasha' : ['Naraku'],
    'Kagome' : ['Naraku'],
    'Naraku' : []
}

TALKING_CALM_INTERACTIONS = {
    'Inuyasha' : ['Kagome'],
    'Kagome' : ['Inuyasha'],
    'Naraku' : []
}

def calculate_on_site_interactions(bar, recently_characters_on_bar, characters_name_dict):

    for character_name in bar:
        character = characters_name_dict[character_name]
        interactions = ON_SITE_TRIGGER_INTERACTIONS[character_name]

        for interaction_character_name in interactions:
            if interaction_character_name in recently_characters_on_bar:
                interaction_character = characters_name_dict[interaction_character_name]
                character.trigger(interaction_character)
                print(character.name, "was tiggered by", interaction_character.name)
                print(character.name, "is mad:", character.is_mad)
                print(character.name, "is moody:", character.is_moody)


if __name__ == "__main__":
    inu= Inuyasha()
    nar= Naraku()
    kag= Kagome()

    characters_name_dict = {
        inu.name: inu,
        kag.name: kag,
        nar.name: nar
    }

    bar = []
    recently_characters_on_bar = []
    out = [inu.name, kag.name, nar.name]

    iterations = range(10)

    for i in iterations:
        for character_name in out:
            rng = random.random()
            if rng > 0.5:
                out.remove(character_name)
                print(character_name, "enters to the bar")
                bar.append(character_name)
                recently_characters_on_bar.append(character_name)

        calculate_on_site_interactions(bar, recently_characters_on_bar, characters_name_dict)

        # talk each other
        # calculate_talk_interactions

        print('These characters are in bar', bar)
        print('===============')

        recently_characters_on_bar = []

