import os

import pygame
from fighter import Fighter
from game import Game
from fighter import Attack
from fighter import Stats
from fighter import Fighter

def create_attack(name, target, health, defense, attack, action_func):
    stats = Stats(health, defense, attack)
    attack = Attack(name, target, stats)
    attack.action = action_func(attack)
    return attack


def bakuryuha_action(attack):
    def action(fighter, enemies, allies):

        damage = fighter.stats.attack + attack.stats.health
        events = {}
        for enemy in enemies:
            enemy_defense = enemy.stats.defense
            damage = max(0, damage - enemy_defense)
            enemy.takes_damage(damage)
            events[enemy] = damage
        return events
    
    return action

pygame.init()  # Initialize all pygame modules
pygame.font.init()  # Initialize the font module

background_file = os.path.join(os.getcwd(), "assets/forest.jpg")

# Crear luchadores
inu_image_path = os.path.join(os.getcwd(), "assets/inu.jpg")
kagu_image_path = os.path.join(os.getcwd(), "assets/kagu.jpg")

fighter1 = Fighter("Inuyasha", 100, 10, inu_image_path)
fighter1.attacks = {
        "TEST" : create_attack("TEST", "enemies", 10, 0, 0, bakuryuha_action)
    }
fighter2 = Fighter("Kagura", 120, 0, kagu_image_path)

# Crear juego
game = Game(background_file)

# Agregar luchadores al juego
game.add_fighter(fighter1)
game.add_fighter(fighter2)

# Correr el juego
game.run()