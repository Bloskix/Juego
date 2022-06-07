from Character import *
from Constantes import *

tof = True
while tof == True:
    character = Character ("name", 1, 5, 5, 5, "race")
    print ("====================","\n1. Create character", "\n2. Choose character", "\n3. Delete character", "\n4. Fight" "\n====================")
    print ("Choose an option:")
    option = int(input())
    if (option == 1):
        print (ADD_NAME)
        name = str(input())
        character.set_name(name)
        print (ADD_AGE)
        age = int(input())
        character.set_age(age)
        print (ADD_STRE)
        stre = int(input())
        character.set_stre(stre)
        print (ADD_AGI)
        agi = int(input())
        character.set_agi(agi)
        print (ADD_CON)
        con = int(input())
        character.set_con(con)
        stats = character.check_character_stats(stre,agi,con)
        while (stats == False):
            print(ADD_STRE)
            stre = int(input())
            character.set_stre(stre)
            print(ADD_AGI)
            agi = int(input())
            character.set_agi(agi)
            print(ADD_CON)
            con = int(input())
            character.set_con(con)
            stats = character.check_character_stats(stre, agi, con)
        print (ADD_RACE)
        race = str(input())
        character.set_race(race)
        character.add_character(character)
        print("Character created")
    elif (option == 2):
        if (character.check_character_list()) == False:
            print("You don´t have any character created")
        else:
            for i in range(len(character.characters)):
                character.get_characters(i)

