class Solution:
    #Function to check whether all nodes of a tree have the value 
    #equal to the sum of their child nodes.
    def isSumProperty(self, root):
        # code here
        
        if not root:
            return 1
            
        childSum = 0
        
        if root.left:
            childSum += root.left.data
        if root.right:
            childSum += root.right.data
            
        if root.left == None and root.right == None:
            return 1
            
        if root.data != childSum:
            return 0
        
        return self.isSumProperty(root.left) and self.isSumProperty(root.right)
