def row_winner(game):

	for item in game:
        
		if item.count(item[0]) == len(item) and item[0] != 0 :
			print('player',item[0], 'wins row') 
			return True
	return False		




def col_winner(game):

	for x in range(len(game)):

	    checklist = []
	    
	    for row in game:
	        checklist.append(row[x])

	    if checklist.count(checklist[0]) == len(checklist) and checklist[0]!= 0 :
	                print('player',checklist[0], 'wins column')     
	                return True
	return False

def diag_winner(game):
	
	diags = []

	for indx in range(len(game)):
				diags.append(game[indx][indx])
		
	if diags.count(diags[0]) == len(diags) and diags[0] != 0:
				print("player",diags[0],  "wins diagonal left to right")
				return True 
	
	diags = []

	for row , col in enumerate(reversed(range(len(game)))):
		    	diags.append(game[row][col])

	if diags.count(diags[0]) == len(diags) and diags[0] != 0:
				print("player",diags[0],  "wins diagonal right to left")
				return True 
	
	return False





def game_board(game_map, player=0, row=0, col=0, just_display=False):
	
	try:
		if game_map[row][col] != 0:
			print('This space is occupied!')
			return game_map, False

		print('Patrick Tic Tac Toe game\n')
		
		#print("   A  B  C")
		#s =  '   '+'  ' .join(str(y) for y in range(len(game)))
		#print(s)
		print('   '+'  ' .join(str(y) for y in range(len(game))))

		if  not just_display:
			#This line is updating the players moves in the TTT memory 
			game_map [row] [col] = player

		for index,row in enumerate(game):
			print(index,row)
				
		return game_map, True 

	except IndexError as patrick_error:
		   print('I goofed', patrick_error)
		   return game_map, False

	except Exception as patrick_error:
		   print('I goofed', patrick_error)
		   return game_map, False



#---------------------------------- Main Flow of the game --------------------


import itertools

play = True
player = [1,2]




while play:
		
		gamesize = int(input("Enter the size of the grid for the game - 2 = 2x2 3 = 3x3 etc : "))

		#gamesize = 4

		game = [   [ 0 for i in range(gamesize)] for i in range(gamesize) ]



		#game = [[0,0,0],
				#[0,0,0],
				#[0,0,0]]

		game_won = False

		game , _ = game_board(game,0,0,0,True)

		player_choice = itertools.cycle([1,2])
		

		while not game_won:
				
				current_player = next(player_choice)

				print(f'current player is: {current_player}')
				
				played = False

				while not played:

					col_choice = int(input('Input your column choice A,B,C :'))
					row_choice = int(input('Input your row choice 0,1,2 : ')) 

					game, played = game_board(game,current_player,row_choice,col_choice,False)

					if row_winner(game) or col_winner(game) or diag_winner(game):
						game_won = True
						again = input('Would you like to play again ? y/n')

						if again.lower() == 'y':
							print('restarting game')

						elif again.lower() == 'n':
							print('Goodbye')
							play = False

						else:
							print('Wrong entry, c u later')
							play = False


					'''if col_winner(game):
						game_won = True
					if diag_winner(game):
						game_won = True'''

					


				

#game [1] [1] = '*' 

#game_board(game, player=2, row=2, col=1, just_display=False)


#diag_winner()
#col_winner()
#row_winner()

#print(game_board)







#game_board()



'''count = 1  


for row in game:
	print(count, row)
	count += 1'''