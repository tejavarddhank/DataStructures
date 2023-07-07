class Solution:
    #Function to check if two trees are identical.
    def isIdentical(self,root1, root2):
        # Code here
        if root1 == None and root2 == None :
            return 1
            
        if root1 == None or root2 == None :
            return 0 
        if root1.data == root2.data :
            return self.isIdentical(root1.left,root2.left) and self.isIdentical(root1.right,root2.right)
        else :
            return 0
