from characters.character import Character

class Kagome (Character):
    def __init__(self):
        super().__init__(
            name="Kagome",
            race="hybrid", 
            is_mad=False,
            is_moody=False,
            attacks=["Arrow" ,"Shikon Jewel","Osuwari","Sacred Arrow"],
            rage=0,
            hp=100,
            selfsteem=10,
            is_hero= True
        )

    def listen (self, speaker): 
        if speaker == "Inuyasha" :
            se= self.selfsteem + 20
            self.selfsteem = se 


        if speaker == "Naraku": 
            self.is_happy= False
            self.rage = 20
            se = self.selfsteem -20
            self.selfsteem =se

    
'''def kagome_attacks (Kagome, characters):
    attack = None
    if "Naraku" in characters:
        if kagome.rage >= 20:
            attack = random.choice (kagome.attacks)


    return attack 
'''


if __name__ == "__main__":
    
    kagome = Kagome ()

    kagome.trigger ()
    print (kagome.is_moody)
    print (kagome.is_mad)