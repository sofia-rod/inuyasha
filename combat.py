from characters.inuyasha import Inuyasha
from characters.naraku import Naraku
from characters.kagome import Kagome
from characters.kagura import Kagura 
#from playsound import playsound


attacks = {
    "Bakuryuha" : {
        "damage" : 6,
        "heal" : 0,
        "upgrade_attack" : 0,
        "upgrad_defense" : 0,
        "success_ratio" : "20%",
    },
    "Barrier" : {
        "damage" : 0,
        "heal" : 5,
        "upgrade_attack" : 0,
        "upgrad_defense" : 10,
        "success_ratio" : "100%", 
    },
    "Enrage" : {
        "damage" : 0,
        "heal" : -10,
        "upgrade_attack" : 20,
        "upgrad_defense" : 20,
        "success_ratio" : "50%",
    } # No es de Inuyasha (EJEMPLO)
}

attack_damages = {
    "Bakuryuha" : 6 , 
    "Heat Blast" : 8 ,
    "Meido Zangetsuha" : 11 ,
    "Mist" : 10,
    "Bees" : 4,
    "Puppet" : 3,
    "Arrow" : 5,
    "Shikon Jewel" : 0,
    "Osuwari" : 0,
    "Sacred Arrow" : 7,
    "Dance of the dragon" : 6, 
    "Dance of blades" : 5 , 
    "Dance of the dead" : 8
    }

def attack_simple (attacker, defenders):
    attack = attacker.select_attack ()
    print(attacker.name + ": " + attack)
    damage = attack_damages [attack]

    for defender in defenders:
        new_hp = defender.hp - damage
        defender.hp = new_hp

def winners (characters):
    ret = [] 

    for character in characters :
        if character.hp > 0 : 
            ret.append (character.name)
        

    return ret


if __name__ == "__main__":
    inu = Inuyasha ()
    nar = Naraku ()
    kag = Kagome ()
    kagu = Kagura ()

    while inu.hp > 0 and kag.hp > 0 and nar.hp > 0 and kagu.hp > 0 : 
        attack_simple (nar, [inu, kag]) 
        attack_simple (inu , [nar, kagu])
        attack_simple (kag , [nar, kagu])
        attack_simple (kagu, [inu, kag])
        print ("inuyasha:", inu.hp)
        print ("kagome :", kag.hp)
        print ("naraku:", nar.hp)
        print ("kagura:", kagu.hp)
    
    win = winners ([inu, nar, kag, kagu])

    print ("GANADOR MUNDIAL:", win)        
    print ("SIEMPRE HAY QUE BUSCAAAAAAR! LA VIIIIDA ES ASI <3") 
    #playsound("src/fukai_mori.mp3")
    