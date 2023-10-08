
import random
class wizardChallenges:
    def __init__(self):
        self.Strength = 0
        self.Dexterity = 2
        self.Intelligence = 2 
        self.Health = 5
        self.points = 0
        self.magical_protection = "no"
        print('Strength =', self.Strength)
        print('Dexterity =,', self.Dexterity)
        print('Health =', self.Health)
        print('Intelligence =', self.Intelligence)
    def play_Wizard_game(self):
        def Wchallenge1(self):
            #testing on intelligence of the wizard 
            #https://www.theshopofmanythings.com/blogs/lessons-from-the-tabletop/riddles
            print("Welcome to challenge1!")
            print("In order to succeed in the challenge1, the player must solve the following riddle.")
            print("What always runs but never walks,")
            print("often murmurs, but never talks,")
            print("has a bed, but never sleeps,")
            print("An open mouth, but never eats.")
            answer = input("please input your answer ")
            if answer.upper() == "RIVER":
                print("Congratulations you succeed in this challenge!")
                print("Magical protection is granted for the next challenge.")
                self.points += 25
                self.magical_protection = "yes"
            else:
                print("Magical protection is not granted for the next challenge.")
                self.points += 20
    
        def Wchallenge2(self):
            #https://www.elventower.com/561-the-elemental-trials-level-9-adventure/
            print("Welcome to challenge2! This challenge is called elemental trial.")
            print("The player must pass this fire trial in order to succeed in this challenge.")
            #testing on dexterity
            print("In front of you, is a 20-feet-tall gate.")
            print("The gate remains open as long as the characters decide if they enter or not; the gate senses when the characters have made up their mind.")
            print("There is no turning back. If they choose not to enter, the gate closes shut for them forever.")
            print("The lava pool produces intense, unbearable heat.")
            print("The Fire Trials begin once the characters cross the gate. Then, twelve magma mephits, two fire elementals, and four salamanders emerge from the lava to attack.")
            subtrials = ['Heat', 'Traps','Lava']
            for subtrial in subtrials:
                if subtrial == 'Heat':
                    print("This subtrial is called HEAT.")
                    print("The temperature inside the chamber of the Fire Trials is so hot that creatures without any magical pro­tection or fire protection.")
                    if self.magical_protection == "yes":
                        print("congratulations, you don't need to use fire damage! You remain protected from heat!")
                        print("Remember! You still have one fire protection left!")
                        self.points += 25
                        print(self.points)
                            
                    else:
                        print("Since you don't have magical protection, you have to use the only one fire damage available to you!")
                        print("You don't have any more fire protection left!")
                        self.points += 20
                        
                elif subtrial == 'Traps':
                    print('This subtrial is called Traps.')
                    print('Five-foot-diameter wrecking balls swing from chains and hit any creature that steps on the marked tiles.')
                    print('Victims take 3d6 bludgeoning damage and can be pushed 15 feet, directly into the lava.')
                    print('But if they move with a speed of more than 70kms/hour, they can dodge the balls.')
                    #random module to determine a random speed
                    print('In order to determine what speed you get assigned, you must spin the wheel of ultimate fate.')
                    print('A player will get 3 chances, the greatest speed among the three will be your assigned speed.')
                    for i in range(3):
                        speed1 = random.randint(60,80)
                        speed2 = random.randint(60,80)
                        speed3 = random.randint(60,80)
                        maximum = max(speed1, speed2, speed3)
                        if maximum>70:
                            print("The wheel of ultimate fate has assigned you ", maximum, 'km/hr of speed.')
                            print('Hence, you are able to dodge the balls and you win this subtrial.')
                            self.points +=10
                        else:
                            print("The wheel of ultimate fate has assigned you ", maximum, 'km/hr of speed.')
                            print('Hence, you are unable to dodge the balls and you lose in this subtrial.')
                            self.points +=5
                else:
                    print('This subtrial is called Lava.')
                    print('Any creature that touches the lava takes 4 fire damage. ')
                    print('The portal floats 10 feet above the searing hot lava.')
                    print('The characters must jump to reach it.')
                    print('In order to determine upto how many feet you can jump, you must spin the wheel of ultimate fate.')
                    print('A player will get 3 chances, the greatest distance among the three will be your assigned speed.')
                    for i in range(3):
                        distance1 = random.randint(7,10)
                        distance2 = random.randint(7,10)
                        distance3 = random.randint(7,10)
                        maximum = max(distance1,distance2,distance3)
                        if maximum==10:
                            print("The wheel of ultimate fate has assigned you ", maximum, 'km/hr of speed.')
                            print('Hence, you are able to dodge the balls and you win this subtrial.')
                            self.points +=10
                        else:
                            print("The wheel of ultimate fate has assigned you ", maximum, 'km/hr of speed.')
                            print('Hence, you are unable to dodge the balls and you lose in this subtrial.')
                            self.points +=5
        
        def Wchallenge3(self):
            print("Welcome in the challenge3!")
            print('There is a gate in front of you. If you answer the following question, you can enter the game.')
            print("I don’t have eyes")
            print('But once I did see')
            print("I once had thoughts,")
            print("Now white and empty.")
            answer2 = input('Who am I? ')
            if answer2.upper() == 'SKULL':
                print('You may enter the game! ')
                print('WELCOME TO THE ARENA!')
                print("In here, you are going to face 5 different monsters and depending on your strength you'll win or loose.")
                monsterstrength1 = random.randint(-2,2)
                if monsterstrength1 < 0:
                    print("The strength of this monster is less than you.")
                    print('Hence, YOU FIGHT WITH THIS MONSTER AND you win this challenge')
                    self.points +=2
                elif monsterstrength1 > 0:
                    print("The strength of the monster is greater than yours.")
                    print("Hence, YOU FIGHT WITH THIS MONSTER AND you loose in this challenge.")
                    self.points +=0
                else:
                    #https://www.theshopofmanythings.com/blogs/lessons-from-the-tabletop/riddles
                    print("Since, your strength is same as the monster's, you will have to solve the following riddle.")
                    print('Bright as diamonds,')
                    print('Loud as thunder,')
                    print('Never still,')
                    print('A thing of wonder.')
                    answer3 = input('Who am I? ')
                    if answer3.upper() == 'WATERFALL':
                        print('Congratulations, you win this challenge.')
                        self.points +=3
                    else:
                        print('SORRY, you loose in this challenge.')   
                        self.points +=0
                   
            else:
                print('Sorry, you have lost the game right away.')
        Wchallenge1(self)
        Wchallenge2(self)
        Wchallenge3(self)
       
        return self.points        


        
    
