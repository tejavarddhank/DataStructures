class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        result = []
        
        while True:
            while root:
                stack.append(root)
                root = root.left
            
            if len(stack) == 0:
                break
            
            root = stack.pop()
            result.append(root.val)
            root = root.right
        return result
