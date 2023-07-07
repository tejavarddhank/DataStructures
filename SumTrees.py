def isSumTree(self,root):
        # Code here
        if(root==None):
            return True
        self.isSumTree(root.left)
        self.isSumTree(root.right)
        if(root.left ==None and root.right==None):
            return True
        sum=0
        if(root.left!=None):
            sum+=root.left.data
        if(root.right!=None):
            sum+=root.right.data
        if(root.data!=sum):
            return False
        root.data+=sum
        return True
