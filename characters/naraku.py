from characters.character import Character

class Naraku (Character):
    def __init__(self):
        super().__init__(
            name = "Naraku",
            race = "hybrid",
            is_mad = True,
            is_moody = True,
            attacks = ["Mist", "Bees" , "Puppet"],
            rage = 30,
            hp = 180,
            selfsteem = -50,
            is_hero= False,
        ) 


    def listen (self, speaker): 
        if speaker == "Kagura" :
            se= self.selfsteem + 20
            self.selfsteem = se 

        if speaker == "Inuyasha": 
            self.is_mad = True
            self.rage = self.rage + 30
            se = self.selfsteem -20
            self.selfsteem =se

    def jealousy (self, rival):
        if rival == "Inuyasha":
            bm = True 
            self.is_mad = bm
    

'''
def naraku_attacks (naraku, characters):
    attack = None
    if "Inuyasha" in characters:
        if naraku.rage >= 80:
            attack = random.choice (naraku.attacks)'''


if __name__ == "__main__":
    
    char = Naraku ()

    char.calm ()
    print (char.is_moody)
    print (char.is_mad)