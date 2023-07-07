class Solution:
    # Function to return the diameter of a Binary Tree.
    def diameter(self, root):
        if root is None:
            return 0
        
     
        left_height = self.height(root.left)
        right_height = self.height(root.right)
        
        left_diameter = self.diameter(root.left)
        right_diameter = self.diameter(root.right)
        return max(left_height + right_height + 1, max(left_diameter, right_diameter))
    
 
    def height(self, root):
        if root is None:
            return 0
        
        left_height = self.height(root.left)
        right_height = self.height(root.right)
        
        return max(left_height, right_height) + 1
