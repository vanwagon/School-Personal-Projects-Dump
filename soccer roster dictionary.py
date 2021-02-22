roster ={} #made dictionary

num_players = 5
for i in range(num_players):
	jerseynum = int(input('Enter player %d\'s jersey number:\n' % (int(i)+1))) #asks for input of jersey num
	#key = ('Jersey Number'
	playerrate = int(input('Enter player %d\'s rating:\n' % (int(i)+1))) #ask input of rating
	roster[jerseynum] = playerrate #adds jerseynum and playerrate to dictionary
	jerseynum = 0
	playerrate = 0
	print('')
	
jerseylist = list(roster.keys())
jerseylist.sort() #sorts the jersey numbers
ratinglist = list(roster.values())
	
print('ROSTER')
for i in jerseylist:
	print('Jersey number: %d, ' % i, end = '') 
	print('Rating: %d' % roster[i])#connect the player's sorted jersey numbers with their rating'
else:
	print('')
	print('MENU')
	print('a - Add player')
	print('d - Remove player')
	print('u - Update player rating')
	print('r - Output players above a rating')
	print('o - Output roster')
	print('q - Quit\n')
	
user_input = input('Choose an option:\n') #ask for input given instructions from else statement
while user_input:
	if user_input == 'q':
		break
	if user_input == 'o':	#reprints the roster
		user_input = input()
		if user_input == 'q':
			break
	else:
		if user_input == 'q':
			break
		if user_input == 'o': #reprints the roster
			for i in jerseylist:
				print('Jersey number: %d, ' % i, end = '') 
				print('Rating: %d' % roster[i])
			user_input = input('Choose an option:\n')
			pass
		if user_input == 'u':
			player_to_update = int(input())
			newrating = int(input())
			roster[player_to_update] = newrating #updates the player's rating
			user_input = input()
			if user_input == 'o':
				jerseylist = list(roster.keys())
				jerseylist.sort() #sorts the jersey numbers
				ratinglist = list(roster.values())
				print('ROSTER')
				for i in jerseylist:
					print('Jersey number: %d, ' % i, end = '') 
					print('Rating: %d' % roster[i])
				print('')
				print('MENU')
				print('a - Add player')
				print('d - Remove player')
				print('u - Update player rating')
				print('r - Output players above a rating')
				print('o - Output roster')
				print('q - Quit\n')
				user_input = input('Choose an option:\n')
				if user_input == 'q':
					break
				else:
					pass
		if user_input == 'a':
			newplayer = int(input())
			newplayerrating = int(input())
			roster[newplayer] = newplayerrating
			user_inputo = input()
			
			if user_inputo == 'o':
				print('ROSTER')
				jerseylist = list(roster.keys())
				jerseylist.sort() #sorts the jersey numbers
				ratinglist = list(roster.values())
				for i in jerseylist:
					print('Jersey number: %d, ' % i, end = '') 
					print('Rating: %d' % roster[i])
				print('')
				print('MENU')
				print('a - Add player')
				print('d - Remove player')
				print('u - Update player rating')
				print('r - Output players above a rating')
				print('o - Output roster')
				print('q - Quit\n')
				user_input = input('Choose an option:\n')
				if user_input == 'q':
					break
				else:
					pass
				
			elif user_input == 'q':
				break
		if user_input == 'd':
			inputdelete = int(input())
			del roster[inputdelete]
			user_input = input()
			if user_input == 'o':
				print('ROSTER')
				jerseylist = list(roster.keys())
				jerseylist.sort() #sorts the jersey numbers
				ratinglist = list(roster.values())
				for i in jerseylist:
					print('Jersey number: %d, ' % i, end = '') 
					print('Rating: %d' % roster[i])
				print('')
				print('MENU')
				print('a - Add player')
				print('d - Remove player')
				print('u - Update player rating')
				print('r - Output players above a rating')
				print('o - Output roster')
				print('q - Quit\n')
				user_input = input('Choose an option:\n')
				if user_input == 'q':
					break
				else:
					pass
				
		
		if user_input == 'r':
			ratingbenchmark = int(input('Enter a rating:\n'))
			print('')
			print('ABOVE %d' % ratingbenchmark)
			jerseylist = sorted(roster)
			for i in range(len(jerseylist)):
				if roster.get(jerseylist[i]) > ratingbenchmark: #sees what ratings is higher than the user input's rating
					print('Jersey number: %d, ' % jerseylist[i], end = '')
					print('Rating: %d' % roster.get(jerseylist[i]))
			print('')
			print('MENU')
			print('a - Add player')
			print('d - Remove player')
			print('u - Update player rating')
			print('r - Output players above a rating')
			print('o - Output roster')
			print('q - Quit\n')
			user_input = input('Choose an option:\n')
			pass
			
			



