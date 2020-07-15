#Ecriture du code

Quotes = ["listen to me, Mister Shakespeare : we may or may not be, we are", "we must be able listenning to ourselves or being heard"]

Characters = ["Alvin et les chumpunks", "Betty boot", "Babar", "Calimero", "Caster", "Baltazar"]

User_Answer = 'B'
# show random quotes

if User_Answer == "B":
  pass
if User_Answer == "C":
  print(" 'C' is'nt a good answer... please enter another letter or press 'B' for leave program")
else :
  pass
def Show_Random_Quotes(My_list):
  Quote = My_list[1]
  print(Quote)

Show_Random_Quotes(Quotes)


