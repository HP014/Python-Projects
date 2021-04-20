import random
print("Rock...Paper...Scissors")

player1 = input("Player 1 , make your move: ")

ran_num= random.randint(0,2)

if ran_num==0:
	computer="Rock"
elif ran_num==1:
	computer="Paper"
else:
	computer="Scissors"

print(f"Computer Played:{computer}")
#print(computer)


