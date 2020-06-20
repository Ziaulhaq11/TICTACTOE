board = {
	'T1' : ' ', 'T2' : ' ', 'T3' : ' ',
	'M1' : ' ', 'M2' : ' ', 'M3' : ' ',
	'D1' : ' ', 'D2' : ' ', 'D3' : ' ',
}

no_of_times = 0
player = 1

def check():
	#player 1
	#horizontally
	if board['T1'] == 'X' and board['T2'] == 'X' and board['T3'] == 'X':
		print('player 1 win')
		return 1
	if board['M1'] == 'X' and board['M2'] == 'X' and board['M3'] == 'X':
		print('player 1 win')
		return 1
	if board['D1'] == 'X' and board['D2'] == 'X' and board['D3'] == 'X':
		print('player 1 win')
		return 1
	#Diagonally
	if board['T1'] == 'X' and board['M2'] == 'X' and board['D3']== 'X':
		print('player 1 win')
		return 1
	#Vertically
	if board['T1'] == 'X' and board['M1'] == 'X' and board['D1']== 'X':
		print('player 1 win')
		return 1
	if board['T2'] == 'X' and board['M2'] == 'X' and board['D2'] == 'X':
		print('player 1 win')
		return 1
	if board['T3'] == 'X' and board['M3'] == 'X' and board['T3'] == 'X':
		print('player 1 win')
		return 1

	#player 2

	if board['T1'] == 'X' and board['T2'] == 'X' and board['T3'] == 'X':
		print('player 1 win')
		return 1
	if board['M1'] == 'X' and board['M2'] == 'X' and board['M3'] == 'X':
		print('player 1 win')
		return 1
	if board['D1'] == 'X' and board['D2'] == 'X' and board['D3'] == 'X':
		print('player 1 win')
		return 1
	#Diagonally
	if board['T1'] == 'X' and board['M2'] == 'X' and board['D3']== 'X':
		print('player 1 win')
		return 1
	#Vertically
	if board['T1'] == 'X' and board['M1'] == 'X' and board['D1']== 'X':
		print('player 1 win')
		return 1
	if board['T2'] == 'X' and board['M2'] == 'X' and board['D2'] == 'X':
		print('player 1 win')
		return 1
	if board['T3'] == 'X' and board['M3'] == 'X' and board['T3'] == 'X':
		print('player 1 win')
		return 1
	return 0


while True:
	print(board['T1'] + '  |  ' + board['T2'] + '  |  ' + board['T3'])
	print('-+-+-+-+-+-+')
	print(board['M1'] + '  |  ' + board['M2'] + '  |  ' + board['M3'])
	print('-+-+-+-+-+-+')
	print(board['D1'] + '  |  ' + board['D2'] + '  |  ' + board['D3'])
	checked = check()
	if no_of_times == 9 or checked == 1:
		break
	while True:
		if player == 1:
			player_input = input('player 1 :> ')
			if player_input.upper() in board and board[player_input.upper()] == ' ':
				board[player_input.upper()] = 'X'
				player = 2
				break
			else:
				print('enter valid input')
		elif player == 2:
			player_input = input('player 2 :> ')
			if player_input.upper() in board and board[player_input.upper()] == ' ':
				board[player_input.upper()] = 'O'
				player = 1
				break
	no_of_times += 1
	print('***********')

