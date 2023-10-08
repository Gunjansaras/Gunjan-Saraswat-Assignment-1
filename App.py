import Game
Game.gameintro()

chosen_role = input("Enter the role that you would like to play in the story; 1)Knight  2)Wizard  ")

print("GREAT CHOICE!!")

print("Your role can have the following attributes; \n 1.Strength(ST), \n 2.Dexterity(DX), \n 3.Intelligence(IQ), \n 4. Health(HQ).")

#user will b=e shown which attribute he or she excels in.
#Moreover, the user's attribute will be assigned two hard coded values according to how much they excel in that particular attribute.


print("Moreover, your attributes will be assigned an hard-coded valuesfrom -2,-1,0,1,2 (-2 being the least and 2 being the most).")
print("LET'S SEE WHICH ATTRIBUTE DOES YOUR CHOSEN ROLE EXCEL IN. \n ")

Game.dicegameplay_rules(chosen_role)
    