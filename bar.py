import random 
from inuyasha import Inuyasha
from naraku import Naraku
from kagome import Kagome


if __name__ == "__main__":
    inu= Inuyasha()
    nar= Naraku()
    kag= Kagome()
    
    inu.add_teammates (kag)
    kag.add_teammates (inu)
    print (inu.teammates)
    print (kag.teammates)
    print (nar.teammates)
    inu.trigger (kag)
    print (inu.is_mad)
    print (inu.is_moody)