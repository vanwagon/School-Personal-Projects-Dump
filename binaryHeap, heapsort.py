class BinHeap: 
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0
    
    def percUp(self,i):
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                tmp = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = tmp
            i = i // 2
            
    def insert(self,k):
        self.heapList.append(k)
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)
        
    def percDown(self,i):
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc
    
    def minChild(self,i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i*2] < self.heapList[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1
    def delMin(self):		#returns the item with the minimum key value, removing the item from the heap.
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.percDown(1)
        return retval

    def buildHeap(self,alist): # builds a new heap from a list of keys.
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        while (i > 0):
            self.percDown(i)
            i = i - 1

# Pseudo code Lecture 14
#while the heap is not empty --> while current size > 0
#remove the first item from the heap by swapping it -- > self.delMin()
#with the last item in the heap --> append the deleted
#reduce the size of the heap by one --> list already goes down from delmin()
#restore the heap property --> ask during office hours

    def heapSort(self, alist):
        sortedlist = []
        self.buildHeap(alist)
        i=0
        while self.currentSize > 0:
            temp = self.delMin() #temp of what will be deleted
            print(temp)
            sortedlist.insert(i, temp) #add onto temporary list
            #print(sortedlist)
            i += 1
        return sortedlist

#testing code
z = [5, 2, -100, 3, 7, 2000, 4]
    
x = BinHeap()
#x.buildHeap(z) #buildheap operator
y= x.heapSort(z)
print(y) #should be -100, 2, 3, 4, 5, 7, 2000
#print(x.heapSort())

