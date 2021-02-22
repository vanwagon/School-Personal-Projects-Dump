def ternarySearch(alist, item): #the print() is to test my code
    first = 0
    last = len(alist)-1
    found = False
    while first <= last and not found:
        midpoint1 = (first + last)//3 #at a third of the list
        print('this is the left midpoint1=', midpoint1)
        midpoint2 = (midpoint1 * 2) + 1 #at the second third of the list
        print('this is the right midpoint2=', midpoint2)
        if alist[midpoint1] == item or alist[midpoint2] == item:
            found = True
        else:
            if item < alist[midpoint1]:
                last = midpoint1
              
                print('this is the new last=', last)
            elif item> alist[midpoint2]:
                first = midpoint2 -1
                print('this is the new first=', first)
            else:
            
                midpoint1=midpoint2
                print('this is the new first AND last=', first, last)
    return found
    
#testing
alist = [1, 2, 3, 4, 5, 6, 7, 8]
z = ternarySearch(alist, 6)
print(z)
