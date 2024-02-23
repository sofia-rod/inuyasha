from characters.character import Character
from fighter import Fighter

def character_to_fighter(character : Character, image_path : str) -> Fighter:
    '''
    Va a tomar un character y definir todos los atributos que necesita la clase Fighter
    del juego para poder utilizar en el mismo
    '''

    fighter = Fighter (character.name, character.hp, 1, image_path)
    fighter.attacks = character.attacks
    return fighter