#according to textbook "The statement a,b=b,a will result in two assignment statements being done at the same time (see Figure 2). Using simultaneous assignment"
#replacing given function with what is said

def bubbleSort(alist):
	L = len(alist)
	for a in range(L):
		for b in range (L - 1):
			if (alist[a] < alist[b]):
				alist[a],alist[b] = alist[b], alist[a] #what is changed
				print(alist) #see progress
	return alist

#testing code
listex = [5, 8, 2, 3, 6, 7, 1, 0, 20, 9]
print(bubbleSort(listex))