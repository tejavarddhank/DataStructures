class Solution:

    def solve(self,nums,st,lst):
        if st>lst:
            return 
        mid=(st+lst)//2
        self.ans.append(nums[mid])
        self.solve(nums,st,mid-1)
        self.solve(nums,mid+1,lst)
        
    
    def sortedArrayToBST(self, nums):
        st=0
        lst=len(nums)-1
        self.ans=[]
        self.solve(nums,st,lst)
        return self.ans
