def removekeys(self, root, l, r):

        #code here

        if root is None:

            return None

        

        root.left=self.removekeys(root.left,l,r)

        root.right=self.removekeys(root.right,l,r)

        

        if root.data<l:

            right_child=root.right

            return right_child

        

        if root.data>r:

            left_child=root.left

            return left_child

        return root
