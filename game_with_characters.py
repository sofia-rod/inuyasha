import os

import pygame
from fighter import Fighter
from game import Game
from characters.inuyasha import Inuyasha
from characters.kagura import Kagura 

from fight_arena.utils import character_to_fighter

pygame.init()  # Initialize all pygame modules
pygame.font.init()  # Initialize the font module

background_file = os.path.join(os.getcwd(), "assets/forest.jpg")

# Crear luchadores
inu_image_path = os.path.join(os.getcwd(), "assets/inu.jpg")
kagu_image_path = os.path.join(os.getcwd(), "assets/kagu.jpg")

inu = Inuyasha ()
kagu = Kagura ()

inu = character_to_fighter(inu, inu_image_path)
kagu = character_to_fighter (kagu,kagu_image_path)

# Crear juego
game = Game(background_file)

# Agregar luchadores al juego
game.add_fighter(inu)
game.add_fighter(kagu)

# Correr el juego
game.run()