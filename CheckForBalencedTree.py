def isBalanced(self,root):
       #add code here
       if not root:
           return 1
       
       left_height = self.isBalanced(root.left)
       right_height = self.isBalanced(root.right)
       if left_height == 0 or right_height == 0 or abs(left_height - right_height) > 1:
               return False
       return 1 + max(left_height, right_height)
