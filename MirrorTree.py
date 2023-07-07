class Solution:
    #Function to convert a binary tree into its mirror tree.
    def mirror(self,root):
        # Code here
        if root==None:
            return None
        ln=self.mirror(root.left)
        rn=self.mirror(root.right)
        root.left=rn
        root.right=ln
        return root
