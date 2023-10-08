class knightChallenges:
    def __init__(self):
        Strength = 2
        Intelligence = 0
        Dexterity = 2
        Health = 2
        print('Strength =', Strength)
        print('Dexterity =,', Dexterity)
        print('Health =', Health)
        print('Intelligence =', Intelligence)
        self.points = 0
    def play_Knight_game(self):
        def Kchallenge1(self):
            #testing on intelligence of the wizard 
            #https://www.theshopofmanythings.com/blogs/lessons-from-the-tabletop/riddles
            print("Welcome to challenge1!")
            print("In order to succeed in the challenge1, the player must solve the following riddle.")
            print("My life can be measured in hours,")
            print("I only serve to be devoured.")
            print("Slim, I am quick.")
            print("Fat, I am slow.")
            print("Wind is my foe.")
            answer = input("What am I? ")
            if answer.upper() == "CANDLE":
                print("Congratulations you succeed in this challenge!")
                self.points += 25
        
        def Kchallenge2(self):
            #https://skyrim.fandom.com/wiki/Deep_Wounds
            print('This challenge is called deep wounds.')
            print("In this challenge you have to kill at least 30 monsters in 15 seconds,")
            print("And in order to do that, you must have at least 25 points which you will attain from critical win.")
            criticalwin = input("enter yes or no; ")
            if criticalwin == "yes":
                print("congratulations you have the critical win and an additional 60 points, you win")
                self.points += 25
            else:
                print("you loose")
                self.points += 0
        
        def Kchallenge3(self):
            #https://www.brainzilla.com/brain-teasers/riddles/AMol4Jyq/i-am-taken-from-a-mine-and-shut-up-in-a-wooden-case-from-which-i-am/
            print("Welcome to challenge3!")
            print("You find yourself standing at the entrance of a mysterious cave, guarded by a legendary creature known as the Shadow Guardian.")
            print("The Guardian poses a riddle, and only those with wit and courage can proceed.")
            print("I am taken from a mine, and shut up in a wooden case, from which I am never released, and yet I am used by almost every person. What am I?")
            answer = input("Your answer: ")
            if answer.upper() == "PENCIL":
                print("Congratulations, you have solved the riddle and earned the Guardian's respect.")
                print("The Guardian grants you passage to the inner chamber.")
                self.points += 30
            else:
                print("Sorry, your answer is incorrect. The Guardian blocks your way, and you must turn back.")
                self.points += 10
        Kchallenge1(self)
        Kchallenge2(self)
        Kchallenge3(self)
        return self.points
