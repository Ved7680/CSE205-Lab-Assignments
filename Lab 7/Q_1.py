'''
    AUTHOR: Ved J Nayi
    DOC:12-11-22
    Objective: Implementing preoder, inorder and postorder traversal of trees using stacks (not recursion).
'''

ans = []

def peek(stack):
    if len(stack)>0:
        return stack[-1]
    return None

def Insert(arr):
    root = Tree_Node(arr[0])
    for i in range(1,len(arr)):
        parent = Tree_Node(arr[(i-1)//2])
        parent.left = arr[2*i+1]
        parent.right = arr[2*i+2]


class Tree_Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def insertL(self,l_node):
        self.left = l_node
    
    def insertR(self,r_node):
        self.right = r_node

    def printTree(self):
        print(self.data)

        if self.left is not None:
            self.left.printTree()
        if self.right is not None:
            self.right.printTree()

def PreOrder_Traversal(root):

    if root is None:
        return

    stack = []
    stack.append(root)
    
    while(len(stack)>0):
        # Here, node beocmes a object of Tree_Node becuase root is a part of it (for 1st iteration)
        node = stack.pop()
        print(node.data,end=' ')

        if node.right is not None:
            stack.append(node.right)
        if node.left is not None:
            stack.append(node.left)

def InOrder_Traversal(root):
    if root is None:
        return
    
    curr_node = root
    stack = []

    while(1>0):
        if curr_node is not None:
            stack.append(curr_node)
            curr_node = curr_node.left
        
        elif curr_node is None and len(stack) > 0:
            curr_node = stack.pop()
            print(curr_node.data,end=' ')
            curr_node = curr_node.right
        
        else:
            break

    print()

def PostOrder_Traversal(root):
    if root is None:
        return
    
    stack = []
    while(1>0):

        while(root!=None):
            if root.right is not None:
                stack.append(root.right)
            stack.append(root)

            root = root.left

        root = stack.pop()    

        if root.right is not None and root.right == peek(stack):
            stack.pop()
            stack.append(root)
            root = root.right
        
        else:
            print(root.data,end=' ')
            root = None
        
        if len(stack) <= 0:
            break

# root = Tree_Node(15)
# root.left = Tree_Node(10)
# root.right = Tree_Node(2003)
# root.left.left = Tree_Node(10)
# root.left.right = Tree_Node(3)
# root.right.left = Tree_Node(1980)
# root.right.right = Tree_Node(1976)

node1 = Tree_Node(15)
node2 = Tree_Node(10)
node3 = Tree_Node(2003)
node4 = Tree_Node(10)
node5 = Tree_Node(3)
node6 = Tree_Node(1980)
node7 = Tree_Node(1976)

node1.insertL(node2)
node1.insertR(node3)
node2.insertL(node4)
node2.insertR(node5)
node3.insertL(node6)
node3.insertR(node7)

print("PreOder Traversal is given Below: ")
PreOrder_Traversal(node1)
print()
print()
print("Inorder Traversal is given Below: ")
InOrder_Traversal(node1)
print()
print("PostOrder Traversal is given Below: ")
PostOrder_Traversal(node1)

'''
Tree Given
                                15
                        10               2003
                    10       3       1980   1976
'''
        




