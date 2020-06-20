board = {
	'T1': ' ', 'T2' : ' ' , 'T3' : ' ',
	'M1': ' ', 'M2' : ' ' , 'M3' : ' ',
	'D1': ' ', 'D2' : ' ' , 'D3' : ' ',
}

player = 1   #to initialize first player
total_moves = 0 #to count the moves
 
def check():
	#Horizantally
	if board['T1'] == 'X' and board['T2'] == 'X' and board['T3'] == 'X':
		print('player1 won')
		return 1
	if board['M1'] == 'X' and board['M2'] == 'X' and board['M3'] == 'X':
		print('player 1 won')
		return 1
	if board['D1'] == 'X' and board['D2'] == 'X' and board['D3'] == 'X':
		print('player 1 won')
		return 1
	#Diagonally
	if board['T1'] == 'X' and board['M2'] == 'X' and board['D3']== 'X':
		print('player 1 won')
		return 1 
	#Verticallly
	if board['T1'] == 'X' and board['M1'] == 'X' and board['D1'] == 'X':
		print('player 1 won')
		return 1
	if board['T2'] == 'X' and board['M2'] == 'X' and board['D2'] == 'X':
		print('player 1 won')
		return 1
	if board['T3'] == 'X' and board['M3'] == 'X' and board['D3'] == 'X':
		print('player 1 won')
		return 1 

	#player2
	#Horizantally
	if board['T1'] == 'O' and board['T2'] == 'O' and board['T3'] == 'O':
		print('player1 won')
		return 1
	if board['M1'] == 'O' and board['M2'] == 'O' and board['M3'] == 'O':
		print('player 1 won')
		return 1
	if board['D1'] == 'O' and board['D2']== 'O' and board['D3'] == 'O':
		print('player 1 won')
		return 1
	#Diagonally
	if board['T1'] == 'O' and board['M2'] == 'O' and board['D3']== 'O':
		print('player 1 won')
		return 1 
	#Verticallly
	if board['T1'] == 'O' and board['M1'] == 'O' and board['D1'] == 'O':
		print('player 1 won')
		return 1
	if board['T2'] == 'O' and board['M2'] == 'O' and board['D2'] == 'O':
		print('player 1 won')
		return 1
	if board['T3'] == 'O' and board['M3'] == 'O' and board['D3'] == 'O':
		print('player 1 won')
		return 1 
	return 0


print('T1|T2|T3')
print('- +-  +-')
print('M1|M2|M3')
print('- +-  +-')
print('D1|D2|D3')
print('********************')


while True:
		print(board['T1'] + '  |  ' + board['T2'] + '  |  ' + board['T3'])
		print('-+-+--+-+-+-')
		print(board['M1'] + '  |  ' + board['M2'] + '  |  ' + board['M3'])
		print('-+-+--+-+-+-')
		print(board['D1'] + '  |  ' + board['D2'] + '  |  ' + board['D3'])

		checked = check()
		if total_moves == 9 or checked == 1:
			break
		while True:   #input players
			if player == 1:  #choose players

				p1_input = input('Player 1 : ')
				if p1_input.upper() in board and board[p1_input.upper()] == ' ':
					board[p1_input.upper()] = 'X'
					player = 2
					break
				# On wrong input
				else:
					print('Invalid input, please try again')
			else:
				p2_input = input('player two : ')
				if p2_input.upper() in board and board[p2_input.upper()] == ' ':
					board[p2_input.upper()] = 'O'
					player = 1
					break
				else: #On wrong input
					print('invalid input, try again')
		total_moves += 1
		print('********************')
		print()
