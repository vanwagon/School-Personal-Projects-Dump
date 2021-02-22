import committee
people = int(input('Enter the number of professors in the department:\n')) #number of people
flexibility = input('Can a professor be on multiple committees? Enter y or n:\n') #allows for conditional statemenet in the while
#the loop should terminate if either the empty string "" is entered 
#for the name of the committee, or if each professor can serve on at most one committee, and there are no 
#unassigned professors left after a committee is formed
#committee_name = input('Enter the name of the committee:\n')
ways_to_form = 1
#placeholder=people
#while committee_name:
while True:
	placeholder = people
	if flexibility == 'y': #professors can be on multiple committees
		committee_name = input('Enter the name of the committee:\n')
		try:
			if committee_name == '':
				#print('There are %d ways to form all the committees.' % ways_to_form) #altogether the committees ways to form.. huge number
				break
			else:
				conditional_chairperson = input('Does the committee need a chairperson? Enter y or n:\n')
				if conditional_chairperson == 'y': #if needs chairperson
					chairperson = True
					members = int(input('Enter the number of members:\n'))
					print('There are %d  ways to form the %s committee.' % (committee.committee(people, members, chairperson),committee_name)) #number of ways to form THIS committee w/ chairperson
					ways_to_form = ways_to_form * committee.committee(people, members, chairperson)  #multiplies onto the number of ways that positions and committees can be made
					pass
				elif conditional_chairperson == 'n': #if needs chairperson
					chairperson = False
					members = int(input('Enter the number of members:\n'))
					print('There are %d  ways to form the %s committee.' % (committee.committee(people, members, chairperson),committee_name))#number of ways to form THIS committee where no chairperson needed
					ways_to_form = ways_to_form * committee.committee(people, members, chairperson) #multiplies onto the number of ways that positions and committees can be made
					pass
				pass
		except ValueError as e:
			print(e)
			

	if flexibility == 'n': #professors can not be on multiple committees (subtract from total people)
		committee_name = input('Enter the name of the committee:\n')
		try:
			if committee_name == '':
				break
			else:
				conditional_chairperson = input('Does the committee need a chairperson? Enter y or n:\n')
				
				if conditional_chairperson == 'y': 
					chairperson = True

					members = int(input('Enter the number of members:\n'))
					#placeholder = placeholder - members #subtracts from total people each time
					if members > people:#if placeholder <= 0: #if people can not be subtracted all the way, assign the remainder
						members = people #members = 0 - placeholder #placeholder is people
						print('Assigning only %d members to the %s committee.' % (members, committee_name))
						print('There are %d ways to form the %s committee.' % (committee.committee(people, members, chairperson),committee_name))#number of ways to form THIS committee where no chairperson needed
						ways_to_form = ways_to_form * committee.committee(people, members, chairperson)
						break
					else:
						print('There are %d  ways to form the %s committee.' % (committee.committee(people, members, chairperson),committee_name)) #number of ways to form THIS committee w/ chairperson
						ways_to_form = ways_to_form * committee.committee(people, members, chairperson)  #multiplies onto the number of ways that positions and committees can be made
						people = people - members
						pass
				if conditional_chairperson == 'n':
					chairperson = False
					members = int(input('Enter the number of members:\n'))
					#placeholder = placeholder - members #subtracts from total people each time
					if members > people: #placeholder <= 0: #if people can not be subtracted all the way, assign the remainder
						members = people #0 - placeholder
						ways_to_form = ways_to_form * committee.committee(people, members, chairperson)
						print('Assigning only %d members to the %s committee.' % (members, committee_name))
						print('There are %d ways to form the %s committee.' % (committee.committee(people, members, chairperson),committee_name))#number of ways to form THIS committee where no chairperson needed
						break
					else:
						print('There are %d  ways to form the %s committee.' % (committee.committee(people, members, chairperson),committee_name)) #number of ways to form THIS committee w/ chairperson
						ways_to_form = ways_to_form * committee.committee(people, members, chairperson)  #multiplies onto the number of ways that positions and committees can be made
						people = people - members
						pass
			if people == 0:
				break
		except ValueError as z:
			print(z)
print('There are %d ways to form all the committees.' % ways_to_form)	#altogether the committees ways to form.. huge number