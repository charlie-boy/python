from random import randint
#from goto import goto, label
b1=[]
b2=[]
count = 0

s1 = int(raw_input("Enter size of first battleship: "))
s2 = int(raw_input("Enter size of second battleship: "))

for i in range(0,s1):
	b1.append(["O"]*s1)
for j in range(0,s2):
        b2.append(["O"]*s2)

def print_board(board):
	for row in board:
		print " ".join(row)
print "Board 1:"
print_board(b1)
print "\n"
print "Board 2:"
print_board(b2)

def random_row(board):
	return randint(0,len(board)-1)
def random_col(board):
        return randint(0,len(board)-1)

#label rematch

ship_row_1 = random_row(b1)
ship_col_1 = random_col(b1)
ship_row_2 = random_row(b2)
ship_col_2 = random_col(b2)


for turn in range(2):
	print "Turn - " 
	print turn+1
	print "Player 1: "
	guess_row_1 = int(raw_input("Guess the row of first ship: "))
	guess_col_1 = int(raw_input("Guess the col of first ship: "))
	print "Player 2: "
	guess_row_2 = int(raw_input("Guess the row of second ship: "))
	guess_col_2 = int(raw_input("Guess the col of second ship: "))

	if guess_row_1 == ship_row_1 and guess_col_1 == ship_col_1:
		print "Player 1 wins"
		break
	elif guess_row_2 == ship_row_2 and guess_col_2 == ship_col_2:
        	print "Player 2 wins"
        	break
	else:
		count = count + 1
        	if (guess_row_1 < 0 or guess_row_1 > s1-1) or (guess_col_1 < 0 or guess_col_1 > s1-1):
            		print "Oops, that's not even in the ocean. Player 1 play nice"
       		elif(b1[guess_row_1][guess_col_1] == "X"):
            		print "You guessed that one already. Player 1"
        	else:
            		print "You missed battleship! Player 1"
            	b1[guess_row_1][guess_col_1] = "X"

     		if (guess_row_2 < 0 or guess_row_2 > s2-1) or (guess_col_1 < 0 or guess_col_1 > s2-1):
            		print "Oops, that's not even in the ocean. Player 2 play nice"
        	elif(b2[guess_row_2][guess_col_2] == "X"):
            		print "You guessed that one already. Player 2"
       		else:
            		print "You missed battleship! Player 2"
            	b2[guess_row_2][guess_col_2] = "X"
	
		print "Board 1 : "
        	print_board(b1)
		print "\nBoard 2 : "
		print_board(b2)
        	if count==2:
            		print "Game Over"

#choise = raw_input("Do you want a rematch?(y/n)")
#if choise == "y" or choise == "Y":
#	goto rematch
#else:
#	print "game over"




