from characters.character import Character 


class Kagura (Character):
    def __init__(self):
        super().__init__(
            name= "Kagura",
            race = "extension",
            is_mad = True,
            is_moody = False,
            attacks = ["Dance of the dragon", "Dance of blades" , "Dance of the dead"],
            rage = 20,
            hp = 120,
            selfsteem = -20,
            is_hero = False,
        )  


    def listen (self, speaker): 
        if speaker == "Kagura" :
            se= self.selfsteem + 20
            self.selfsteem = se 

        if speaker == "Inuyasha": 
            self.is_mad = True
            self.rage = self.rage + 30
            se = self.selfsteem -10
            self.selfsteem =se
