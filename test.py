#Ecriture du code

Quotes = ["listen to me, Mister Shakespeare : we may or may not be, we are", "we must be able listenning to ourselves or being heard"]

Characters = ["Alvin et les chumpunks", "Betty boot", "Babar", "Calimero", "Caster", "Baltazar"]

User_Answer = input("Press Enter for know another quotes or press 'B' for leave program")
# show random quotes

if User_Answer == "B":
  exit()
if User_Answer == "C":
  print(" 'C' is'nt a good answer... please enter another letter or press 'B' for leave program")
else :
  pass
def Get_Random_Quotes(My_list):
  # get a random item
  item = My_list[1]
  print(item)
  return "Program is over"
  # show the quote
print(Get_Random_Quotes(Quotes))


