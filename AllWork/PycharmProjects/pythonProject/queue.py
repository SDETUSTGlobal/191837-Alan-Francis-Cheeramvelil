#Add and item in a queue
import queue
q1 = queue.Queue()
q1.put(10) #this will additem 10 to the queue.

#import queue
q1 = queue.Queue(5) #The max size is 5.
q1.put(1)
q1.put(2)
q1.put(3)
q1.put(4)
q1.put(5)
print(q1.full()) # will return true.

#import queue
q1 = queue.Queue()
q1.put(10)
item1 = q1.get()
print('The item removed from the queue is ', item1)

#import queue
q1 = queue.LifoQueue()
q1.put(10)

#import queue
q1 = queue.LifoQueue()
q1.put(10)
item1 = q1.get()
print('The item removed from the LIFO queue is ', item1)


#import queue
q1 = queue.Queue()
for i in range(20):
    q1.put(i) # this will additem from 0 to 20 to the queue

#import queue
q1 = queue.Queue()
for i in range(20):
    q1.put(i) # this will additem from 0 to 20 to the queue
while not q1.empty():
    print("The value is ", q1.get()) # get() will remove the item from the queue.

#import queue
q1 = queue.LifoQueue()
for i in range(20):
    q1.put(i) # this will additem from 0 to 20 to the queue

#import queue
q1 = queue.LifoQueue()
for i in range(20):
    q1.put(i) # this will additem from 0 to 20 to the queue
while not q1.empty():
    print("The value is ", q1.get()) # get() will remove the item from the queue.


#import queue
q1 = queue.Queue()
#Addingitems to the queue
q1.put(11)
q1.put(5)
q1.put(4)
q1.put(21)
q1.put(3)
q1.put(10)
#using bubble sort on the queue
n =  q1.qsize()
for i in range(n):
    x = q1.get() # the element is removed
    for j in range(n-1):
        y = q1.get() # the element is removed
        if x > y :
            q1.put(y)   #the smaller one is put at the start of the queue
        else:
            q1.put(x)  # the smaller one is put at the start of the queue
            x = y     # the greater one is replaced with x and compared again with nextelement
    q1.put(x)

while (q1.empty() == False):
    print(q1.queue[0], end = " ")
    q1.get()


#import queue
q1 = queue.Queue()

q1.put(11)
q1.put(5)
q1.put(4)
q1.put(21)
q1.put(3)
q1.put(10)

def reverseQueue (q1src, q2dest) :
    buffer = q1src.get()
    if (q1src.empty() == False) :
        reverseQueue(q1src, q2dest)      #using recursion
    q2dest.put(buffer)
    return q2dest

q2dest = queue.Queue()
qReversed = reverseQueue(q1,q2dest)

while (qReversed.empty() == False):
    print(qReversed.queue[0], end = " ")
    qReversed.get()
