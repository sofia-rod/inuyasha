from characters.character import Character

class Inuyasha(Character):

    def __init__(self):
        super().__init__(
            name="Inuyasha",
            race="hybrid", 
            is_mad=False,
            is_moody=False,
            attacks=["Bakuryuha", "Heat Blast" , "Meido Zangetsuha"],
            rage=0,
            hp=100,
            selfsteem=-10,
            is_hero= True
        )   


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


# ESTO NO ES DE LA CLASE
'''def inuyasha_attacks (inuyasha, characters):
    attack = None
    if "Naraku" in characters:
        if inuyasha.rage >= 30:
            attack = random.choice (inuyasha.attacks)


    return attack    '''        



if __name__ == "__main__":
    
    inu = Inuyasha ()
    print (inu.is_moody)
    inu.trigger ()
    print (inu.is_moody)
    #inu = 4
    #print (inu + 3)
    attack = inu.select_attack()
    print("Attack: ", attack)
    print("HP before damage: ", inu.hp)
    inu.takes_damage(20)
    print("HP after damage: ", inu.hp)
    inu.learn_attack ("Gokuyurha")
    print (inu.attacks)





