class Solution:

    def maxPathSum(self, root):

        def root_node(root):

            nonlocal sum1,maximum

            if root==None:

                return None   

            sum1+=root.data

            if root.left==None and root.right==None and sum1>maximum:

                maximum=sum1   

            if root_node(root.left) or root_node(root.right):

                return True

            sum1-=root.data

            return False    

        sum1,maximum=0,-9999

        root_node(root)

        return maximum
