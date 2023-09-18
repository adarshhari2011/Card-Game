import random
PC_SCORE=0
PLAYER_SCORE=0
CHOICE=""
print("********DEAL THE CARDS********")
CARD_TYPE=["Clubs","Diamonds","Hearts","Spades"]
CARD_NUMBER=[2,3,4,5,6,7,8,9,10,11,12,13,14]
CARD_COUNT=0
while CHOICE !="exit" and CARD_COUNT<15:
  PC_NUMBER=random.choice(CARD_NUMBER)
  PC_TYPE=random.choice(CARD_TYPE)
  PLAYER_NUMBER=random.choice(CARD_NUMBER)
  PLAYER_TYPE=random.choice(CARD_TYPE)
  print("The computer choosed",PC_NUMBER,"of",PC_TYPE)
  print("You have",PLAYER_NUMBER,"of",PLAYER_TYPE)
  if PC_NUMBER>PLAYER_NUMBER:
    print("The computer won this round\nbetter luck next time ")
    PC_SCORE=PC_SCORE+1
  elif PC_NUMBER<PLAYER_NUMBER:
    print("You won this round! ")
    PLAYER_SCORE=PLAYER_SCORE+1
  else:
    print("It is a tie! ")
  
  CARD_COUNT=CARD_COUNT+1
  print("Computer score is",PC_SCORE,"\nYour score is",PLAYER_SCORE )

  CHOICE=input("Type exit to end the game\nType enter to continue\n")  
if PC_SCORE>PLAYER_SCORE:
  print("The computer won this game! ")
elif PC_SCORE<PLAYER_SCORE:
  print("You won the game! ")
else:
  print("It is a tie! ")
