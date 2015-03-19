class TreeNode:
    # Definition for a  binary tree node
    # class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.left.right = TreeNode(5)
class Solution:
    # @param root, a tree node
    # @return a list of integers
    def inorderTraversal(self, root):
        # stack node and flag false if its children haven't been
        # checked/expanded, flag true if the node is expanded as
        # F_right, T_node, F_left
        # start to deal the element from the F_left
        # filter false, and anything else, until a T_node shows up
        # store the T_node value into accumulating vector 'acc'
        
        stack = [(False, root)]
        acc = []
        while stack != []:
            (flag, val) =  stack.pop()
            if val != None:
                if flag == False:
                    stack.append((False, val.right))
                    stack.append((True, val.val))
                    stack.append((False, val.left))
                else:
                    acc.append(val)
                    
        return acc

Solution().inorderTraversal(root)
