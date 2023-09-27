#game introduction 
print("Welcome to the Text Adventure Game!")
print("In a world shrouded in mystery and danger, you stand at the crossroads of destiny.")
print("As you embark on this thrilling journey, you must choose your path wisely.")
print("Two remarkable roles await you:")
print("1. Wizard - A wielder of arcane powers, mastering intelligence and magic.")
print("2. Barbarian - A mighty warrior, known for unmatched strength and valor.")

#Quest 
print("GET READY FOR THE QUEST!")
print("The treasure is hidden in the Amazon Rainforest. Among the DeAdLiEsT animals!")
print("Take it upon you to find it while managing to survive in this dangerous rainforest!")
print("You will be tested on all of your attributes and accordingly you will face three challenges!")
print("In order to win, you have to win all the three challenges! ")
print("Failure in any of the challenge will lead to an overall failure in the game.")

#Dice based game play rules 
print("TIME FOR THE GAME PLAY RULES.")
print("The user will get to choose the number of six-numbered dice and according to which the range will be calculated.")

#importing random module in order to get a random number on the dice.

import random
number_of_dice = int(input("Enter the number of dices you want to play with; \n 1) 1 \n 2) 2 \n 3) 3  \n"))

if number_of_dice == 1:
    diceroll_number = random.randint(1,6)
    print(diceroll_number, "is your dice roll number.")
    if diceroll_number == 1:
        print("CRITICAL LOSS")
        print("SORRY! Not only did you loose the game but your attributes also decreased!")
    elif diceroll_number in [2,3]:
        print("LOSS")
        print("SORRY! You lost the game but at least you attributes experienced no change.")
    elif diceroll_number in [4,5]:
        print("WIN")
        print("CONGRATULATIONS! You won the game but your attributes experienced no change.")
    else:
        print("CRITICAL WIN")
        print("CONGRATULATIONS! Not only did you win the game but also your attributes increased!")
elif number_of_dice == 2:
    diceroll_number1 = random.randint(1,6)
    diceroll_number2 = random.randint(1,6)
    print(diceroll_number1, "is your dice roll number 1.")
    print(diceroll_number2, "is your dice roll number 2.")
    sum = diceroll_number1 + diceroll_number2   #sum of numbers of both the dices. RANGE FROM (2,12)
    print(sum, "is the sum of both the numbers.")
    if sum in [2,3]:
        print("CRITICAL LOSS")
        print("SORRY! Not only did you loose the game but your attributes also decreased!")
    elif sum in [4,7]:
        print("LOSS")
        print("SORRY! You lost the game but at least you attributes experienced no change.")
    elif sum in [8,10]:
        print("WIN")
        print("CONGRATULATIONS! You won the game but your attributes experienced no change.")
    else:
        print('CRTICAL WIN')
        print("CONGRATULATIONS! Not only did you win the game but also your attributes increased!")
else:
    diceroll_number1 = random.randint(1,6)
    diceroll_number2 = random.randint(1,6)
    diceroll_number3 = random.randint(1,6)
    print(diceroll_number1, "is your dice roll number 1.")
    print(diceroll_number2, "is your dice roll number 2.")
    print(diceroll_number3, "is your dice roll number 3.")
    sum = diceroll_number1 + diceroll_number2 + diceroll_number3  #sum of numbers of all three dices. RANGE FROM (3,18)
    print(sum, "is the sum of all the three numbers.")
    if sum in [3,7]:
        print("CRITICAL LOSS")
        print("SORRY! Not only did you loose the game but your attributes also decreased!")
    elif sum in [8-11]:
        print("LOSS")
        print("SORRY! You lost the game but at least you attributes experienced no change.")
    elif sum in [12,15]:
        print("WIN")
        print("CONGRATULATIONS! You won the game but your attributes experienced no change.")
    else:
        print("CRITICAL WIN")
        print("CONGRATULATIONS! Not only did you win the game but also your attributes increased!")
