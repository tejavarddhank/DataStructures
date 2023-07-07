class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        tree = []
        
        def levelorder(node, depth=0):
            if len(tree) <= depth:
                tree.append([])

            tree[depth].append(node.val)
            if node.left:
                levelorder(node.left, depth+1)
            if node.right:
                levelorder(node.right, depth+1)
        if root:
            levelorder(root)
        
        return tree
