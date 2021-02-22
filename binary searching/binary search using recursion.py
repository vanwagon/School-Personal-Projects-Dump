
def ternarySearchRec(alist,item): #the print is just to test my code
	if alist == []:
		return False
	else:
		midpoint1 = (len(alist)-1)//3
		midpoint2 = (len(alist)-1) - midpoint1
		print('midpoint1 is:', midpoint1, '\n' 'midpoint2 is:', midpoint2)
		if alist[midpoint1] == item or alist[midpoint2] == item:
			return True
		if item < alist[midpoint1]:
			print('searching under midpoint1 at', midpoint1)
			return ternarySearchRec(alist[:midpoint1], item)
		if item > alist[midpoint2]:
			print('over midpoint2 at', midpoint2)
			return ternarySearchRec(alist[midpoint2:], item)
		else:
			print('searching between two midpoints', midpoint1, 'and', midpoint2)
			return ternarySearchRec(alist[midpoint1+1:midpoint2], item)
			
			

z = [1,2,3,4,5,6,7,8]
print(ternarySearchRec(z, 8))
		
		