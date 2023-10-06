def Knight_attributes():
    Strength = 2
    Intelligence = 0
    Dexterity = 2
    Health = 2
    print('Strength =', Strength)
    print('Dexterity =,', Dexterity)
    print('Health =', Health)
    print('Intelligence =', Intelligence)

import random
class knightChallenges:
    def __init__(self, role, strength = 0, dexterity = 2, intelligence = 2):
        self._role = role
        self._strength = strength
        self._dexterity = dexterity 
        self._intelligence = intelligence

    def Kchallenge1(self,answer):
        #testing on intelligence of the wizard 
        #https://www.theshopofmanythings.com/blogs/lessons-from-the-tabletop/riddles
        print("Welcome to challenge1!")
        print("In order to succeed in the challenge1, the player must solve the following riddle.")
        print("My life can be measured in hours,")
        print("I only serve to be devoured.")
        print("Slim, I am quick.")
        print("Fat, I am slow.")
        print("Wind is my foe.")
        if self.answer.upper() == "CANDLE":
            print("Congratulations you succeed in this challenge!")
    
    def Kchallenge2(self):
        #https://skyrim.fandom.com/wiki/Deep_Wounds
        print('This challenge is called deep wounds.')
        print("In this challenge you have to kill at least 30 monsters in 15 seconds,")
        print("And in order to do that, you must have at least 50 points which you will attain from critical win.")
        criticalwin = input("enter yes or no; ")
        if criticalwin == "yes":
            print("congratulations you have the critical win and an additional 60 points, you win")
        else:
            print("you loose")
    
    def Kchallenge3(self):
        #https://dndtools.net/classes/knight/
        
