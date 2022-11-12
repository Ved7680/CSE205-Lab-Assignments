'''
    AUTHOR: Ved J Nayi
    DOC: 12-11-22
    Objective: Implement breadth first search on a tree (not necessarily binary)
'''
class Tree_Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

mydict = {15:[10,2003],10:[11,3,16],2003:[1980,1976,1933]}

print(list(mydict.keys()))
print(mydict.get(10))

# def Breadth_First_Search(root):
#     if root is None:
#         return 
    
#     queue = [root]
    
#     while(len(queue) > 0):
#         curr_node = queue.pop(0)
#         print(curr_node.data,end=' ')

#         if curr_node.left is not None:
#             queue.append(curr_node.left)

#         if curr_node.right is not None:
#             queue.append(curr_node.right)

# root = Tree_Node(15)
# root.left = Tree_Node(10)
# root.right = Tree_Node(2003)
# root.left.left = Tree_Node(10)
# root.left.right = Tree_Node(3)
# root.right.left = Tree_Node(1980)
# root.right.right = Tree_Node(1976)

# Breadth_First_Search(root)