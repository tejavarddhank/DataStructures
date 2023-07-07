class Solution:

  def solve(self,curr):

        if curr==None:return 0

        left=self.solve(curr.left)

        right=self.solve(curr.right)

        return max(left,right)+1

  def height(self, root):

        curr=root

        return self.solve(curr)
