def factorial(n):
		seat = 1
		if n < 0: #factorial cant be negative number
			raise ValueError('Cannot take the factorial of a negative number.') 

		for num in range(1, n + 1): 
			seat *= num 
		return seat
	#if n < 0:
		#raise ValueError('Cannot take the factorial of a negative number.')

def committee(people, members, chairperson = True):
	if people < 0: #raise value errors before the else statement
		raise ValueError('People count must be positive.') #error statement
	if members > people:
		raise ValueError('Member count must not be greater than people count.')
	else:
		if chairperson == False:
			return factorial(people) / (factorial(members) * factorial(people-members))#n! / (r!*(n-r)!)  where n = people and r = members
		elif chairperson == True: #the difference is members - 1???
			return factorial(people)/(factorial(members-1) * factorial(people-members)) #n! / ((r-1)!*(n-r)!) where n = people, r = members








	#if people <= 0:
		#raise ValueError('Member count must not be greater than people count.')
	#if members > people:
		#raise ValueError('Member count must not be greater than people count.')
