# ----------------------------------------------------------------------------------------------
# Practice II) Tree Traversals
# Mission: Complete the code for “Post-order traversal” and “In-order traversal” 
# ----------------------------------------------------------------------------------------------

class BinaryTree:
    def __init__(self,Rootobj):
        self.key = Rootobj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self,newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self,newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self,obj):
        self.key = obj

    def getRootVal(self):
        return self.key
 
    def preorder(self):  #root l r
        print(self.key)
        if self.leftChild:
            self.leftChild.preorder()
        if self.rightChild:
            self.rightChild.preorder()
        
    def postorder(self):  #l r root
        #Enter code here
        if self.leftChild:
            self.leftChild.postorder()
        if self.rightChild:
            self.rightChild.postorder()
        print(self.key)
        
    def inorder(self):  #l root  r
        #Enter code here
        if self.leftChild:
            self.leftChild.inorder()
        print(self.key)
        if self.rightChild:
            self.rightChild.inorder()
        
    def breadthorder(self):
        q = list()
        q.append(self)
        while q:
            node = q.pop(0)
            print(node.key)
            if node.leftChild:
                q.append(node.leftChild)
            if node.rightChild:
                q.append(node.rightChild)
    

t = BinaryTree('A')
t.insertLeft('B')
t.insertRight('C')
t.getLeftChild().insertLeft('D')
t.getLeftChild().insertRight('E')
t.getLeftChild().getRightChild().insertLeft('H')
t.getRightChild().insertLeft('F')
t.getRightChild().insertRight('G')
t.getRightChild().getRightChild().insertLeft('I')
t.getRightChild().getRightChild().insertRight('J')


#Enter code here
t.preorder()
# t.preorder() จะได้ 
# A
# B
# D
# E
# H
# C
# F
# G
# I
# J
print('-'*20)

t.postorder()
# t.postorder() จะได้ 
# D
# H
# E
# B
# F
# I
# J
# G
# C
# A
print('-'*20)

t.inorder()
# t.inorder() จะได้ 
# D
# B
# H
# E
# A
# F
# C
# I
# G
# J
print('-'*20)