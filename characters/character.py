import random

class Character:
    def __init__(self, name, race, is_mad, is_moody, attacks, rage, hp, selfsteem, is_hero):
        self.race = race
        self.is_mad = is_mad
        self.is_moody = is_moody
        self.attacks = attacks
        self.rage = rage
        self.hp = hp
        self.selfsteem = selfsteem
        self.name = name
        self.is_hero = is_hero
        self.teammates = []

    def takes_damage (self, damage): 
        new_life = self.hp - damage
        self.hp = new_life
        
    def select_attack(self):
        attack = random.choice (self.attacks)
        return attack
    
    def learn_attack(self,attack_name):
        self.attacks.append (attack_name)

    
    def trigger(self, character):
        
        if (character.name in self.teammates) == True :
            self.is_moody = True
        else:
            self.is_mad = True

    def calm(self):
        self.is_moody = False
        self.is_mad = False

    def listen(self, character):
        pass
        
    
    def add_teammates (self,character):
        self.teammates.append (character.name)




