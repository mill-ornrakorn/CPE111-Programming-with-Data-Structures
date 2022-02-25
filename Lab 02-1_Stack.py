#implementation of the Queue ADT using a Python list
class Queue:
    # Creates an empty queue.
    def __init__( self ):
        self._qList = list()

    # Returns True if the queue is empty.
    def isEmpty( self ):
        return len( self ) == 0

    # Returns the number of items in the queue.
    def __len__( self ):
        return len( self._qList )

    # Adds the given item to the queue.
    def enqueue( self, item ): #เป็นการเอาค่าเข้าไปใน QUEUE 
        self._qList.append(item)

    # Removes and returns the first item in the queue.
    def dequeue( self ): #เป็นการเอาค่าออกจาก QUEUE
        assert not self.isEmpty(), "Cannot dequeue from an empty queue."
        return self._qList.pop(0)

    # Display items in the queue
    def __repr__(self):
        s = "<--"
        s=s.join([str(x) for x in self._qList])
        return s


A = Queue()
A.enqueue(1) #เป็นการป้อนค่าเข้าไปใน queue เป็นลำดับไปเรื่อยๆ โดยหลักการของ queue คือ ตัวที่ใส่ไปตัวแรกจะเป็นตัวแรกที่ออกก่อนเช่นกัน ตาม concept first in first out 
A.enqueue(2)
A.enqueue(3)
A.enqueue(4)
A.enqueue(5)
x = A.dequeue() #เป็นการเอาค่าออกจาก queue โดยจะเห็นได้ว่าเลขที่ถูกเอาออกจาก queue คือ เลข  1 ซึ่งเป็นค่าเลขที่เอาเข้าไปใน queue นั่นเอง 
print(A) 
# print(a) จะได้ดังนี้
# 2<--3<--4<--5