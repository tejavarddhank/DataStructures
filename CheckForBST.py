class Solution:
    
    #Function to check whether a Binary Tree is BST or not.
    def isBST(self, root):
        #code here
        return isProperBST(root)
    
def isProperBST(root, min_value = float('-inf'), max_value = float('inf')):
    if root is None:
        return True
    if root.data <= min_value or root.data >= max_value:
        return False
    return (isProperBST(root.left, min_value, root.data) and isProperBST(root.right, root.data, max_value))
