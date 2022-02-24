# Implementation of the Stack ADT using a Python list.
class Stack :
    # Creates an empty stack.
    def __init__(self):
        self._theItems = list()

    # Returns True if the stack is empty or False otherwise.
    def isEmpty(self):
        return len(self) == 0

    # Returns the number of items in the stack.
    def __len__ (self):
        return len(self._theItems)

    # Returns the top item on the stack without removing it.
    def peek(self):  # เป็นการข้อดู หรือเรียกดูข้อมุูล เป็นการสั่งให้ข้อมูลออกมา
        assert not self.isEmpty(), "Cannot peek at an empty stack"
        return self._theItems[-1]

    # Removes and returns the top item on the stack.
    def pop(self): # เป็นการดึงข้อมูลหรือดึงค่าออก ซึ่งเป็นไปตาม concept คือ fist in last out ตัวแรกออกทีหลัง ตัวที่เข้าตัวสุดท้ายจะออกก่อน
        assert not self.isEmpty(), "Cannot pop from an empty stack"
        return self._theItems.pop()

    # Push an item onto the top of the stack.
    def push(self, item ): # เป็นการใส่ข้อมูลหรือการป้อนค่าเข้าไปใน STACK 
        self._theItems.append(item)
        
    # Display items in the stack
    def __repr__(self):
        s = ""
        for item in reversed(self._theItems):
            s = s + "| "+str(item)+" \t|" + "\n"
        s = s+"---------"
        return s

f = [1,2,3,4,5] #กำหนด STACK มา 5 ตัวโดยมีตำแหน่งข้อมูลตั้งแต่ 0-4
f.pop(1) #เป็นการดึงข้อมูลในตำแหน่งที่ 1 ออกมา นั่นก็คือ เลข 2
print('f:',f)
# print(f) จะได้ดังนี้
# f: [1, 3, 4, 5]


a=Stack()  #เป็นการสร้าง STACK โดยใส่ค่าต่างๆไป โดยค่าที่ใส่เข้าไปตัวสุดท้ายใน STACK จะเป็นตัวที่ถูกดึงออกมาเป็นตัวแรก 
a.push(8)
a.push(6)
a.push(4)
a.push(2)
a.push(0)
a.pop()
print(a)  
# print(a) จะได้ดังนี้
# | 0     |
# | 2     |
# | 4     |
# | 6     |
# | 8     |
# ---------