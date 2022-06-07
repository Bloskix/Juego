from Constantes import *
class Character:
    def __init__(self,name,age,stre,agi,con,race):
        self.__name = name
        self.__age = age if self.check_validate_age(age) else 1
        self.__stre = stre
        self.__agi = agi
        self.__con = con
        self.__race = race
        self.characters = []


    def set_name (self,name):
        self.__name = name

    def check_validate_age(self,age):
        if age > 0:
            return True
        else:
            print ("edad no valida")
            return False
    def set_age (self,age):
        self.__age = age if self.check_validate_age else 0

    def check_character_stats (self,stre,agi,con):
        if (stre + agi + con == MAX_STATS_POINTS):
            return True
        elif (stre + agi + con < MAX_STATS_POINTS or stre + agi + con > MAX_STATS_POINTS):
            print ("The amount of stats points must be 15")
            return False
    def set_stre(self,stre):
        while (stre > MAX_STAT_POINT and stre < MIN_STAT_POINTS):
            print ("The strenth can´t be more than 13 or less than 1")
            self.__stre = stre
    def set_agi(self,agi):
        while (agi> MAX_STAT_POINT and agi < MIN_STAT_POINTS):
            print("The strenth can´t be more than 13 or less than 1")
            self.__agi = agi
    def set_con(self,con):
        while (con > MAX_STAT_POINT and con < MIN_STAT_POINTS):
            print("The strenth can´t be more than 13 or less than 1")
            self.__con = con

    def set_race(self,race):
        if (race == "orc"):
            self.__stre = self.__stre + ORC_STATS
        elif (race == "elf"):
            self.__agi = self.__agi + ELF_STATS
        elif (race == "human"):
            self.__con = self.__con + HUMAN_STATS

    def add_character(self,character):
        self.characters.append(character)

    def check_character_list(self):
        if len(self.characters) == 0:
            print(len(self.characters))
            print("FALSE")
            return False
        else:
            print("TRUE")
            return True

    def get_characters(self,i):
        name = getattr(self.characters[i],"name")
        age = getattr(self.characters[i],"age")
        stre = getattr(self.characters[i],"stre")
        agi = getattr(self.characters[i],"agi")
        con = getattr(self.characters[i],"con")
        race = getattr(self.characters[i],"race")
        return print(name,age,stre,agi,con,race)


