# Implements the Queue ADT using a singly linked list.

# Defines a private storage class for creating list nodes.
class ListNode( object ):
    def __init__( self, item ) :
        self._item = item
        self._next = None

class LQueue :
    # Constructs an empty queue.
    def __init__( self ):
        self._head = None
        self._tail = None
        self._size = 0

    # Return True if the queue is empty or False otherwise.
    def isEmpty(self):
        return len(self) == 0 # เก็บค่าเพื่อเช็คว่าขนาดของตัวแปรในqueueว่างไหม
        
    
     # Returns the number of items in the queue.
    def __len__( self ):
        return self._size # เก็บค่าขนาดของqueue

    # Return but not remove the first item on the queue.
    def first(self):
        assert not self.isEmpty(),"Queue is empty"
        return self._head._item

    # Removes and return the first (head of the linked list) item from the queue
    def dequeue(self):
        assert not self.isEmpty(),"Queue is empty" # ตรวจสอบขนาดของ queue ว่าว่างมั้ย เพื่อให้สามารถนำค่าออกจาก queue ได้
        self._head = self._head._next  # ให้ head ตัวปัจจุบันเคลื่อนไปอยู่ค่าถัดไป
        self._size = self._size - 1    # ลดขนาดของ queue ออก ให้เท่ากับตัวแปรที่นำออก

    # add a new item onto the last of the queue (tail of the linked list).
    def enqueue( self, item ):
        newNode = ListNode(item)
        if self.isEmpty():# เช็คขนาดของ queue ว่าว่างไหมถ้าว่างให้สร้างเพิ่ม
            self._head = newNode #สร้าง node ใหม่ให้อยู่ที่ส่วนต้น
        else:
            self._tail._next = newNode # สร้างตัวท้ายตัวใหม่ให้เป็น newNode
        self._tail = newNode # ให้ค่าตัวท้ายสุดให้เป็น newNode
        self._size = self._size +1 # เพิ่มขนาดของ queue ให้เท่ากับจำนวนตัวแปรที่เพิ่มเข้ามา
        return item

    # Traversing a linked list
    def __repr__(self):
        curNode = self._head
        s = "["
        while curNode is not None:
            #print(curNode.item)
            s = s + str(curNode._item)+ " "
            curNode = curNode._next

        s = s[:-1] + "]"
        return s
    
    def __str__(self):
        curNode = self._head
        s = "["
        while curNode is not None:
            #print(curNode.item)
            s = s + str(curNode._item)+ " "
            curNode = curNode._next
        s = s[:-1] + "]"
        return s
        
    # Determines if an item is contained in the queue.
    def isContain( self, target ):
        curNode = self._head
        while curNode is not None and curNode._item != target :
            curNode = curNode._next
        return curNode is not None

        
# Code start here
A = LQueue()
A.enqueue(4)
A.dequeue()
A.enqueue(23)
A.enqueue(74)
A.enqueue(12)
A.first()
print(A)

# print(A) จะได้
# [23 74 12]