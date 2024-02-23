from fighter import Attack
from fighter import Stats
from fighter import Fighter

def create_attack(name, target, health, defense, attack, action_func):

    '''
    name: nombre del ataque
    target:  "self", "enemies", "allies"
    health: ejemplo 10
    defense: ejemplo 10
    attack: ejemplo 10
    action_func: Lo que hace el ataque
    '''
    stats = Stats(health, defense, attack)
    attack = Attack(name, target, stats)
    attack.action = action_func(attack)
    return attack

# CODIGO EJEMPLO DE FACU
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

# ACA TRABAJAS VOS
def pontuataqueaqui_action(attack):
    def action(fighter, enemies, allies):
        # TODO: aca va lo que hace el ataque
        # ataque que se cure el personaje
        events = {}
        pass
        return events



    return action




if __name__ == "__main__":
    f1 = Fighter("f1", 100, 1, "")
    f1.attacks = {
        "TEST" : create_attack("TEST", "enemies", 10, 0, 0, bakuryuha_action),
        "NUEVO ATAQUE" : create_attack("TEST", "enemies", 10, 0, 0, pontuataqueaqui_action)
    }

    f2 = Fighter("f2", 100, 1, "")

    #attack = f1.attack("NUEVO ATAQUE")
    attack = f1.attack("TEST")


    events = attack.action(f1, [f2], [])

    print(attack)
    print(events)



'''attacks = {
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
'''