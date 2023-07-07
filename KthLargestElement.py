def solve(self,root,k):

        if root==None:

            return

        self.solve(root.right,k)

        if self.ind==k:

            self.ans=root.data

            self.ind+=1

            return self.ans

        else:

            self.ind+=1

        self.solve(root.left,k)

        

    def kthLargest(self,root, k):

        self.ind=1

        self.ans=-9999

        self.solve(root,k)

        return self.ans
