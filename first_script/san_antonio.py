#Ecriture du code

Quotes = ["listen to me, Mister Shakespeare : we may or may not be, we are", "we must be able listenning to ourselves or being heard"]

Characters = ["alvin et les chumpunks", "betty boot", "babar", "Calimero", "caster", "Baltazar"]

# définition de la fonction get random
def Get_Random_Quotes(My_list):
  # get a random item
  item = My_list[0]
  return item

# Get user answer

User_Answer = input("Press Enter for know another quotes or press 'B' for leave program")

while User_Answer != "B":
  print(Get_Random_Quotes(Quotes))
  User_Answer = input("Press Enter for know another quotes or press 'B' for leave program")
# show random quotes
# put capitalize a fist letter of sentence

for Character in Characters:
  n_Characters = Character.capitalize()
  print(n_Characters)





