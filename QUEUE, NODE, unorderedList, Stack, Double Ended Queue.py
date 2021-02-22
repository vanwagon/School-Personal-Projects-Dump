#HW 2 ECS 32B William Van 

class QueueX():		#problem #1
	def __init__(self):
		self.items = []
		

	def isEmpty(self):
		return self.items == []
		
	def enqueue(self, item): #rear is where the first element is inserted 
			self.items.insert(0,item)		#self.items.insert(4,item) only works. So use Length function to get number of items

	def dequeue(self): #
		return self.items.pop()

	def size(self):
		return len(self.items)
	
#below this is to test number 1		

list = QueueX()

list.enqueue('Start')
list.enqueue('end')
list.dequeue()
list.enqueue('end2')
list.enqueue('end3')

print(list.items) #shoud print End, end2, end3 bc start is dequeued and the next 3 are end





#problem #2
# 18.Implement the remaining operations defined in the UnorderedList ADT (append, index, pop, insert).
class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext

    
class UnorderedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    def append(self, item):
        added = item
        if self.head == None:
            self.head = added
        else:
            newtail = self.tail.setNext(added)
            self.tail= newtail
        self.size = self.size + 1
    def index(self, item):
        referencer = self.head
        position = 0
        
        if referencer == None:
            return False
        else:
            if referencer == item:
                return position
            else:
                while referencer != item:
                    if referencer == item:
                        return position
                    referencer = referencer.getNext()
                    position = position + 1
    def pop(self): #pop function was taken from miderm sample review answer which was given by TA during discussion
        curr = self.head
        if curr.getNext() == None:
            self.head = None
        else:
            while curr.getNext() != None:
                prev = curr
                curr = curr.getNext()
                prev.setNext(None)
            self.size = self.size-1
            return curr.getData()
    def insert(self, item, index):
	    referencer == self.head
	    prev = None
	    tobeinserted = Node(item) #for future insert node
	    position = 0
	    while self.size != 0:
		    if position < 0 or position > self.size:
		        return False
		    if position == 0:
			    self.add(item)
			    self.head = tobeinserted
		    if position == self.size:
			    self.append(tobeinserted)
		    if position == index:
			    prev.setNext(tobeinserted)
		    prev == referencer
		    referencer = referencer.getNext() #moves down list of nodes
		    position = position + 1
		
			
#3 on HW 2 also known as excercise 19
    def slice(self, start, stop):
	    list =[]
	    next = self.head
	    position == 0
	    difference = stop - start
	    while start <= difference:
		    for i in range(stop - start):
			    if  start == position:
				    list.insert(self.head)
			    start+=1
			    list.append(next)
			    next = self.head.getNext()
				
				
			
		

#4 on HW 2
    def convert(self):
	    referencer == self.head
	    list == []
	    index = 0
	    while self.size != 0:
		    list.append[referencer]
		    referencer == referencer.getNext()
			
		    if index == self.size:
			    break
		    index = index + 1
#5 on HW 2
class Stack:
	def __init__(self):
		self.head = None
		self.size = 0
	def isEmpty(self):
		if self.size == 0:
			return True
		else:
			return False

	def push(self, item):
		if self.size == 0: #if nothing in list, just add to it
			self.head = Node(item)
			self.size += 1
		else:
			first = Node(item)
			first.setNext(self.head)
			self.head = first
			self.size += 1

	def pop(self):  
		if self.size == 0: #can't remove if theres nothing there
			return False
		else:
			first = self.head
			self.head.setNext(first) #moves previous head into the next one
			self.head = first

	def peek(self):
		if self.size == 0:
			return False
		else:
			return self.head
			

	def size(self):
		return self.size
		
#HW 6 The linked list implementation given above is called a singly linked list because each node has a single reference to the next node in sequence. An alternative implementation is known as a doubly linked list. In this implementation, each node has a reference to the next node (commonly called next) as well as a reference to the preceding node (commonly called back). The head reference also contains two references, one to the first node in the linked list and one to the last. Code this implementation in Python.
class Node2: #double linked node used geeksforgeeks.org as reference to class
	def __init__(self, next = None, prev = None, data = None):
		self.next = next
		self.prev = prev
		self.data = data

def getNext(self):
	return self.next

def setNext(self, newnext):
	self.next = newnext
	
def getPrev(self):
	return self.prev



class Deque2:
	def __init__(self):
		self.head = None
		self.tail = None
		self.size = 0

	
	def isEmpty(self):
		if self.size == 0:
			return True
		else:
			return False
	
	def addFront(self, item):
		if self.size == 0: #jsut add to deque
			self.head = Node2(item)
			self.size = self.size + 1
		else:  #add in front of first node
			next = head.setNext(head)
			head = Node2(item)
			self.size = self.size + 1
	def addRear(self, item):
		if self.size ==0: #just add to deque
			self.head = Node2(item)
			self.tail = self.head 
			self.size + self.size + 1
		else: #add to the end
			newtail = Node2(item)
			self.tail.setNext(newtail)
			self.tail = newtail
			self.size = self.size + 1
	def removeFront(self):
		if self.size == 0:
			return False
		else:
			secondnode = self.head.getNext()
			self.head.setNext(None)
			self.head = secondnode
			self.size = self.size - 1
	def removeRear(self):
		if self.size == 0:
			return False
		else:
			newtail = self.tail.getPrev()
			self.tail = None
			newtail.setNext(None)
			self.tail = newtail
			self.size = self.size - 1
	
	def size(self):
		return self.size
		
		
	



		