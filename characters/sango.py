import random

class Sango :
    def __init__(self):
        self.race = "human"
        self.is_happy = True
        self.attacks = ["Hiraikotsu", "Heat Blast" , "Meido Zangetsuha"]
        self.rage = 0
        self.hp = 100
        self.selfsteem = -10
        self.name = "Inuyasha"

    def trigger (self):
        self.is_moody = True

    def calm (self) :
        self.is_moody = False    


    def listen (self, speaker): 
        if speaker == "Kagome" :
            se= self.selfsteem + 20
            self.selfsteem = se 

        if speaker == "Naraku": 
            self.is_moody = True
            self.rage = 30
            se = self.selfsteem -20
            self.selfsteem =se

    def jealousy (self, rival):
        if rival == "Koga":
            bm = True 
            self.is_moody =bm

    def select_attack(self):
        attack = random.choice (self.attacks)
        return attack
    
    def learn_attack(attack_name):
        # TODO: Borrar pass y programar la funcion
        # recibe un nombre y lo guarda en sus ataques
        # revisar como agregas cosas a una lista en la funcion winners de combat.py
        pass


def inuyasha_attacks (inuyasha, characters):
    attack = None
    if "Naraku" in characters:
        if inuyasha.rage >= 30:
            attack = random.choice (inuyasha.attacks)


    return attack  