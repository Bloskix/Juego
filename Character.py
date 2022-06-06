from Constantes import *
class Character:
    def __init__(self,name,age,str,agi,con,race):
        self.__name = name
        self.__age = age if self.check_validate_age(age) else 1
        self.__str = str
        self.__agi = agi
        self.__con = con
        self.__race = race

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

    def check_character_stats (self,str,agi,con):
        if (str + agi + con == MAX_STATS_POINTS):
            return True
        elif (str + agi + con < MAX_STATS_POINTS or str + agi + con > MAX_STATS_POINTS):
            print ("The amount of stats points must be 15")
            return False
    def set_str(self,str):
        while (str > MAX_STAT_POINT and str < MIN_STAT_POINTS):
            print ("The strenth can´t be more than 13 or less than 1")
            self.__str = str
    def set_agi(self,agi):
        while (str > MAX_STAT_POINT and str < MIN_STAT_POINTS):
            print("The strenth can´t be more than 13 or less than 1")
            self.__agi = agi
    def set_con(self,con):
        while (str > MAX_STAT_POINT and str < MIN_STAT_POINTS):
            print("The strenth can´t be more than 13 or less than 1")
            self.__con = con

    def set_race(self,race):
        if (race == "orc"):
            self.__str = self.__str + ORC_STATS
        elif (race == "elf"):
            self.__agi = self.__agi + ELF_STATS
        elif (race == "human"):
            self.__con = self.__con + HUMAN_STATS







