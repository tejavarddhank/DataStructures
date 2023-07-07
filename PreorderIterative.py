class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        result = []
        
        while True:
            while root:
                result.append(root.val)
                stack.append(root)
                root = root.left
            
            if len(stack) == 0:
                break
            
            root = stack.pop()
            root = root.right
        return result
