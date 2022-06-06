from Character import *
from Constantes import *
from Data_base import *

data_base = CharacterController()
print ("====================","\n1. Create character", "\n2. Create Enemy", "\n3. Choose character", "\n4. Delete character", "\n5. Fight" "\n====================")
print ("Choose an option:")
option = int(input())
if (option == 1):
    character = Character ("name", 1, 5, 5, 5, "race")
    print (ADD_NAME)
    name = str(input())
    character.set_name(name)
    print (ADD_AGE)
    age = int(input())
    character.set_age(age)
    print (ADD_STR)
    str = int(input())
    character.set_str(str)
    print (ADD_AGI)
    agi = int(input())
    character.set_agi(agi)
    print (ADD_CON)
    con = int(input())
    character.set_con(con)
    stats = character.check_character_stats(str,agi,con)
    while (stats == False):
        print(ADD_STR)
        str = int(input())
        character.set_str(str)
        print(ADD_AGI)
        agi = int(input())
        character.set_agi(agi)
        print(ADD_CON)
        con = int(input())
        character.set_con(con)
        stats = character.check_character_stats(str, agi, con)


